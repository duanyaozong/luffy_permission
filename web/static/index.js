  $(".c1").click(function () {
       $(this).css("color","red")
   });


   $(".c2").click(function () {


       $.ajax({
           url:"",
           type:"get",
           data:{
               name:$("#i1").attr("user")
           },
           success:function (res) {
               console.log(res)
           }
       })

   })