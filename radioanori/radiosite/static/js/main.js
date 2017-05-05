$(document).ready(function() {
        $("submit").click(function(){
            var favorite = [];
            $.each($("input[name='pesquisa']:checked"), function(){            
                favorite.push($(this).val());
                
            });
            
            alert("My favourite sports are: " + favorite.join(", "));
            
            $.ajax({
                type:'POST',
                url:'pesquisa/',
                data:{
                    favorite:favorite
                }
            });
        });
    });
