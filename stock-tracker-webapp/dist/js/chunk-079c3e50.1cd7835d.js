(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-079c3e50"],{"030f":function(t,e,o){},"765c":function(t,e,o){"use strict";o("030f")},a50a:function(t,e,o){"use strict";o.r(e);var r=function(){var t=this,e=t.$createElement,o=t._self._c||e;return o("v-card",{attrs:{id:t.symbol+"_year"},on:{plotly_relayout:function(e){return t.console.log("Relayout")}}})},a=[],n=(o("96cf"),o("1da1")),c=o("5530"),i=o("030a"),l=o.n(i),s=o("2f62"),u=o("db49"),p={name:"YearlyChart",props:{symbol:{type:String}},data:function(){return{config:u["a"]}},computed:Object(c["a"])(Object(c["a"])({},Object(s["e"])({timeSeries:function(t){return t.history.lastYear}})),Object(s["c"])(["isLastYearEmpty"])),methods:Object(c["a"])({plotChart:function(){var t={x:this.timeSeries.x,close:this.timeSeries.close,open:this.timeSeries.open,low:this.timeSeries.low,high:this.timeSeries.high,increasing:{line:{color:this.config.plt.trace.color.green}},decreasing:{line:{color:this.config.plt.trace.color.red}},type:"ohlc",xaxis:"x",yaxis:"y"},e=[t],o={dragmode:"zoom",showlegend:!1,plot_bgcolor:this.config.plt.layout.plot_bgcolor,paper_bgcolor:this.config.plt.layout.paper_bgcolor,font:{color:this.config.plt.layout.font.color},xaxis:{gridcolor:this.config.plt.layout.xaxis.gridcolor,autorange:!0,title:"Time",rangeselector:{x:0,y:1.2,xanchor:"left",font:{size:12,color:"black"},bgcolor:this.config.plt.rangeslider.buttons.bgcolor,activecolor:this.config.plt.rangeslider.buttons.activecolor,buttons:[{step:"month",stepmode:"backward",count:1,label:"1 MONTH"},{step:"month",stepmode:"backward",count:6,label:"6 MONTHS"},{step:"all",label:"1 YEAR"}]}},yaxis:{gridcolor:this.config.plt.layout.yaxis.gridcolor,autorange:!0,title:"Share Value [£p]"}},r={responsive:!0};l.a.newPlot(this.symbol+"_year",e,o,r)}},Object(s["b"])(["lastYearsTrace"])),mounted:function(){var t=this;return Object(n["a"])(regeneratorRuntime.mark((function e(){return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return console.log("YearlyChart: mounted, current route:",t.$route),e.next=3,t.lastYearsTrace(t.symbol);case 3:t.plotChart();case 4:case"end":return e.stop()}}),e)})))()}},g=p,h=(o("765c"),o("2877")),b=o("6544"),f=o.n(b),d=o("b0af"),m=Object(h["a"])(g,r,a,!1,null,"336e0912",null);e["default"]=m.exports;f()(m,{VCard:d["a"]})}}]);
//# sourceMappingURL=chunk-079c3e50.1cd7835d.js.map