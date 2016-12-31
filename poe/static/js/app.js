(function () {

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
})()
