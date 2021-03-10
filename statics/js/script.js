$('a[data-imagelightbox="demo"]').imageLightbox({
    selector:       'a[data-imagelightbox]',
    id:             'imagelightbox',
    allowedTypes:   'png|jpg|jpeg|gif',
    animationSpeed: 250,
    activity:       true,
    arrows:         true,
    button:         true,
    caption:        true,
    enableKeyboard: true,
    lockBody:       true,
    navigation:     true,
    overlay:        true,
    preloadNext:    true,
    quitOnEnd:      true,
    quitOnImgClick: true,
    quitOnDocClick: true,
    quitOnEscKey:   true
});