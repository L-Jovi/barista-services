require('UIView, UIColor, UILabel, UIImage');

defineClass('AppDelegate', {
  genView: function() {
    var view = self.ORIGgenView();

    view.setBackgroundColor(UIColor.colorWithPatternImage(UIImage.imageNamed("static/ant.jpg")));
    var label = UILabel.alloc().initWithFrame(view.frame());
    label.setText("VERSION - 03");
    label.setTextAlignment(1);
    view.addSubview(label);

    return view;
  }
});
