# ہفتہ 4: ROS 2 کے بنیادی اصول (جاری ہے)

اس ہفتے، ہم ROS 2 کے بنیادی تصورات کی اپنی تفہیم پر مزید تعمیر کرتے ہیں اور مضبوط روبوٹ ایپلی کیشنز تیار کرنے کے لیے ضروری مزید جدید موضوعات کو تلاش کرتے ہیں۔ ہم کوالٹی آف سروس (QoS) کی ترتیبات، کلائنٹ لائبریریوں کی ساخت اور استعمال، اور پیچیدہ ROS 2 نظاموں کو ترتیب دینے میں لانچ فائلوں اور پیرامیٹر مینجمنٹ کے اہم کردار کا جائزہ لیں گے۔

## کوالٹی آف سروس (QoS) پالیسیاں

ROS 2 کی کوالٹی آف سروس (QoS) ترتیبات ڈویلپرز کو نوڈس کے درمیان مواصلات کی وشوسنییتا، تاخیر، اور لمبی عمر کو ترتیب دینے کی اجازت دیتی ہیں۔ یہ پالیسیاں ROS 2 کو مختلف ایپلی کیشن کی ضروریات کے مطابق ڈھالنے کے لیے اہم ہیں، اعلی تھروپٹ سینسر ڈیٹا سے لے کر اہم کنٹرول کمانڈز تک۔

اہم QoS پالیسیوں میں شامل ہیں:

- **تاریخ**: اس بات کا تعین کرتی ہے کہ مڈل ویئر کو کتنے نمونے یا کتنا وقت رکھنا چاہیے۔
    - `KEEP_LAST`: صرف N حالیہ نمونے ذخیرہ کیے جاتے ہیں۔
    - `KEEP_ALL`: تمام نمونے اس وقت تک ذخیرہ کیے جاتے ہیں جب تک کہ وسائل کی حدیں ختم نہ ہوجائیں۔
- **گہرائی**: `KEEP_LAST` تاریخ کے ساتھ استعمال کیا جاتا ہے تاکہ رکھنے کے لیے نمونوں کی تعداد کی وضاحت کی جا سکے۔
- **وشوسنییتا**: پیغام کی ترسیل کے بارے میں ضمانتیں۔
    - `BEST_EFFORT`: پیغامات پہنچانے کی کوشش کرتا ہے لیکن اگر نیٹ ورک بھیڑ بھاڑ والا ہو تو انہیں چھوڑ سکتا ہے۔ اعلی تعدد، غیر اہم ڈیٹا (جیسے، سینسر اسٹریمز) کے لیے موزوں۔
    - `RELIABLE`: ہر پیغام کی ترسیل کی ضمانت دیتا ہے، ممکنہ طور پر دوبارہ ترسیل کے ساتھ۔ اہم کنٹرول کمانڈز یا کنفیگریشن اپ ڈیٹس کے لیے ضروری ہے۔
- **پائیداری**: اس سے متعلق ہے کہ آیا پیغامات عارضی ہیں (صرف موجودہ سبسکرائبرز کے لیے دستیاب ہیں) یا مستقل ہیں (مستقبل کے سبسکرائبرز کے لیے دستیاب ہیں)۔
    - `VOLATILE`: نئے سبسکرائبرز کے لیے پیغامات برقرار نہیں رکھے جاتے۔
    - `TRANSIENT_LOCAL`: آخری شائع شدہ پیغام برقرار رکھا جاتا ہے اور نئے سبسکرائبرز کو پہنچایا جاتا ہے۔ کنفیگریشن ڈیٹا یا ابتدائی حالتوں کے لیے مفید ہے۔
- **زندگی**: مڈل ویئر یہ کیسے تعین کرتا ہے کہ آیا کوئی پبلشر اب بھی فعال ہے۔
    - `AUTOMATIC`: زندگی کا دعویٰ مڈل ویئر کے ذریعے خود بخود کیا جاتا ہے۔
    - `MANUAL_BY_TOPIC`: ایپلی کیشن واضح طور پر زندگی کا دعویٰ کرتی ہے۔
- **آخری تاریخ**: پیغامات کے درمیان زیادہ سے زیادہ متوقع وقت۔ اگر کوئی پبلشر اس کو پورا کرنے میں ناکام رہتا ہے، تو سبسکرائبرز کو مطلع کیا جاتا ہے۔
- **عمر**: وہ زیادہ سے زیادہ مدت جس کے لیے کوئی پیغام درست ہے۔ اپنی عمر سے پرانے پیغامات نہیں پہنچائے جاتے۔

مناسب QoS ترتیبات ایک تقسیم شدہ روبوٹک نظام کے صحیح رویے اور کارکردگی کو یقینی بنانے کے لیے بہت ضروری ہیں۔

## پائتھن کے ساتھ ROS 2 پیکجز بنانا

ROS 2 پیکجز ROS 2 کوڈ کے لیے تنظیم کی بنیادی اکائی ہیں۔ ان میں نوڈس، لانچ فائلیں، کنفیگریشن، اور دیگر وسائل شامل ہوتے ہیں۔ پائتھن کی ترقی کے لیے، `ament_python` بلڈ ٹول ہے، اور `setup.py` پیکیج کی وضاحت کرتا ہے۔

ایک پائتھن پیکیج بنانے اور بنانے کے اقدامات:

