(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["home"],{bb51:function(t,e,r){"use strict";r.r(e);var n=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("div",[r("Articles")],1)},c=[],l=function(){var t=this,e=t.$createElement,r=t._self._c||e;return r("v-container",{attrs:{fluid:"","grid-list-md":""}},[r("h1",[t._v("Articles")]),r("v-layout",{attrs:{row:"",wrap:""}},t._l(t.allArticles,function(e){return r("v-flex",{key:e.id,attrs:{sm6:"",xs12:""}},[r("v-card",[r("v-card-title",{attrs:{"primary-title":""}},[r("h3",{staticClass:"headline mb-0"},[t._v(t._s(e.title))])]),r("v-card-text",[r("vue-markdown",[t._v(t._s(e.overview))])],1),r("v-card-actions",[r("v-btn",{attrs:{color:"orange"}},[t._v("Edit")]),r("v-btn",{attrs:{color:"orange"}},[t._v("Remove")])],1)],1)],1)}),1)],1)},o=[],a=r("2f62"),i=r("9ce6"),s=r.n(i);function u(t){for(var e=1;e<arguments.length;e++){var r=null!=arguments[e]?arguments[e]:{},n=Object.keys(r);"function"===typeof Object.getOwnPropertySymbols&&(n=n.concat(Object.getOwnPropertySymbols(r).filter(function(t){return Object.getOwnPropertyDescriptor(r,t).enumerable}))),n.forEach(function(e){v(t,e,r[e])})}return t}function v(t,e,r){return e in t?Object.defineProperty(t,e,{value:r,enumerable:!0,configurable:!0,writable:!0}):t[e]=r,t}var f={name:"Articles",components:{VueMarkdown:s.a},methods:u({},Object(a["b"])(["fetchArticles"])),computed:Object(a["c"])(["allArticles"]),created:function(){this.fetchArticles()}},b=f,d=r("2877"),m=Object(d["a"])(b,l,o,!1,null,null,null),p=m.exports,w={name:"home",components:{Articles:p}},h=w,O=Object(d["a"])(h,n,c,!1,null,null,null);e["default"]=O.exports}}]);
//# sourceMappingURL=home.js.map