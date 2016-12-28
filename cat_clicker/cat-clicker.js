var model = {
    currentCat: null,
    cats: [
        {
            clickCount: 0,
            name: 'Tiggy',
            imgSrc: 'cat.jpg'
        }, {
            clickCount: 0,
            name: 'Muffin',
            imgSrc: 'cat1.jpg'
        }, {
            clickCount: 0,
            name: 'Peppa',
            imgSrc: 'cat2.jpg'
        }, {
            clickCount: 0,
            name: 'Jess',
            imgSrc: 'cat3.jpg'
        }, {
            clickCount: 0,
            name: 'Dain',
            imgSrc: 'cat4.jpg'
        }, {
            clickCount: 0,
            name: 'Kira',
            imgSrc: 'cat5.jpg'
        }, {
            clickCount: 0,
            name: 'Ming',
            imgSrc: 'cat6.jpg'
        }, {
            clickCount: 0,
            name: 'Callie',
            imgSrc: 'cat7.jpg'
        }, {
            clickCount: 0,
            name: 'Socks',
            imgSrc: 'cat8.jpg'
        }, {
            clickCount: 0,
            name: 'Patches',
            imgSrc: 'cat9.jpg'
        }
    ]
};

var octopus = {
    init: function() {
        model.currentCat = model.cats[0];
        catListView.init();
        catView.init();
    },
    getCurrentCat: function() {
        return model.currentCat;
    },

    getCats: function() {
        return model.cats;
    },

    setCurrentCat: function(cat) {
        model.currentCat = cat;
    },

    incrementCounter: function() {
        model.currentCat.clickCount++;
        catView.render();
    }
};

var catView = {
    init: function() {
        this.catElem = document.getElementById('cat');
        this.catNameElem = document.getElementById('cat-name');
        this.catImageElem = document.getElementById('cat-img');
        this.countElem = document.getElementById('cat-count');

        this.catImageElem.addEventListener('click', function(e) {
           octopus.incrementCounter();
        });

        this.render();
    },

    render: function() {
        var currentCat = octopus.getCurrentCat();
        this.countElem.textContent = currentCat.clickCount;
        this.catNameElem.textContent = currentCat.name;
        this.catImageElem.src = currentCat.imgSrc;
    }
};

var catListView = {
  init: function() {
      this.catListElem = document.getElementById('cat-list');
      this.render()
  },
  render: function() {
      var cats = octopus.getCats();
      this.catListElem.innerHTML = '';

      for (var i = 0; i < cats.length; i++) {
        var cat = cats[i]
        var elem = document.createElement('li');
        elem.textContent = cat.name;

        elem.addEventListener('click', (function(cat) {
            return function() {
                octopus.setCurrentCat(cat);
                catView.render()
            };
        })(cat));

        this.catListElem.appendChild(elem);
      };
  }
};

octopus.init()
