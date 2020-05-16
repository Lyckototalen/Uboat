var seastuffObj = { "renderAtElId":"seastuff-timeline" };
seastuffObj.html = "";
seastuffObj.renderSealevel = function(sealevel) {
  return '' +
    '<div class="timeline-month">' +
      sealevel.name +
      '<span>'+
        sealevel.readableName +
      '</span>' +
    '</div>';
};
seastuffObj.renderDepthStart = function(depth) {
  return '' +
    '<div class="timeline-section">' +
      '<div class="timeline-date">' +
        depth.name +
      '</div>' +
      '<div class="row">';
};
seastuffObj.renderDepthEnd = function(depth) {
  return '</div></div>';
};
seastuffObj.renderStuff = function(stuff) {  console.log("r",stuff);
  return '' +
    '<div class="col-sm-4">' + 
      '<div class="timeline-box">' +
        '<div class="box-title">' +
        '<i class="fa fa-asterisk text-success" aria-hidden="true"></i>'+
          stuff.name +
        '</div>'+
        '<div class="box-content">'+
          '<a class="btn btn-xs btn-default pull-right">'+
            'Details'+
          '</a>' +
          '<div class="box-item">' +
            '<strong>Vikt</strong>' +
            stuff.weight +
          '</div>' +
          '<div class="box-item">' +
            '<strong>Ljud</strong>' +
            stuff.sound +
          '</div>' +    
        '</div>' +      
      '</div>' +
    '</div>';
};


$( document ).ready(function() {

  $.getJSON( "ajax/seastuff.json", function( seastuff ) {
    
    $.each( seastuff.sealevels, function( k1, sealevel ) {
      
      seastuffObj.html += seastuffObj.renderSealevel(sealevel);
      
      $.each( sealevel.depths, function( k2, depth ) {
        
        seastuffObj.html += seastuffObj.renderDepthStart(depth);
        
        $.each( depth.stuff, function( k3, stuff ) {
        
          seastuffObj.html += seastuffObj.renderStuff(stuff);
        
        });
        
        seastuffObj.html += seastuffObj.renderDepthEnd(depth);
        
      });
      
      
    });
    
    /*
    var items = [];
    $.each( data, function( key, val ) {
      items.push( "<li id='" + key + "'>" + val + "</li>" );
    });
 
    $( "<ul/>", {
      "class": "my-new-list",
      html: items.join( "" )
    }).appendTo( "body" );
    */
    $( seastuffObj.html ).appendTo( $('#'+seastuffObj.renderAtElId) );
    console.log(seastuffObj.html);
  });
    
});
  