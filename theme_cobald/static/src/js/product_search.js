odoo.define('theme_custom.product_search', function (require) {
'use strict';
var rpc= require('web.rpc')
var core = require('web.core');
var qweb = core.qweb;

$( document ).ready(function() {
    $(".search-query").keyup(function(){
        var product_search = $(this).val()
        rpc.query({route: '/advance_search_product',
            params:{
                product_search:product_search,
            },
        }).then(function(products) {
            var search = $('.search-query')
            if(products){
                $('.product_search_results').html(products);
            }
        });
    });

    $(".o_add_wishlist").click(function(){
        rpc.query({route: '/o_add_wishlist_count',}).then(function(wishcount) {
            if(wishcount){
                $('.wishcount_div').html(wishcount);
            }
        });
    });

});

});