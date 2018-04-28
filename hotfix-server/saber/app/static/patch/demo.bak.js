require('UIView, UIColor, UILabel, UIImage');

defineClass('AppDelegate', {
  genView: function() {
    var view = self.ORIGgenView();

    view.setBackgroundColor(UIColor.colorWithRed_green_blue_alpha(190.0 / 255.0, 190.0 / 255.0,190.0 / 255, 1.0));
    var label = UILabel.alloc().initWithFrame(view.frame());
    label.setText("VERSION - 01");
    label.setTextAlignment(1);
    view.addSubview(label);

    return view;
  }
});
