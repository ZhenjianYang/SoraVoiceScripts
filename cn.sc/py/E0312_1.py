from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'E0312_1 ._SN',
        MapName             = 'Event',
        Location            = 'E0312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/E0312   ._SN',
            'ED6_DT21/E0312_1 ._SN',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    FadeToDark(300, 0, 100)
    OP_22(0x9D, 0x0, 0x64)
    SetChrName("CAPEL")
    SetMessageWindowPos(250, 78, 36, 12)

    AnonymousTalk(    #0
        (
            "\x07\x02#1SThe Orbal Calculator\x01",
            "CAPEL SYSTEM Ver.7.0\x01",
            "Copyright(C)Z.C.F. 1197-1202\x01",
            "MODE:Information Retrieval\x01",
            "#200W　#20W\x01",
            "MEMORY_CHECK#100W..........#20WＯＫ!\x01",
            "#200W　#20W\x01",
            "#1S已连接到数据库。\x01",
            "请选择要搜索的内容。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F26")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x0, 0x37, 0x50, 0x1)
    OP_CC(0x1, 0x0, "【中央工房关联】")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 3)), scpexpr(EXPR_END)), "loc_1EE")
    OP_CC(0x1, 0x0, "【数据水晶】")

    label("loc_1EE")

    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_205"),
        (1, "loc_1585"),
        (SWITCH_DEFAULT, "loc_4F16"),
    )


    label("loc_205")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1585")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        55,
        153,
        1,
        (
            "【设立·沿革】\x01",            # 0
            "【技术一览】\x01",              # 1
            "【关连信息搜索】　　\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26E"),
        (1, "loc_8C1"),
        (2, "loc_12A4"),
        (SWITCH_DEFAULT, "loc_1575"),
    )


    label("loc_26E")


    AnonymousTalk(    #1
        (
            "\x07\x02#1S【Ｓ１１５４】（Ｓ…七耀历）\x01",
            "Ｃ·爱普斯泰恩博士于列曼自治州去世。\x01",
            "【Ｓ１１５５】\x01",
            "Ａ·拉赛尔博士回到利贝尔王国。\x01",
            "回国后提倡普及导力器技术，\x01",
            "但没有得到世人的认可和支持。\x01",
            "【Ｓ１１５７】\x01",
            "拉赛尔博士带领蔡斯的钟表工匠普及导力器。\x01",
            "同年，『蔡斯技术工房』（即之后的中央工房）设立。\x01",
            "【Ｓ１１６０】\x01",
            "埃德佳Ⅲ世在视察蔡斯技术工房后提供巨额资金建设工\x01",
            "房。拉赛尔博士出任首任工房长。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #2
        (
            "\x07\x02#1S【Ｓ１１６２】\x01",
            "埃德佳Ⅲ世去世。艾莉茜雅Ⅱ世即位。\x01",
            "【Ｓ１１６４】\x01",
            "『伦格兰德大桥』落成。\x01",
            "【Ｓ１１６８】\x01",
            "首部导力飞船『加拉托拉巴号』诞生。\x01",
            "（经过３９次飞行实验失败后的产物）\x01",
            "【Ｓ１１７３】\x01",
            "蔡斯技术工房开始对共和国乌尔努社和帝国莱恩福尔特\x01",
            "社输出导力器技术。工房改名为『中央工房』。\x01",
            "【Ｓ１１７５】\x01",
            "飞船公社设立。定期船『林德号』开始服役。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #3
        (
            "\x07\x02#1S【Ｓ１１７７】\x01",
            "定期船『赛希莉亚号』开始服役。\x01",
            "【Ｓ１１７８】\x01",
            "移动工房船『莱普尼兹号』竣工。\x01",
            "【Ｓ１１８０】\x01",
            "中央工房搬迁（即现在的建筑物）。\x01",
            "开掘卡鲁迪亚平原丘陵的一角，地下工房建成。\x01",
            "【Ｓ１１８２】\x01",
            "拉赛尔工房长退休。\x01",
            "玛多克技术主任出任第二任工房长。\x01",
            "【Ｓ１１８５】\x01",
            "自然科学和医学研究部门设立。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #4
        (
            "\x07\x02#1S【Ｓ１１８７】\x01",
            "客船『埃迪鲁那号』在卡尔瓦德领海沉没。\x01",
            "尤迪斯王太子夫妇去世。\x01",
            "【Ｓ１１９０】\x01",
            "与爱普斯泰恩财团合作，\x01",
            "发表了『导力网络』的构想。\x01",
            "【Ｓ１１９２】\x01",
            "『百日战役』爆发。\x01",
            "中央工房被埃雷波尼亚帝国接管。\x01",
            "拉赛尔博士在雷斯顿要塞开发出警备飞艇，\x01",
            "并将其用于反攻作战中，取得了显赫的战功，\x01",
            "从此警备飞艇作为王国军的主力兵器被广泛使用。\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #5
        (
            "\x07\x02#1S【Ｓ１１９３】\x01",
            "利贝尔王国和埃雷波尼亚帝国缔结和平条约。\x01",
            "战后，王国再次向帝国输出导力器。\x01",
            "【Ｓ１１９７】\x01",
            "导力演算器『卡佩尔』Ver.1完成。\x01",
            "【Ｓ１１９９】\x01",
            "高速巡洋舰『埃尔赛尤』开发工程开始。\x01",
            "【Ｓ１２０２】\x01",
            "高速巡洋舰『埃尔赛尤』竣工，进入试飞阶段。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1582")

    label("loc_8C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1294")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        259,
        1,
        (
            "【导力器】\x01",          # 0
            "【结晶回路】\x01",        # 1
            "【七耀石】\x01",          # 2
            "【导力飞船】\x01",        # 3
            "【导力兵器】\x01",        # 4
            "【战术导力器】\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_951"),
        (1, "loc_AD4"),
        (2, "loc_B9E"),
        (3, "loc_CB6"),
        (4, "loc_DEB"),
        (5, "loc_F60"),
        (SWITCH_DEFAULT, "loc_1284"),
    )


    label("loc_951")


    AnonymousTalk(    #6
        (
            "\x07\x02#1S项目：导力器（Orbment）\x01",
            "在半世纪前由Ｃ·爱普斯泰恩博士所发明，是能从七耀\x01",
            "石中提取导力，从而引发各种各样现象的机械装置的总\x01",
            "称。导力器内部的构造和齿轮的运动，使加工七耀石而\x01",
            "成的结晶回路相互干涉，可以引发丰富多彩的现象。导\x01",
            "力器的实用性，除了能产生丰富现象以外，还在于拥有\x01",
            "『经过一段时间内部的导力可以自然恢复』这种特异的\x01",
            "便利性。另外，经济效率也要远远地领先于各种外燃、\x01",
            "内燃机。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1291")

    label("loc_AD4")


    AnonymousTalk(    #7
        (
            "\x07\x02#1S项目：结晶回路（Quartz）\x01",
            "将七耀石的碎片（耀晶片，Sepith）精制、加工而成的\x01",
            "具有结晶构造的回路。作为能量源的同时，本身还是引\x01",
            "起各种各样现象的装置。但结晶回路必须安装在导力器\x01",
            "内才可以发挥作用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1291")

    label("loc_B9E")


    AnonymousTalk(    #8
        (
            "\x07\x02#1S项目：七耀石（Septium）\x01",
            "是在大陆全土分布的７种贵重矿石的总称。因被人们称\x01",
            "为『古代的宝石』、『神秘的象征』而变得珍重。近代\x01",
            "一种将体积过小不能成为宝石的碎片（耀晶片）精制加\x01",
            "工制作出结晶回路的技术被发明出来，因此导致七耀石\x01",
            "资源的重要性在大陆诸国之间一夜之间变得十分重要。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1291")

    label("loc_CB6")


    AnonymousTalk(    #9
        (
            "\x07\x02#1S项目：导力飞船\x01",
            "导力飞船可以称得上是导力技术精华凝聚而成的结晶。\x01",
            "集合了用于重力制御的大型飞翔引擎和供给大量能量的\x01",
            "导力引擎两大技术，使得如此大的飞船在空中飞行成为\x01",
            "可能。\x01",
            "为了实现高效率的导力传送和十分复杂的船体控制，最\x01",
            "新的飞船大多搭载了高性能的导力演算器。２０亚矩以\x01",
            "下的小型飞船又被称为『飞艇』。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1291")

    label("loc_DEB")


    AnonymousTalk(    #10
        (
            "\x07\x02#1S项目：导力兵器\x01",
            "即以导力枪、导力炮作为代表，使用导力技术的兵器体\x01",
            "系。现在已成为大多数国家军队的主力装备。\x01",
            "导力枪枪管内具有能将能量按照螺旋线聚集并高速射出\x01",
            "豆粒大小的金属子弹的构造，与发射火药的枪相比，填\x01",
            "弹量大幅增加，而且还能够调节枪的威力。\x01",
            "导力炮则可以发射封装了能量的炮弹（导力弹）并产生\x01",
            "爆炸，与发射火药的炮相比，其后坐力小，而且也可以\x01",
            "自由调节威力大小。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1291")

    label("loc_F60")


    AnonymousTalk(    #11
        (
            "\x07\x02#1S项目：战术导力器\x01",
            "可以发动导力魔法的导力器。大小和怀表差不多，内部\x01",
            "构造则相当精致优雅。\x01",
            "战术导力器具有安装结晶回路后能够提高持有者能力的\x01",
            "设计，使内部结晶回路与持有者达到同步，引发出『共\x01",
            "鸣现象』，以代替传统释放魔法所需的复杂的齿轮和驱\x01",
            "动装置，使持有者能够发动各种导力魔法。\x01",
            "而且，根据复数结晶回路属性和势能的组合不同，持有\x01",
            "者能够使用的导力魔法也会发生变化，具有相当的灵活\x01",
            "性。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #12
        (
            "\x07\x02#1S追加：新型战术导力器\x01",
            "作为战术导力器的开发者，爱普斯泰恩财团对过去的型号进\x01",
            "行大幅改良，并且成功投入实用的新规格战术导力器。和过\x01",
            "去只有六个结晶回路插槽的旧型号相比，这种新型号则具备\x01",
            "了七个结晶回路插槽，可以实现更为灵活的结晶回路组合。\x01",
            "新型号不仅使可以使用的魔法变得多元化，而且使其威力也\x01",
            "得到了飞跃性的提升。但是，由于新型号和过去型号的基本\x01",
            "构造有很大的不同，新型战术导力器也有着无法互换结晶回\x01",
            "路的缺陷。\x01",
            "　\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1291")

    label("loc_1284")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1291")

    label("loc_1291")

    Jump("loc_8C1")

    label("loc_1294")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_1582")

    label("loc_12A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1565")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        55,
        255,
        1,
        (
            "【内燃机】\x01",      # 0
            "【汽油】\x01",        # 1
            "【运输车】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_12FB"),
        (1, "loc_13CC"),
        (2, "loc_1478"),
        (SWITCH_DEFAULT, "loc_1555"),
    )


    label("loc_12FB")


    AnonymousTalk(    #13
        (
            "\x07\x02#1S项目：内燃机\x01",
            "在机关装置内燃烧燃料以获得能量的动力源。与导力机\x01",
            "关相比经济效率低下，而且还会产生噪音、废气等各种\x01",
            "问题，因此已经停止开发和生产。\x01\x01",
            "『内燃机部件』\x01",
            "库存量：１台\x01",
            "管理责任人：格斯塔夫维修长\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_13CC")


    AnonymousTalk(    #14
        (
            "\x07\x02#1S项目：汽油\x01",
            "将天然产生的液态碳氢化合物（石油）分馏、精制而成\x01",
            "的液体。常作为内燃引擎设备的燃料以及工业生产的溶\x01",
            "剂使用。\x01\x01",
            "共和国产汽油\x01",
            "储备量：无（已向共和国订购）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_1478")

    OP_28(0x29, 0x1, 0x8000)

    AnonymousTalk(    #15
        (
            "\x07\x02#1S项目：运输车\x01",
            "使用导力引擎驱动的各种车辆的总称。因为乘坐的舒适\x01",
            "度较差，速度也很慢，所以基本不用于客运方面，而主\x01",
            "要用来进行中短距离的货物运输。\x01\x01",
            "『运输车用驱动导力器』\x01",
            "库存量：不明\x01",
            "保管地点：地下工场搬入口\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1562")

    label("loc_1555")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1562")

    label("loc_1562")

    Jump("loc_12A4")

    label("loc_1565")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x2)
    Jump("loc_1582")

    label("loc_1575")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1582")

    label("loc_1582")

    Jump("loc_205")

    label("loc_1585")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F06")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CC(0x0, 0x1, 0x37, 0x99, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 0)), scpexpr(EXPR_END)), "loc_15CC")
    OP_CC(0x1, 0x1, "＃０　　阅览完毕")
    Jump("loc_15FE")

    label("loc_15CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_15EC")
    OP_CC(0x1, 0x1, "＃０　　分析完成！")
    Jump("loc_15FE")

    label("loc_15EC")

    OP_CC(0x1, 0x1, "＃０　　分析中")

    label("loc_15FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 7)), scpexpr(EXPR_EXEC_OP, "OP_40(0x3FE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 1)), scpexpr(EXPR_END)), "loc_1639")
    OP_CC(0x1, 0x1, "＃１　　阅览完毕")
    Jump("loc_166B")

    label("loc_1639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1659")
    OP_CC(0x1, 0x1, "＃１　　分析完成！")
    Jump("loc_166B")

    label("loc_1659")

    OP_CC(0x1, 0x1, "＃１　　分析中")

    label("loc_166B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 0)), scpexpr(EXPR_EXEC_OP, "OP_40(0x3FF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16D8")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 2)), scpexpr(EXPR_END)), "loc_16A6")
    OP_CC(0x1, 0x1, "＃２　　阅览完毕")
    Jump("loc_16D8")

    label("loc_16A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_16C6")
    OP_CC(0x1, 0x1, "＃２　　分析完成！")
    Jump("loc_16D8")

    label("loc_16C6")

    OP_CC(0x1, 0x1, "＃２　　分析中")

    label("loc_16D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 1)), scpexpr(EXPR_EXEC_OP, "OP_40(0x400, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1745")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 3)), scpexpr(EXPR_END)), "loc_1713")
    OP_CC(0x1, 0x1, "＃３　　阅览完毕")
    Jump("loc_1745")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1733")
    OP_CC(0x1, 0x1, "＃３　　分析完成！")
    Jump("loc_1745")

    label("loc_1733")

    OP_CC(0x1, 0x1, "＃３　　分析中")

    label("loc_1745")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 6)), scpexpr(EXPR_EXEC_OP, "OP_40(0x401, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 4)), scpexpr(EXPR_END)), "loc_1780")
    OP_CC(0x1, 0x1, "＃４　　阅览完毕")
    Jump("loc_17B2")

    label("loc_1780")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_17A0")
    OP_CC(0x1, 0x1, "＃４　　分析完成！")
    Jump("loc_17B2")

    label("loc_17A0")

    OP_CC(0x1, 0x1, "＃４　　分析中")

    label("loc_17B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 7)), scpexpr(EXPR_EXEC_OP, "OP_40(0x402, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_181F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 5)), scpexpr(EXPR_END)), "loc_17ED")
    OP_CC(0x1, 0x1, "＃５　　阅览完毕")
    Jump("loc_181F")

    label("loc_17ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_180D")
    OP_CC(0x1, 0x1, "＃５　　分析完成！")
    Jump("loc_181F")

    label("loc_180D")

    OP_CC(0x1, 0x1, "＃５　　分析中")

    label("loc_181F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 0)), scpexpr(EXPR_EXEC_OP, "OP_40(0x403, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_188C")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x20), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 6)), scpexpr(EXPR_END)), "loc_185A")
    OP_CC(0x1, 0x1, "＃６　　阅览完毕")
    Jump("loc_188C")

    label("loc_185A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_187A")
    OP_CC(0x1, 0x1, "＃６　　分析完成！")
    Jump("loc_188C")

    label("loc_187A")

    OP_CC(0x1, 0x1, "＃６　　分析中")

    label("loc_188C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x404, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x450, 7)), scpexpr(EXPR_END)), "loc_18C7")
    OP_CC(0x1, 0x1, "＃７　　阅览完毕")
    Jump("loc_18F9")

    label("loc_18C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_18E7")
    OP_CC(0x1, 0x1, "＃７　　分析完成！")
    Jump("loc_18F9")

    label("loc_18E7")

    OP_CC(0x1, 0x1, "＃７　　分析中")

    label("loc_18F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 3)), scpexpr(EXPR_EXEC_OP, "OP_40(0x405, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1966")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 0)), scpexpr(EXPR_END)), "loc_1934")
    OP_CC(0x1, 0x1, "＃８　　阅览完毕")
    Jump("loc_1966")

    label("loc_1934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_1954")
    OP_CC(0x1, 0x1, "＃８　　分析完成！")
    Jump("loc_1966")

    label("loc_1954")

    OP_CC(0x1, 0x1, "＃８　　分析中")

    label("loc_1966")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 4)), scpexpr(EXPR_EXEC_OP, "OP_40(0x406, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19D3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 1)), scpexpr(EXPR_END)), "loc_19A1")
    OP_CC(0x1, 0x1, "＃９　　阅览完毕")
    Jump("loc_19D3")

    label("loc_19A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_19C1")
    OP_CC(0x1, 0x1, "＃９　　分析完成！")
    Jump("loc_19D3")

    label("loc_19C1")

    OP_CC(0x1, 0x1, "＃９　　分析中")

    label("loc_19D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 1)), scpexpr(EXPR_EXEC_OP, "OP_40(0x407, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1A40")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 2)), scpexpr(EXPR_END)), "loc_1A0E")
    OP_CC(0x1, 0x1, "＃１０　阅览完毕")
    Jump("loc_1A40")

    label("loc_1A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_1A2E")
    OP_CC(0x1, 0x1, "＃１０　分析完成！")
    Jump("loc_1A40")

    label("loc_1A2E")

    OP_CC(0x1, 0x1, "＃１０　分析中")

    label("loc_1A40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x408, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1AAD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x400), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x451, 3)), scpexpr(EXPR_END)), "loc_1A7B")
    OP_CC(0x1, 0x1, "＃１１　阅览完毕")
    Jump("loc_1AAD")

    label("loc_1A7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_1A9B")
    OP_CC(0x1, 0x1, "＃１１　分析完成！")
    Jump("loc_1AAD")

    label("loc_1A9B")

    OP_CC(0x1, 0x1, "＃１１　分析中")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 3)), scpexpr(EXPR_EXEC_OP, "OP_40(0x409, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B1A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x800), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44E, 6)), scpexpr(EXPR_END)), "loc_1AE8")
    OP_CC(0x1, 0x1, "＃１２　阅览完毕")
    Jump("loc_1B1A")

    label("loc_1AE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1B08")
    OP_CC(0x1, 0x1, "＃１２　分析完成！")
    Jump("loc_1B1A")

    label("loc_1B08")

    OP_CC(0x1, 0x1, "＃１２　分析中")

    label("loc_1B1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 2)), scpexpr(EXPR_EXEC_OP, "OP_40(0x412, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B87")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44E, 7)), scpexpr(EXPR_END)), "loc_1B55")
    OP_CC(0x1, 0x1, "＃１３　阅览完毕")
    Jump("loc_1B87")

    label("loc_1B55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1B75")
    OP_CC(0x1, 0x1, "＃１３　分析完成！")
    Jump("loc_1B87")

    label("loc_1B75")

    OP_CC(0x1, 0x1, "＃１３　分析中")

    label("loc_1B87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 3)), scpexpr(EXPR_EXEC_OP, "OP_40(0x413, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BF4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44F, 0)), scpexpr(EXPR_END)), "loc_1BC2")
    OP_CC(0x1, 0x1, "＃１４　阅览完毕")
    Jump("loc_1BF4")

    label("loc_1BC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1BE2")
    OP_CC(0x1, 0x1, "＃１４　分析完成！")
    Jump("loc_1BF4")

    label("loc_1BE2")

    OP_CC(0x1, 0x1, "＃１４　分析中")

    label("loc_1BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C6, 4)), scpexpr(EXPR_EXEC_OP, "OP_40(0x414, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C61")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x44F, 1)), scpexpr(EXPR_END)), "loc_1C2F")
    OP_CC(0x1, 0x1, "＃１５　阅览完毕")
    Jump("loc_1C61")

    label("loc_1C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_1C4F")
    OP_CC(0x1, 0x1, "＃１５　分析完成！")
    Jump("loc_1C61")

    label("loc_1C4F")

    OP_CC(0x1, 0x1, "＃１５　分析中")

    label("loc_1C61")

    OP_CC(0x2, 0x1)
    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C81")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1CEB")

    label("loc_1C81")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C8B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CEB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA4")
    Jump("loc_1CEB")

    label("loc_1CA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CDE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1CD1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1CDE")

    label("loc_1CD1")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1CA4")

    label("loc_1CDE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1C8B")

    label("loc_1CEB")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1D34"),
        (1, "loc_211B"),
        (2, "loc_23CE"),
        (3, "loc_2685"),
        (4, "loc_2A1E"),
        (5, "loc_2D75"),
        (6, "loc_3099"),
        (7, "loc_3342"),
        (8, "loc_3639"),
        (9, "loc_3930"),
        (10, "loc_3C8D"),
        (11, "loc_4083"),
        (12, "loc_4492"),
        (13, "loc_46BD"),
        (14, "loc_492C"),
        (15, "loc_4BA9"),
        (SWITCH_DEFAULT, "loc_4EF6"),
    )


    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_1F2A")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #16
        (
            "\x07\x02#1S『关于封印机构（１／４）』\x01",
            "　\x01",
            "──我的名字是\x01",
            "赛雷斯托·Ｄ·奥赛雷丝。\x01",
            "是『封印机构』的设立者，\x01",
            "『封印计划』的实行负责人。\x01",
            "　\x01",
            "因塔的『第二结界』发动\x01",
            "而被封印在异次元之中的『环』\x01",
            "在后世将会苏醒，\x01",
            "为此我们决定留下一部分信息。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #17
        (
            "\x07\x02#1S读到这些信息的人，\x01",
            "如果打算阻止『环』的复活的话，\x01",
            "请以此作参考，那将是一大幸事。\x01",
            "但如果你是期盼『环』复活的人，\x01",
            "我请求你重新考虑一下。\x01",
            "　\x01",
            "『环』的力量过于强大，\x01",
            "并非人类所能操控的存在。\x01",
            "当人们接纳了『环』之时，\x01",
            "也许就是我们造访炼狱之日。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2280)
    Jump("loc_2117")

    label("loc_1F2A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #18
        (
            "\x07\x02#1S『关于封印机构（１／４）』\x01",
            "　\x01",
            "──我的名字是\x01",
            "赛雷斯托·Ｄ·奥赛雷丝。\x01",
            "是『封■■■』■设立■■\x01",
            "■封■计■■■■■负责人。\x01",
            "丂\x01",
            "■塔■■■二结■■发■\x01",
            "而■封■■异次■■■■■环』\x01",
            "■■世■会苏■■\x01",
            "■■■■■定留■■部分信■■\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #19
        (
            "\x07\x02#1S读■这■■息的■，\x01",
            "■■■■■■『环■■复活的■■\x01",
            "■以此作■■，那将是■大幸■。\x01",
            "■■■你是期■■环』■■的■，\x01",
            "我请求■■新考虑■■■■■。\x01",
            "　\x01",
            "『■』■力量■■强大■\x01",
            "■■人类■能■■的■在。\x01",
            "当人■接■了『环■之■■\x01",
            "也■是■们造■■狱■日。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2117")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_211B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2279")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #20
        (
            "\x07\x02#1S『关于封印机构（２／４）』\x01",
            "　\x01",
            "本机构，是为了通过消除『环』\x01",
            "的干涉，从而保护人类的存在\x01",
            "而设立的。\x01",
            "　\x01",
            "在此想事先提醒大家的是，\x01",
            "『环』本身并不具备\x01",
            "支配人类的意志。\x01",
            "一切都起因于我们对\x01",
            "『环』的过分依赖以及自身的软弱。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #21
        (
            "\x07\x02#1S这伟大的至宝对于不成熟的灵魂\x01",
            "而言，力量实在过于强大了。\x01",
            "因此，女神的慈悲和全能\x01",
            "丝毫也不会动摇。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2281)
    Jump("loc_23CA")

    label("loc_2279")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        (
            "\x07\x02#1S『关于封印机构（２／４）』\x01",
            "　\x01",
            "本■■，是■了■■■除『■』\x01",
            "的干■，■而■■人■的存■\x01",
            "■■立的。\x01",
            "　\x01",
            "在此想■■■■大■的是，\x01",
            "『环』■身■■具■\x01",
            "■配■■的■志。\x01",
            "一■■起■■■们对\x01",
            "『■■的过■■赖■及自■■■弱。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #23
        (
            "\x07\x02#1S■■大的至宝■■■■■■■■\x01",
            "而■■■量实■■■■大了。\x01",
            "因此■■神的慈■■全能\x01",
            "丝■■■■■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CA")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_23CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_252F")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #24
        (
            "\x07\x02#1S『关于封印机构（３／４）』\x01",
            "　\x01",
            "封印机构的目的，\x01",
            "完全脱离了所谓\x01",
            "民主主义的理念。\x01",
            "　\x01",
            "即使在我们之中，也存在着不少\x01",
            "认为应当有效地利用拥有\x01",
            "无限力量的『环』的意见。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #25
        (
            "\x07\x02#1S但是，当『环』拥有自主性后，\x01",
            "它将会凭借着其势不可挡的力量\x01",
            "给社会和市民生活带来惊人的变化。\x01",
            "不仅不可思议地带来物质上的充足，\x01",
            "甚至还囊括了精神层面的丰富。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2282)
    Jump("loc_2681")

    label("loc_252F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #26
        (
            "\x07\x02#1S『关于封印机构（３／４）』\x01",
            "　\x01",
            "■印■■■■的，\x01",
            "完■■离了■谓\x01",
            "民■■义的■■。\x01",
            "丂\x01",
            "■使在我■■中，■存在着■■\x01",
            "认为■当有效■■■■有\x01",
            "无■■量■■』■意见。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #27
        (
            "\x07\x02#1S■是，■■■』拥■■■■后，\x01",
            "■■会凭■■■势不■■■■量\x01",
            "给社会■■■生活带■■■■■■■\x01",
            "■■不可思议■■来物质■■■■，\x01",
            "■■■■括■精■■面的■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2681")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_2685")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_2856")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #28
        (
            "\x07\x02#1S『关于封印机构（４／４）』\x01",
            "　\x01",
            "例如『环』通过『福音』向市民\x01",
            "展示了带来幸福感的虚拟现实，\x01",
            "有时甚至完全控制了脑内物质。\x01",
            "　\x01",
            "这就跟随时随地在吸食强力无比的\x01",
            "毒品或迷幻药别无二致。\x01",
            "更糟糕的是，这种药品在\x01",
            "生理方面完全没有副作用。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #29
        (
            "\x07\x02#1S这样的恩惠将给人类的存在\x01",
            "带来多么深刻的影响啊……\x01",
            "　\x01",
            "这种影响已经在很多市民的身上体现出来，\x01",
            "留给我们的时间太少了。\x01",
            "因此，我们在克服了意见的对立，\x01",
            "并对将来的各种困难抱持觉悟后，\x01",
            "着手实施了『封印计划』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2283)
    Jump("loc_2A1A")

    label("loc_2856")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #30
        (
            "\x07\x02#1S『关于封印机构（４／４）』\x01",
            "　\x01",
            "■■『环』■■■■音』向市■\x01",
            "展■■带来■■感■虚■■实，\x01",
            "■■■至■■控制■■内■质。\x01",
            "　\x01",
            "这就■■■随地■■■■力无■■\x01",
            "毒■■迷■■■■■致■\x01",
            "■■■的■■这■■品■\x01",
            "■理■面■■■有■■用。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x02#1S这样的■■将给人■■■在\x01",
            "带来■么■■的■■■……\x01",
            "　\x01",
            "这种■■已经在■多市民■■■■现出■，\x01",
            "■■■■的时间太■■。\x01",
            "因此，我■■■服了意见■■■■\x01",
            "并■将来的各■■■抱■■悟■，\x01",
            "■手■■了■■■■■』。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A1A")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_2A1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_2BCD")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #32
        (
            "\x07\x02#1S『关于湖岸的地下设施（１／４）』\x01",
            "　\x01",
            "要使『封印机构』建立成形，\x01",
            "庞大的能量以及\x01",
            "大规模的设施都是不可或缺的。\x01",
            "作为能量的来源，我们首先\x01",
            "研究尝试了对『环』本身的利用。\x01",
            "　\x01",
            "『环』会对人的愿望产生反应，\x01",
            "进而给予恩惠－－也就是说，\x01",
            "我们当时猜想可否藉由此方式\x01",
            "从『环』之中提取必须的能量。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #33
        (
            "\x07\x02#1S……但是这种想法没能行得通。\x01",
            "『环』在拥有了自主性之后不久，\x01",
            "那种恩惠就与人的愿望脱离关系，\x01",
            "成为了单方面的给予。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2284)
    Jump("loc_2D71")

    label("loc_2BCD")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #34
        (
            "\x07\x02#1S『关于湖岸的地下设施（１／４）』\x01",
            "　\x01",
            "要使『■印■■』建■■形，\x01",
            "■大的■■■■\x01",
            "■规模■■施都■不可■■■。\x01",
            "作为■■的■■，我■■先\x01",
            "研究■■■对『■■■■的利用。\x01",
            "丂\x01",
            "■■』会对人的愿望■■■■■\x01",
            "■■■予■■－－也就是■■\x01",
            "我■当时■■■否■■■■方式\x01",
            "从『环』■中■■■须■■量。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #35
        (
            "\x07\x02#1S……■■■种■■没能■得■。\x01",
            "■■』在拥有了■主性■■■久，\x01",
            "那种■■就与人的■■■■关系，\x01",
            "■为了■方■的■予■\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D71")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_2D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_2F0B")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #36
        (
            "\x07\x02#1S『关于湖岸地下设施（２／４）』\x01",
            "　\x01",
            "－－利用『环』的力量的构想无法实现。\x01",
            "我们便将目光转向都市之外，\x01",
            "找到了深深沉眠在大地中的七耀脉能源之后，\x01",
            "我们试图在那里建造设施。\x01",
            "　\x01",
            "但是，我们当时已经完全\x01",
            "置身于『环』的监视之下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #37
        (
            "\x07\x02#1S『环』的思考模式\x01",
            "似乎是把城市的存续放在第一位\x01",
            "而排除所有可能对此造成威胁的因素。\x01",
            "　\x01",
            "因此为了欺骗『环』，我们就在\x01",
            "观测七耀脉的名义下进行设施的建造。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2285)
    Jump("loc_3095")

    label("loc_2F0B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #38
        (
            "\x07\x02#1S『关于湖岸的地下设施（２／４）』\x01",
            "　\x01",
            "■■■■环■的力量■■■■法实现。\x01",
            "#1S■们■■■光转■■市■■■\x01",
            "找到■■深沉眠■■■中的七耀脉■■■■■\x01",
            "■们■■在■里■造■■。\x01",
            "　\x01",
            "■是，我们当■■经完■\x01",
            "置■于『■』的监■■下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #39
        (
            "\x07\x02#1S■环』的■■■■\x01",
            "似乎是■■■的存续放■第■位\x01",
            "而排■■■■能对此■成■胁的■■■\x01",
            "　\x01",
            "■■为了■■『■』，我们就■\x01",
            "观测七■■的名义下■■施的■造。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3095")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_3099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_31F0")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #40
        (
            "\x07\x02#1S『关于湖岸的地下设施（３／４）』\x01",
            "　\x01",
            "设施被建在瓦雷利亚湖东岸\x01",
            "地下５００亚矩的位置。\x01",
            "根据调查显示，\x01",
            "那里是七耀脉高密度集中的地方。\x01",
            "　\x01",
            "都市底下的辽阔大地，\x01",
            "被郁郁葱葱的原生林笼罩着。\x01",
            "其间完全无人涉足，\x01",
            "没有任何事物对工程造成阻碍。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #41
        (
            "\x07\x02#1S我们一边逃避『环』的监视，\x01",
            "一边集结所有技术力量\x01",
            "火速进行地下设施的建设。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2286)
    Jump("loc_333E")

    label("loc_31F0")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #42
        (
            "\x07\x02#1S『关于湖岸的地下设施（３／４）』\x01",
            "　\x01",
            "设施■■■■雷利亚■东■\x01",
            "地下５■０■■的位■■\x01",
            "#1S■调查■■■\x01",
            "那里是七■脉■■■■中■地方。\x01",
            "　\x01",
            "都市■■的■■■地，\x01",
            "被郁郁■葱■原生■■■着。\x01",
            "#1S■完全■■■足，\x01",
            "没有任■事物对工程■■■■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #43
        (
            "\x07\x02#1S■■一边逃避『■』■监视，\x01",
            "一■■结所有■■■量，\x01",
            "火■■行地■■施的■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333E")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_3342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 0)), scpexpr(EXPR_END)), "loc_34C2")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #44
        (
            "\x07\x02#1S『关于湖岸的地下设施（４／４）』\x01",
            "　\x01",
            "在进行地下设施建造的期间，\x01",
            "我们在『环』未察觉的情况下，\x01",
            "于地面的周边部分\x01",
            "建起了两种巨大的建筑物。\x01",
            "　\x01",
            "一种是内壁一致朝向\x01",
            "『环』的方向的长城『亚宁堡』。\x01",
            "而另一种则是包围着『环』，\x01",
            "矗立于地面的四座『设备塔』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #45
        (
            "\x07\x02#1S这两种建筑物在计划中\x01",
            "分别有着各自重要的任务，\x01",
            "它们和地下设施一样，\x01",
            "都是『封印机构』不可或缺的存在。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2287)
    Jump("loc_3635")

    label("loc_34C2")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #46
        (
            "\x07\x02#1S『关于湖岸的地下设施（４／４）』\x01",
            "　\x01",
            "在进行■■■■建■■期间，\x01",
            "■们在『环■■■■的情况■，\x01",
            "于■■的周■■分\x01",
            "建起了■■巨大■■■物。\x01",
            "　\x01",
            "■■■■壁■■朝向\x01",
            "『■』的方■■■城■■■堡』。\x01",
            "而另■■则■■围■■环』，\x01",
            "■立于■■的四■■■■塔』。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #47
        (
            "\x07\x02#1S这两■建■■在计■■\x01",
            "分■有着■■■要■任务，\x01",
            "它们和■下■■一■■\x01",
            "都■『封印■■』■■■缺的■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3635")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_3639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_37B9")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #48
        (
            "\x07\x02#1S关于『环』的封印（１／４）\x01",
            "　\x01",
            "当地下设施的建造即将完成的时候，\x01",
            "在不知不觉中，我们被\x01",
            "『环』得知了『封印计划』的存在。\x01",
            "　\x01",
            "原因是我们其中一名同胞禁不住\x01",
            "『环』的诱惑而被其介入精神之中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #49
        (
            "\x07\x02#1S不过，那名同胞没有处于\x01",
            "能够得知计划全貌的立场上，\x01",
            "这实在是不幸中的万幸。\x01",
            "　\x01",
            "『环』并没有将目光放在\x01",
            "长城『亚宁堡』和『设备塔』上，\x01",
            "而是只掌握到了湖畔的地下设施。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2288)
    Jump("loc_392C")

    label("loc_37B9")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #50
        (
            "\x07\x02#1S关于『环』的封印（１／４）\x01",
            "　\x01",
            "当地■■■■建■■将■■■■候，\x01",
            "在■知不■中■■们被\x01",
            "『■■■知了『■■■■』■存在。\x01",
            "丂\x01",
            "■因是■们其■■名同■■■住\x01",
            "『■』的诱■而被■■■精■■中。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #51
        (
            "\x07\x02#1S不过■■■■胞没有■于\x01",
            "能■■■计划全■■■场■■\x01",
            "■■■是不幸■■■■。\x01",
            "丂\x01",
            "『■』并■■■■■放在\x01",
            "长城■■■■■和『设■■■上，\x01",
            "■是只■■■了湖■的■■■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_392C")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_3930")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_3AE3")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #52
        (
            "\x07\x02#1S『关于‘环’的封印（２／４）』\x01",
            "　\x01",
            "得知我们计划的『环』\x01",
            "所采取的手段是强制性的。\x01",
            "　\x01",
            "『环』诞生出了几台\x01",
            "被称为『幻想乐曲』\x01",
            "的自身守护者，\x01",
            "并向来到设施中的我们袭来\x01",
            "　\x01",
            "──不过，幸运的是\x01",
            "我们的设施建造于地下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #53
        (
            "\x07\x02#1S地上与设施之间\x01",
            "相连的路径只有一条。\x01",
            "『幻想乐曲』的攻击\x01",
            "无法直接到达\x01",
            "地下５００亚矩的深处。\x01",
            "　\x01",
            "但是，『幻想乐曲』的攻击\x01",
            "却日夜不停地持续进行着。\x01",
            "过了不久之后，\x01",
            "我们坚固的防线也逼近了极限。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2289)
    Jump("loc_3C89")

    label("loc_3AE3")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #54
        (
            "\x07\x02#1S『关于‘环’的封印（２／４）』\x01",
            "　\x01",
            "得知■■■划的■环■\x01",
            "■采■■手段■强制■■■\x01",
            "丂\x01",
            "『■』诞生出■■■\x01",
            "被称为『■想■■』\x01",
            "的自■■护者，\x01",
            "并■来到■■中的我们■■\x01",
            "　\x01",
            "──不■，■■的■\x01",
            "■■的设■建造■■下。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #55
        (
            "\x07\x02#1S地■■■施之■\x01",
            "相连■■■只■一■。\x01",
            "■■想乐■』的攻■\x01",
            "无法■■■■\x01",
            "■■５００■■■■■。\x01",
            "　\x01",
            "■■，■■■乐■』的攻■\x01",
            "却日■不■■持续■■■。\x01",
            "过■■久之■，\x01",
            "■们坚固■■■■逼近■■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C89")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_3C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_3E8B")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #56
        (
            "\x07\x02#1S『关于‘环’的封印（３／４）』\x01",
            "　\x01",
            "在承受『幻想乐曲』的攻击期间，\x01",
            "设施的建造终于完成了，\x01",
            "然而我们还需要一些时间\x01",
            "确保从七耀脉中得到计划所需的能量。\x01",
            "　\x01",
            "但是，或许是设施的完工\x01",
            "让我们松懈下来了──\x01",
            "我们不小心让一架『幻想乐曲』\x01",
            "进入了设施的内部。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #57
        (
            "\x07\x02#1S一旦让它进入内部之后，\x01",
            "要阻止它的攻击就十分困难了。\x01",
            "『幻想乐曲』一转眼\x01",
            "便抵达了设施的最深处。\x01",
            "　\x01",
            "──真是千钧一发啊。\x01",
            "来到最深处的『幻想乐曲』\x01",
            "正要展开破坏活动时，\x01",
            "计划所需的能量终于收集完毕了，\x01",
            "于是我们马上启动了『第一结界』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x228A)
    Jump("loc_407F")

    label("loc_3E8B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #58
        (
            "\x07\x02#1S『关于‘环’的封印（３／４）』\x01",
            "　\x01",
            "在■■■幻想乐■■的攻■■间，\x01",
            "设■的■■■于■成了，\x01",
            "然■我们■■■一■时■\x01",
            "■■从■■脉中■■计■■■的能■■\x01",
            "　\x01",
            "但是，■■■设施的■■\x01",
            "让我■松■■来■──\x01",
            "■■不小■■■架■幻■■曲』\x01",
            "■入了■■的内部。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #59
        (
            "\x07\x02#1S■旦让■进入■■■■，\x01",
            "要阻止■■■■就十分■■■■\x01",
            "■■想■■■■■眼\x01",
            "■■■了■■■■■处。\x01",
            "　\x01",
            "■─真是■■一■啊。\x01",
            "#1S来到■■■■『■■■曲』\x01",
            "正要展■■坏■■时，\x01",
            "■■所需的■■终于■■■■■，\x01",
            "于是我们■上启■■■第■结■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_407F")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_4083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 6)), scpexpr(EXPR_END)), "loc_428F")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #60
        (
            "\x07\x02#1S『关于‘环’的封印（４／４）』\x01",
            "　\x01",
            "设施所释放出的光芒，\x01",
            "经过长城『亚宁堡』的内壁增幅后，\x01",
            "顺利地捕捉到了漂浮在空中的『环』。\x01",
            "　\x01",
            "于是，『环』\x01",
            "便从我们眼前消失了，\x01",
            "『幻想乐曲』也停止了运转。\x01",
            "就这样，我们确认\x01",
            "『第一结界』顺利地发动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #61
        (
            "\x07\x02#1S『环』是『七至宝』中\x01",
            "掌管空间的至宝。\x01",
            "为了让拥有对空间的绝对支配力量的『环』\x01",
            "失去效力，所必须做的事情就是──\x01",
            "断绝掉『环』对空间\x01",
            "乃至对时间的一切干涉。\x01",
            "　\x01",
            "我们费尽心血所建立起的『封印机构』\x01",
            "将『环』连同都市一起送进了异次元，\x01",
            "成功地实现了『时间冻结』。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x228B)
    Jump("loc_448E")

    label("loc_428F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #62
        (
            "\x07\x02#1S『关于‘环’的封印（４／４）』\x01",
            "　\x01",
            "设施■■■■的光■■\x01",
            "■过长城『■■■』■■■■■后，\x01",
            "■■■■■到了■■在空中■■■』。\x01",
            "　\x01",
            "■是，■环■\x01",
            "■从我们■■消■■，\x01",
            "『■■■曲』■■■了运■。\x01",
            "■这样■■■确认\x01",
            "『■■■■』顺利■■■了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #63
        (
            "\x07\x02#1S■环■是■■至宝■中\x01",
            "■■空间的■■。\x01",
            "■了让拥■■空■■■■■■力量的■■』\x01",
            "失去■■■所■■■的事情■■──\x01",
            "■绝掉■■■对空间\x01",
            "■至对时间的■■■■。\x01",
            "　\x01",
            "我们费■■血■■■起的■■印■■』\x01",
            "将■■■连同都■■■■进了■■元，\x01",
            "成功地■■■■时■■结■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_448E")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_4492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_45AC")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #64
        (
            "\x07\x02#1S『关于设备塔（１／４）』\x01",
            "　\x01",
            "『第一结界』顺利发动，\x01",
            "我们将『环』封进异次元，\x01",
            "成功地实现了『时间冻结』。\x01",
            "　\x01",
            "但是，正如名称所示\x01",
            "『封印计划』中的结界\x01",
            "并非只有这一道。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #65
        (
            "\x07\x02#1S『封印计划』最后的防线是『第二结界』。\x01",
            "　\x01",
            "──其关键是由\x01",
            "四座设备塔所掌握的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2276)
    Jump("loc_46B9")

    label("loc_45AC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        (
            "\x07\x02#1S『关于设备塔（１／４）』\x01",
            "　\x01",
            "■第一■界』■利■■，\x01",
            "我们■『环■■进■■元，\x01",
            "成■■实现■■时间■■■。\x01",
            "　\x01",
            "但■，正如■■■示\x01",
            "『■■计划』■■■■\x01",
            "■非■■■一■。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #67
        (
            "\x07\x02#1S■封印计■』最后的■■■『■二■界■。\x01",
            "　\x01",
            "──■■■■■\x01",
            "■■■■塔■■握的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46B9")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_46BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_4801")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #68
        "\x07\x02#1S『关于设备塔（２／４）』\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #69
        (
            "\x07\x02#1S这个机构在『第一结界』被解除\x01",
            "『环』的时间再次开始流动之时，\x01",
            "便会自行发动。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #70
        (
            "\x07\x02#1S『第二结界』\x01",
            "又名『重力结界』，\x01",
            "拥有在异次元中\x01",
            "产生重力的机能。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #71
        (
            "\x07\x02#1S其目的是当『环』开始活动的时候，\x01",
            "利用重力之楔将它维系在异次元之中，\x01",
            "藉此防止『环』重新出现于世上。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2277)
    Jump("loc_4928")

    label("loc_4801")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #72
        (
            "\x07\x02#1S『关于设备塔（２／４）』\x01",
            "　\x01",
            "■■机■在『■■■■』被解除\x01",
            "■环■的时间■■开始■■之时\x01",
            "■会■■■动。\x01",
            "　\x01",
            "『■二■界』\x01",
            "■■『重力结■』，\x01",
            "拥有在■次■中\x01",
            "■■■■的机能。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #73
        (
            "\x07\x02#1S其■■是当『环』■■活动■■■■\x01",
            "利用■■■楔将■维系■■■元■■，\x01",
            "■此■■『■』重新■■于■上。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4928")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_492C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_4A71")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #74
        (
            "\x07\x02#1S『关于设备塔（３／４）』\x01",
            "　\x01",
            "当『第二结界』发动时，\x01",
            "『环』已经开始了运转。\x01",
            "　\x01",
            "如果使用那个名为『福音』的终端，\x01",
            "便可以随心所欲地提取它的力量。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #75
        (
            "\x07\x02#1S残留在『利贝尔·方舟』中的\x01",
            "『福音』\x01",
            "与『环』一样是被封印起来的。\x01",
            "　\x01",
            "但是，如果后世出现了\x01",
            "可以代替『福音』的东西，\x01",
            "『环』的力量便会波及到世间。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2278)
    Jump("loc_4BA5")

    label("loc_4A71")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #76
        (
            "\x07\x02#1S『关于数据塔（３／４）』\x01",
            "　\x01",
            "当『第二结界■发■■，\x01",
            "『■』已经■■■■转。\x01",
            "　\x01",
            "如果使用那个■为■■■■的■■，\x01",
            "■■■随■所欲地■■■的■量。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #77
        (
            "\x07\x02#1S■留在■贝■·■舟■■\x01",
            "■■音』\x01",
            "■■■』一样是■■■■来■■\x01",
            "　\x01",
            "但是，如果■■■现了\x01",
            "■■代■■■■』的东西，\x01",
            "■环■的力量便会■■到■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BA5")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_4BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_END)), "loc_4D53")
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #78
        (
            "\x07\x02#1S『关于设备塔（４／４）』\x01",
            "　\x01",
            "虽然我们成功地封印了『环』，\x01",
            "但并没能使它的力量消失。\x01",
            "　\x01",
            "我们打算扎根于此地，\x01",
            "世世代代一直看守着『环』。\x01",
            "并且祈祷这些记录\x01",
            "不被任何人看到。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #79
        (
            "\x07\x02#1S然而与此同时\x01",
            "我们也预见，这是不可能的事。\x01",
            "　\x01",
            "『环』再次出现在世间的时候，\x01",
            "生活于后世里的人们\x01",
            "将做出怎样的选择呢──\x01",
            "　\x01",
            "我们相信人类将不会再次犯错，\x01",
            "相信终有从『环』中解放出来的一天\x01",
            "因此，我们决定将这些记录托付给后世。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2279)
    Jump("loc_4EF2")

    label("loc_4D53")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #80
        (
            "\x07\x02#1S『关于设备塔（４／４）』\x01",
            "　\x01",
            "■■■■成功地封■了『■』，\x01",
            "但■没■■■的力■■失。\x01",
            "　\x01",
            "我■打算■■■此地，\x01",
            "■■■代一直■■着『■』。\x01",
            "并且祈祷■■■■\x01",
            "不被■■人看到。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #81
        (
            "\x07\x02#1S■■■此同时\x01",
            "我们也■见，这是■■能的事。\x01",
            "　\x01",
            "『环■再次出■在世间■■■，\x01",
            "生活于■世里的■■\x01",
            "将做出■■■选择■－－\x01",
            "　\x01",
            "我们相信人类■不会■次■错，\x01",
            "■■终有从■环■中■■■■的一天。\x01",
            "■■，我们决定■这些■■■■给■■。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EF2")

    CloseMessageWindow()
    Jump("loc_4F03")

    label("loc_4EF6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F03")

    label("loc_4F03")

    Jump("loc_1585")

    label("loc_4F06")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_XOR_SAVE), scpexpr(EXPR_END)))
    OP_5F(0x1)
    Jump("loc_4F23")

    label("loc_4F16")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F23")

    label("loc_4F23")

    Jump("loc_1A5")

    label("loc_4F26")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    EventEnd(0x1)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
