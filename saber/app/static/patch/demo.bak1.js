require('UIView, UIColor, UILabel, UIImage');

defineClass('AppDelegate', {
  genView: function() {
    var view = self.ORIGgenView();

    view.setBackgroundColor(UIColor.colorWithPatternImage(UIImage.imageNamed("static/eva.jpg")));
    var label = UILabel.alloc().initWithFrame(view.frame());
    label.setText("VERSION - 02");
    label.setTextAlignment(1);
    view.addSubview(label);

    return view;
  }
});
