function getfac(a)
{
	console.log(a);
        $.post(
                  "fetchfac.html",
                  { key: a },
                  function(data)
                  {
                     $('#data').html(data);
                  }
               );
}