1. **پیکیج بنائیں**:
    ```bash
    ros2 pkg create --build-type ament_python my_python_package
    ```
2. **نوڈ انٹری پوائنٹس کی وضاحت کریں**: `setup.py` میں، اپنی قابل عمل پائتھن اسکرپٹس کے لیے انٹری پوائنٹس کی وضاحت کریں:
    ```python
    entry_points={
        'console_scripts': [
            'my_node = my_python_package.my_node:main',
        ],
    },
    ```
    جہاں `my_node` آپ کے قابل عمل کا نام ہے، `my_python_package` پائتھن ماڈیول (فولڈر) ہے، اور `my_node` پائتھن فائل ہے جس میں `main` فنکشن ہے۔
3. **نوڈ منطق کو نافذ کریں**: `rclpy` کا استعمال کرتے ہوئے اپنی ROS 2 نوڈ منطق کو پائتھن میں لکھیں۔
    ```python
    # my_python_package/my_node.py
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class MyPublisher(Node):
        def __init__(self):
            super().__init__('my_publisher')
            self.publisher_ = self.create_publisher(String, 'topic', 10)
            timer_period = 0.5  # seconds
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.i = 0

        def timer_callback(self):
            msg = String()
            msg.data = 'Hello ROS 2: %d' % self.i
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1

    def main(args=None):
        rclpy.init(args=args)
        my_publisher = MyPublisher()
        rclpy.spin(my_publisher)
        my_publisher.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```
4. **بنائیں**:
    ```bash
    colcon build --packages-select my_python_package
    ```
5. **ماخذ اور چلائیں**:
    ```bash
    source install/setup.bash
    ros2 run my_python_package my_node
    ```

## لانچ فائلیں اور پیرامیٹر مینجمنٹ

پیچیدہ روبوٹک نظاموں میں اکثر بہت سے نوڈس شامل ہوتے ہیں، جن میں سے ہر ایک کے مختلف پیرامیٹرز ہوتے ہیں۔ **لانچ فائلیں** ایک ہی وقت میں ایک سے زیادہ ROS 2 نوڈس کو شروع کرنے اور ترتیب دینے کا ایک آسان طریقہ فراہم کرتی ہیں۔ وہ عام طور پر پائتھن یا XML میں لکھی جاتی ہیں۔

### پائتھن لانچ فائلیں
پائتھن لانچ فائلیں زیادہ لچک اور پروگراماتی کنٹرول پیش کرتی ہیں۔

**مثال (`my_robot_launch.py`):**
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_python_package',
            executable='my_node',
            name='my_publisher_node',
            output='screen',
            parameters=[
                {'publish_frequency': 1.0},
                {'message_prefix': 'Robot says: '}
            ]
        ),
        Node(
            package='another_package',
            executable='another_node',
            name='my_subscriber_node',
            output='log',
        ),
    ])
```
چلانے کے لیے: `ros2 launch my_python_package my_robot_launch.py`

### پیرامیٹر مینجمنٹ
پیرامیٹرز آپ کو کوڈ کو دوبارہ مرتب کیے بغیر نوڈس کے رویے کو ترتیب دینے کی اجازت دیتے ہیں۔

- **اعلان**: پیرامیٹرز ایک نوڈ کے اندر اعلان کیے جاتے ہیں (جیسے، `self.declare_parameter('my_parameter', 'default_value')`)۔
- **رسائی**: نوڈس پیرامیٹر کی قدریں حاصل کرسکتے ہیں (`self.get_parameter('my_parameter').value`)۔
- **کنفیگریشن**:
    - **لانچ فائلوں کے ذریعے**: جیسا کہ اوپر دکھایا گیا ہے، پیرامیٹرز کو براہ راست `Node` اعلانات میں سیٹ کیا جاسکتا ہے۔
    - **YAML فائلوں کے ذریعے**: زیادہ پیچیدہ کنفیگریشنز کے لیے پیرامیٹرز کو YAML فائلوں سے لوڈ کیا جاسکتا ہے:
        ```yaml
        my_publisher_node:
            ros__parameters:
                publish_frequency: 2.0
                message_prefix: "YAML configured: "
        ```
        پھر، لانچ فائل میں YAML کا حوالہ دیں:
        ```python
        from ament_index_python.packages import get_package_share_directory
        import os

        # ...
        Node(
            package='my_python_package',
            executable='my_node',
            name='my_publisher_node',
            output='screen',
            parameters=[os.path.join(
                get_package_share_directory('my_python_package'),
                'config',
                'my_params.yaml'
            )]
        ),
        # ...
        ```
    - **متحرک طور پر**: پیرامیٹرز کو `ros2 param set` اور `ros2 param get` کمانڈز کا استعمال کرتے ہوئے رن ٹائم پر سیٹ اور بازیافت کیا جاسکتا ہے۔

لانچ فائلوں اور پیرامیٹر مینجمنٹ کو سمجھنا قابل توسیع اور آسانی سے قابل ترتیب ROS 2 روبوٹ نظام بنانے کے لیے بہت ضروری ہے۔ یہ اوزار انفرادی ماڈیولر اجزاء سے پیچیدہ طرز عمل کی ترتیب کو قابل بناتے ہیں، جو کامیاب روبوٹک تعیناتیوں کا سنگ بنیاد ہے۔
