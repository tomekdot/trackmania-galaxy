function md_gallery(options = {}) {
  const settings = {
    listType: 'ul',
    className: 'gallery',
    tagType: 'div',
    ...options,
  };

  const lists = document.querySelectorAll(`${settings.listType}.md-gallery`);

  lists.forEach((list) => {
    const gallery = document.createElement(settings.tagType);
    gallery.className = `${settings.className} gallery-cols-${list.children.length}`;

    Array.from(list.children).forEach((item) => {
      const figure = document.createElement('figure');
      const imageLink = item.querySelector('a[href]');
      const image = item.querySelector('img');

      if (!image) {
        return;
      }

      const captionText = image.getAttribute('alt') || '';
      const wrappedImage = image.cloneNode(true);

      if (imageLink) {
        const anchor = document.createElement('a');
        anchor.href = imageLink.getAttribute('href');
        anchor.appendChild(wrappedImage);
        figure.appendChild(anchor);
      } else {
        figure.appendChild(wrappedImage);
      }

      if (captionText) {
        const caption = document.createElement('figcaption');
        caption.textContent = captionText;
        figure.appendChild(caption);
      }

      gallery.appendChild(figure);
    });

    list.replaceWith(gallery);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  md_gallery();
});