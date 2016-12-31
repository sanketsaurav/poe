(function () {

  var getText = function (content) {
    return content.replace(/<\/?[^>]+(>|$)/g, "")
  }

  var showErrorNotice = function (msg) {
    var el = document.getElementById('error-notice')
    el.innerText = msg
    el.style.marginTop = 0
    window.setTimeout(function () {
      el.style.marginTop = ''
    }, 3000)
  }

  var createNewPost = function () {
    // prepare the post data
    var post = {
      title: title.getContent(),
      content: content.getContent(),
      author: document.getElementById('author').value
    }

    if (!(getText(post.content))) {
      showErrorNotice('You cannot create an empty post.')
      return
    }

    var request = new XMLHttpRequest()
    request.open('POST', '/', true)
    request.setRequestHeader('Content-Type', 'application/json')

    request.onload = function () {
      if (request.status >= 200 && request.status < 400) {
        // post creation is successful
        resp = JSON.parse(request.responseText)

        // redirect to the post page
        window.location = '/' + resp.slug

      } else {
        // some error has occured
        showErrorNotice('An error has occured. Please try again.')
      }
    }

    request.onerror = function() {
      showErrorNotice('Error reaching Poe server.')
    }

    request.send(JSON.stringify(post))

  }

  // initialize the editors

  var title = new MediumEditor('#title', {
    toolbar: false,
    placeholder: {
      text: 'Title',
      hideOnClick: false
    }
  })

  var content = new MediumEditor('#content', {
    anchorPreview: false,
    placeholder: {
      text: 'You have something to say. Write it down...',
      hideOnClick: false
    }
  })

  // set focus to content field
  window.setTimeout(function () {
    content.elements[0].focus()
  }, 0)

  // attach listener to publish button
  var publishButton = document.getElementById('publish')
  publishButton.addEventListener('click', function () {
    createNewPost()
  }, false)

})()
