URDF/SRDFとロボットモデルの仕様
====================================

---------------
URDF
---------------

ロボットの関節、リンク、干渉形状、関節角度制限などを記述するROSのロボットモデル記述形式です。

詳しい仕様は、以下の外部ドキュメントを参照してください。

https://wiki.ros.org/urdf/XML


---------------
SRDF
---------------

MoveIt!がURDFに加えて利用するロボットモデルの記述形式です。
グループ、キネマティックチェーン、エンドエフェクタ名、干渉ペアの指定を行います。

詳しい仕様は、以下の外部ドキュメントを参照してください。

https://wiki.ros.org/srdf


SRDFファイルは、MoveIt Setup Assistantを使って生成できます。詳しくは以下の外部ドキュメントを参照してください。

http://docs.ros.org/melodic/api/moveit_tutorials/html/doc/setup_assistant/setup_assistant_tutorial.html


---------------
モデルローダー
---------------

URDFとSRDFファイルをロードするユーティリティクラスです。運動学プラグインのロードにも使われます。

.. doxygenclass:: robot_model_loader::RobotModelLoader
   :members:

---------------
ロボットモデル
---------------

.. doxygenclass:: moveit::core::RobotModel
   :members:

.. .. doxygenclass:: moveit::core::LinkModel
   :members:

.. .. doxygenclass:: moveit::core::JointModel
   :members:

.. .. doxygenclass:: moveit::core::RobotState
   :members:
