from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4143   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4143.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '戴尔蒙',                               # 9
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


    AddCharChip(
        'ED6_DT07/CH02410 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH02410P._CP',             # 00
    )

    DeclNpc(
        X                   = -270,
        Z                   = 0,
        Y                   = 2120,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -440,
        TriggerZ            = 0,
        TriggerY            = 680,
        TriggerRange        = 400,
        ActorX              = -270,
        ActorZ              = 1500,
        ActorY              = 2120,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_11A",          # 01, 1
        "Function_2_11B",          # 02, 2
        "Function_3_120",          # 03, 3
        "Function_4_5EB",          # 04, 4
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41D, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_119")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_119")

    Return()

    # Function_0_F6 end

    def Function_1_11A(): pass

    label("Function_1_11A")

    Return()

    # Function_1_11A end

    def Function_2_11B(): pass

    label("Function_2_11B")

    Call(0, 3)
    Return()

    # Function_2_11B end

    def Function_3_120(): pass

    label("Function_3_120")

    TalkBegin(0x8)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "对话\x01",        # 0
            "买东西\x01",      # 1
            "离开\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F4")
    FadeToBright(300, 0)

    ChrTalk(    #0
        0x8,
        (
            "#660F有钱能使鬼推磨……\x01",
            "欢迎来到戴尔蒙商会。\x02\x03",

            "呵呵……想要耀晶片的话，\x01",
            "随时都可以来找我。\x02\x03",

            "不过，该给的钱\x01",
            "还是要给的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DE")

    label("loc_1F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5C4")

    label("loc_201")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B2")

    AnonymousTalk(    #1
        "\x18\x07\x05购买哪种耀晶片？\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        150,
        90,
        1,
        (
            "地之耀晶片　１００个　３０００米拉\x01",      # 0
            "水之耀晶片　１００个　３０００米拉\x01",      # 1
            "火之耀晶片　１００个　３０００米拉\x01",      # 2
            "风之耀晶片　１００个　３０００米拉\x01",      # 3
            "时之耀晶片　１００个　３０００米拉\x01",      # 4
            "空之耀晶片　１００个　９０００米拉\x01",      # 5
            "幻之耀晶片　１００个　６０００米拉\x01",      # 6
            "退出\x01",                                    # 7
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_364"),
        (1, "loc_3B6"),
        (2, "loc_408"),
        (3, "loc_45A"),
        (4, "loc_4AC"),
        (5, "loc_4FE"),
        (6, "loc_550"),
        (SWITCH_DEFAULT, "loc_5A2"),
    )


    label("loc_364")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_382")

    AnonymousTalk(    #2
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_3B0")

    label("loc_382")

    SubMira(3000)
    AddSepith(0x0, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #3
        "\x07\x05#56I 得到１００个地之耀晶片。\x02",
    )


    label("loc_3B0")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_3B6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3D4")

    AnonymousTalk(    #4
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_402")

    label("loc_3D4")

    SubMira(3000)
    AddSepith(0x1, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #5
        "\x07\x05#57I 得到１００个水之耀晶片。\x02",
    )


    label("loc_402")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_408")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_426")

    AnonymousTalk(    #6
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_454")

    label("loc_426")

    SubMira(3000)
    AddSepith(0x2, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #7
        "\x07\x05#58I 得到１００个火之耀晶片。\x02",
    )


    label("loc_454")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_45A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_478")

    AnonymousTalk(    #8
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_4A6")

    label("loc_478")

    SubMira(3000)
    AddSepith(0x3, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #9
        "\x07\x05#59I 得到１００个风之耀晶片。\x02",
    )


    label("loc_4A6")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_4AC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4CA")

    AnonymousTalk(    #10
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_4F8")

    label("loc_4CA")

    SubMira(3000)
    AddSepith(0x4, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x05#62I 得到１００个时之耀晶片。\x02",
    )


    label("loc_4F8")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_4FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_51C")

    AnonymousTalk(    #12
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_54A")

    label("loc_51C")

    SubMira(9000)
    AddSepith(0x5, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #13
        "\x07\x05#60I 得到１００个空之耀晶片。\x02",
    )


    label("loc_54A")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_550")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_56E")

    AnonymousTalk(    #14
        "\x07\x05钱不够了。\x02",
    )

    Jump("loc_59C")

    label("loc_56E")

    SubMira(6000)
    AddSepith(0x6, 0x64)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #15
        "\x07\x05#61I 得到１００个幻之耀晶片。\x02",
    )


    label("loc_59C")

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_5AF")

    label("loc_5A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5AF")

    label("loc_5AF")

    Jump("loc_201")

    label("loc_5B2")

    FadeToBright(300, 0)
    OP_56(0x0)
    TalkEnd(0x8)
    Return()

    label("loc_5C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5DE")
    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    label("loc_5DE")

    FadeToBright(300, 0)
    TalkEnd(0x8)
    Return()

    # Function_3_120 end

    def Function_4_5EB(): pass

    label("Function_4_5EB")

    EventBegin(0x0)
    OP_6D(1170, -250, -1690, 0)
    OP_67(0, 5380, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, -570, -250, -2430, 0)
    SetChrPos(0x102, 470, -250, -2600, 0)
    SetChrPos(0xF8, -570, -250, -3710, 0)
    SetChrPos(0xF9, 520, -250, -3790, 0)
    OP_4A(0x8, 255)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #16
        0x101,
        (
            "#1015F#6P咦，这种地方\x01",
            "居然有店？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #17
        0x8,
        "店员",
        "欢迎光临……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x8, 0, 600)
    Sleep(500)

    def lambda_6EC():
        OP_8E(0xFE, 0xFFFFFC54, 0x0, 0xF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EC)
    Sleep(50)

    def lambda_70C():
        OP_8E(0xFE, 0xDC, 0x0, 0xFA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70C)
    Sleep(80)

    def lambda_72C():
        OP_8E(0xFE, 0xFFFFFC40, 0x0, 0xFFFFFBA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_72C)
    Sleep(70)

    def lambda_74C():
        OP_8E(0xFE, 0xFA, 0x0, 0xFFFFFBC8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_74C)
    Sleep(50)

    def lambda_76C():
        OP_6D(530, 0, 1970, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_76C)

    def lambda_784():
        OP_67(0, 4900, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_784)

    def lambda_79C():
        OP_6B(2830, 2000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_79C)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    WaitChrThread(0x102, 0x3)
    Sleep(300)

    ChrTalk(    #18
        0x101,
        "#1000F#6P售货员，这里是什么店？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    NpcTalk(    #19
        0x8,
        "店员",
        "#5P…………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1000F请问────\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x102,
        (
            "#1042F……没想到会在\x01",
            "这种地方碰到你。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #22
        0x101,
        "#1004F咦，是约修亚的熟人吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #23
        0x102,
        (
            "#1043F#2P艾丝蒂尔，这个人\x01",
            "你也认识的哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#1005F咦咦！？\x01",
            "难不成，是结社的家伙？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x102,
        (
            "#1035F#2P不，有点不同。\x02\x03",

            "#1042F希望你能解释清楚呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)
    OP_21()

    ChrTalk(    #26
        0x102,
        "#1042F原卢安市长……戴尔蒙先生。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#1004F你说什么！？\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #28
        0x8,
        "店员",
        "#5P没办法了……\x02",
    )

    CloseMessageWindow()
    OP_1D(0x57)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #29
        0x101,
        "#1005F为、为什么你会在这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1042F记得你应该是被\x01",
            "监禁在雷斯顿要塞的吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x8,
        (
            "#666F#5P哼，确实如此，但你可别误会。\x02\x03",

            "#664F我会在这里\x01",
            "是经过正式手续的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1009F正式的手续？\x01",
            "再没有比这更可疑的事了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "#666F#5P真、真失礼啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1005F有卢安的事在先，\x01",
            "怎么可能相信你！\x02\x03",

            "竟然让孤儿院里\x01",
            "无辜的孩子们遭到那种事！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x8,
        "#663F#5P呜……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #36
        0x102,
        (
            "#1035F艾丝蒂尔……先\x01",
            "听听他怎么说吧。\x02\x03",

            "#1042F能不能相信\x01",
            "之后再判断就是。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1009F嗯、嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 0, 400)

    ChrTalk(    #38
        0x8,
        (
            "#666F#5P那、那个事件里\x01",
            "我也是受害者啊。\x02\x03",

            "因为是在记忆混乱的时候，\x01",
            "被什么人操纵的。\x02\x03",

            "而且，我用留下的财产\x01",
            "支付了巨额的保释金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        "#1044F原来如此，是这么回事啊……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #40
        0x101,
        "#1015F保释金是什么意思？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        (
            "#1035F#2P还没正式定罪的时候，\x01",
            "只要支付一定的钱\x01",
            "就能被释放。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#1004F什么……做了那么多坏事，\x01",
            "只要有钱就会被饶恕？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #43
        0x102,
        (
            "#1042F#2P不是被饶恕啦。\x02\x03",

            "在利贝尔，确定真正犯人之前\x01",
            "不将其作为罪犯来对待是原则。\x02\x03",

            "作为定罪之前的担保\x01",
            "支付相应的米拉\x01",
            "就能保证人身自由。\x02\x03",

            "#1035F当然，其间如果逃跑\x01",
            "或者藏起来都是不能饶恕的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        "#664F#5P哼、哼，就是如此。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1019F嗯～还是\x01",
            "有点不能接受……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#1042F#2P不过，戴尔蒙氏会在这里\x01",
            "也不奇怪了。\x02\x03",

            "有可以酌情的余地\x01",
            "也不是不能理解……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)
    OP_8C(0x102, 0, 400)

    ChrTalk(    #47
        0x101,
        (
            "#1015F呼～不过……\x01",
            "你到底在这里干什么？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#662F#5P如你所见。\x02\x03",

            "为了复兴戴尔蒙家族，\x01",
            "我决定重振旗鼓。\x02\x03",

            "首先要在这里做买卖，\x01",
            "积蓄复兴所需的资金。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1019F买、买卖啊……\x02\x03",

            "#1015F对了对了，\x01",
            "这里到底是什么店？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        "#664F#5P耀晶片店。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1004F耀晶片！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        (
            "#662F#5P对啊，买卖耀晶片的店\x01",
            "在利贝尔的任何地区都没有吧。\x02\x03",

            "这个着眼点不坏吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#1044F确实………\x02\x03",

            "#1042F不过，要购入足够\x01",
            "用于交易的大量耀晶片\x01",
            "不是相当辛苦吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x8,
        (
            "#663F#5P这、这个……\x02\x03",

            "#664F我有专门的\x01",
            "秘密进货途径嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        (
            "#1019F总……觉得，还是\x01",
            "很可疑……\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    OP_21()
    OP_1D(0x1A)
    OP_A2(0x20EE)
    OP_4B(0x8, 255)
    EventEnd(0x0)
    Return()

    # Function_4_5EB end

    SaveToFile()

Try(main)
