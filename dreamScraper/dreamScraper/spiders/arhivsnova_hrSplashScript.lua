--[[
Lua script written to render page http://arhivsnova.hr/archive through Splash
It does not work
]]

local treat = require('treat')

function main(splash, args)
    assert(splash:go(args.url))
    splash:set_viewport_full()

    local scroll_delay = 0.1
    local num_scrolls = 100
    local scroll_to = splash:jsfunc("window.scrollTo")

    local get_body_height = splash:jsfunc(
        "function() {return document.body.scrollHeight;}"
    )

    for _ = 1, num_scrolls do
        scroll_to(0, get_body_height())
        splash:wait(scroll_delay)
    end


  	local dreams = {}

    local js_container = splash:select_all('ul#dreams a')

  	for _, link in treat.as_array(js_container) do
    	splash:runjs(link.node.attributes.href)

        --[[
        local info_container = splash:select('div#popup-inner p')

        local text_container = treat.as_array(info_container)[2]

        dreams.newKey = text_container:text()
        --]]

        local text_container = splash:select('div#popup-inner .dream-excerpt p')
        dreams.newKey = text_container:text()

        --dreams.newKey = treat.as_array(info_container)[2]:text()

    end



    --return splash:html()
    return treat.as_array(dreams)
end