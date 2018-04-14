from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60014",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T4111_1 ._SN',
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
        '赫穆特',                               # 9
        '诺琪',                                 # 10
        '马丁',                                 # 11
        '玛丽安',                               # 12
        '海伦娜',                               # 13
        '卡特莉娜夫人',                         # 14
        '达丽娅',                               # 15
        '莉安妮',                               # 16
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
        'ED6_DT07/CH01220 ._CH',             # 00
        'ED6_DT07/CH01230 ._CH',             # 01
        'ED6_DT07/CH01020 ._CH',             # 02
        'ED6_DT07/CH01210 ._CH',             # 03
        'ED6_DT07/CH02490 ._CH',             # 04
        'ED6_DT07/CH01180 ._CH',             # 05
        'ED6_DT07/CH01350 ._CH',             # 06
        'ED6_DT07/CH01480 ._CH',             # 07
        'ED6_DT27/CH03005 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH01220P._CP',             # 00
        'ED6_DT07/CH01230P._CP',             # 01
        'ED6_DT07/CH01020P._CP',             # 02
        'ED6_DT07/CH01210P._CP',             # 03
        'ED6_DT07/CH02490P._CP',             # 04
        'ED6_DT07/CH01180P._CP',             # 05
        'ED6_DT07/CH01350P._CP',             # 06
        'ED6_DT07/CH01480P._CP',             # 07
        'ED6_DT27/CH03005P._CP',             # 08
    )

    DeclNpc(
        X                   = 60000,
        Z                   = 0,
        Y                   = 2950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 60530,
        Z                   = 0,
        Y                   = 62340,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 115690,
        Z                   = 0,
        Y                   = 60750,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 125180,
        Z                   = 0,
        Y                   = 63830,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 114980,
        Z                   = 0,
        Y                   = -55400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -1040,
        Z                   = 0,
        Y                   = -56350,
        Direction           = 3,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 6600,
        Z                   = 0,
        Y                   = -56390,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -2470,
        Z                   = 0,
        Y                   = 61010,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )


    DeclActor(
        TriggerX            = 1520,
        TriggerZ            = 0,
        TriggerY            = 64780,
        TriggerRange        = 1000,
        ActorX              = 1520,
        ActorZ              = 2000,
        ActorY              = 64780,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 0,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_41B",          # 01, 1
        "Function_2_472",          # 02, 2
        "Function_3_496",          # 03, 3
        "Function_4_4BA",          # 04, 4
        "Function_5_7EA",          # 05, 5
        "Function_6_E5D",          # 06, 6
        "Function_7_104B",         # 07, 7
        "Function_8_11FE",         # 08, 8
        "Function_9_1446",         # 09, 9
        "Function_10_1773",        # 0A, 10
        "Function_11_19F4",        # 0B, 11
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28B")
    SetChrPos(0x8, 59640, 0, 1740, 90)
    SetChrPos(0x9, 60760, 0, 1740, 270)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0xA, 123980, 0, 1080, 90)
    SetChrPos(0xB, 126360, 0, 1830, 270)
    SetChrPos(0xC, 126360, 0, 740, 270)
    SetChrFlags(0xA, 0x10)
    OP_43(0xA, 0x0, 0x6, 0x2)
    Jump("loc_41A")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_2B7")
    SetChrPos(0x8, 59640, 0, 1740, 90)
    SetChrPos(0x9, 60760, 0, 1740, 270)
    Jump("loc_41A")

    label("loc_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_327")
    SetChrPos(0x8, 55510, 0, 62080, 270)
    SetChrPos(0xA, 115170, 0, 60900, 90)
    SetChrPos(0xB, 116170, 0, 60910, 270)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    OP_43(0xA, 0x0, 0x6, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrPos(0xD, -2640, 0, 64080, 179)
    Jump("loc_41A")

    label("loc_327")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_397")
    SetChrPos(0x8, 55510, 0, 62080, 270)
    SetChrPos(0xB, 114980, 0, -55400, 0)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    SetChrPos(0xD, -1600, 0, 64260, 90)
    SetChrPos(0xE, -2180, 0, 63520, 90)
    SetChrPos(0xF, -1460, 0, 64920, 180)
    Jump("loc_41A")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E9")
    SetChrPos(0x8, 55510, 0, 62080, 270)
    SetChrPos(0xB, 114980, 0, -55400, 0)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    SetChrPos(0xD, -2640, 0, 64080, 179)
    Jump("loc_41A")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_41A")
    SetChrFlags(0x8, 0x80)
    SetChrPos(0xB, 114980, 0, -55400, 0)
    SetChrPos(0xC, 120270, 0, 68790, 0)
    Jump("loc_41A")

    label("loc_41A")

    Return()

    # Function_0_216 end

    def Function_1_41B(): pass

    label("Function_1_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_437")
    OP_B1("t4111_y")
    Jump("loc_440")

    label("loc_437")

    OP_B1("t4111_n")

    label("loc_440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_44E")
    OP_43(0xF, 0x0, 0x6, 0x2)

    label("loc_44E")

    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x4)"), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0xC4, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_471")
    OP_65(0x0, 0x1)

    label("loc_471")

    Return()

    # Function_1_41B end

    def Function_2_472(): pass

    label("Function_2_472")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_495")
    OP_8D(0xFE, 113830, 62500, 117900, 58880, 2000)
    Jump("Function_2_472")

    label("loc_495")

    Return()

    # Function_2_472 end

    def Function_3_496(): pass

    label("Function_3_496")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B9")
    OP_8D(0xFE, -1150, 59690, -3770, 62520, 3000)
    Jump("Function_3_496")

    label("loc_4B9")

    Return()

    # Function_3_496 end

    def Function_4_4BA(): pass

    label("Function_4_4BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_4C7")
    Jump("loc_7E6")

    label("loc_4C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_4FA")

    ChrTalk(    #0
        0xFE,
        (
            "这、这局面，也实在是\x01",
            "不能钓鱼了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E6")

    label("loc_4FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_60A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1")

    ChrTalk(    #1
        0xFE,
        "怎么说呢……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "因为这次的事件，\x01",
            "我终于明白了被抛弃是什么感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "我准备与妻子一边享受钓鱼\x01",
            "一边重新开始人生。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        "虽然心情有点复杂……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_607")

    label("loc_5A1")


    ChrTalk(    #5
        0xFE,
        (
            "因为这次的事件，\x01",
            "我终于明白了被抛弃是什么感觉。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "我准备与妻子一边享受钓鱼\x01",
            "一边重新开始人生。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_607")

    Jump("loc_7E6")

    label("loc_60A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_649")

    ChrTalk(    #7
        0xFE,
        "不过我已经决定了……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "我准备……\x01",
            "放弃钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7E6")

    label("loc_649")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D4")

    ChrTalk(    #9
        0xFE,
        "特级钓师……真令人吃惊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "这不是钓公师团中的\x01",
            "最高称号吗……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "想不到我妻子\x01",
            "已经进步到如此程度了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_700")

    label("loc_6D4")


    ChrTalk(    #12
        0xFE,
        "……………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "………………呼。\x02",
    )

    CloseMessageWindow()

    label("loc_700")

    Jump("loc_7E6")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_70D")
    Jump("loc_7E6")

    label("loc_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_7E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7AB")

    ChrTalk(    #14
        0xFE,
        (
            "妻子抛开喜爱钓鱼的我\x01",
            "加入了钓公师团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "我工作离家期间，\x01",
            "她好像频繁前往湖那边……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "唉哟哟……\x01",
            "这样一来水平差距就越来越大了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_7E6")

    label("loc_7AB")


    ChrTalk(    #17
        0xFE,
        (
            "而且我还没有加入\x01",
            "钓公师团。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "这真是莫大的屈辱……\x02",
    )

    CloseMessageWindow()

    label("loc_7E6")

    TalkEnd(0xFE)
    Return()

    # Function_4_4BA end

    def Function_5_7EA(): pass

    label("Function_5_7EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x407, 3)), scpexpr(EXPR_END)), "loc_7F7")
    Jump("loc_E59")

    label("loc_7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_8FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_89F")

    ChrTalk(    #19
        0xFE,
        "你在说什么呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "这样下去的话你永远也\x01",
            "不能入团了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "就是在这种局面下才要\x01",
            "才要通过垂钓来使心情平静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "所谓钓鱼的心\x01",
            "即是明镜止水！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_8F7")

    label("loc_89F")


    ChrTalk(    #23
        0xFE,
        (
            "就是在这种局面下才要\x01",
            "才要通过垂钓来使心情平静……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "所谓钓鱼的心\x01",
            "即是明镜止水！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8F7")

    Jump("loc_E59")

    label("loc_8FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2CD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACA")

    ChrTalk(    #25
        0xFE,
        (
            "呵呵，我最近\x01",
            "买了新的钓竿。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "因为从开始钓鱼到现在\x01",
            "都用着同一根钓竿，\x01",
            "我想也该要买新的了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "那么……\x01",
            "该怎么处理旧的呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "我丈夫也只用又新\x01",
            "又高级的东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #29
        0xFE,
        "你……会钓鱼吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #30
        0x101,
        (
            "#1004F咦？　嗯，多少会点……\x02\x03",

            "#1013F（她、她是怎么知道的？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "那么，这个\x01",
            "就送给你了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #32
        "\x1F\x4E\x02\x07\x00收下了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x24E, 1)
    OP_0D()

    ChrTalk(    #33
        0x101,
        "#1008F谢、谢谢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "呵呵，拿去尽情地钓吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x166B)
    Jump("loc_E59")

    label("loc_ACA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_B51")

    ChrTalk(    #35
        0xFE,
        (
            "我准备下次休假时\x01",
            "教丈夫钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "我丈夫准备请假\x01",
            "带我去垂钓旅行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "虽然发生了不少事，\x01",
            "不过现在我……感觉挺幸福的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E59")

    label("loc_B51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_C1A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BD8")

    ChrTalk(    #38
        0xFE,
        (
            "从昨天起我丈夫\x01",
            "就开始想不开了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "就为那点事，真没出息……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "以前刚遇见他时，\x01",
            "他明明是个充满勇气的人。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_C17")

    label("loc_BD8")


    ChrTalk(    #41
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "我可能逼丈夫\x01",
            "有点过火了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C17")

    Jump("loc_E59")

    label("loc_C1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C77")

    ChrTalk(    #43
        0xFE,
        (
            "听说我获得了\x01",
            "特级钓师的称号\x01",
            "丈夫便沉默了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "呵呵，这次看来\x01",
            "很有效果。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E59")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_D8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D28")

    ChrTalk(    #45
        0xFE,
        "听我说，\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "这次我……\x01",
            "获得了『钓公师团』授予的\x01",
            "『特级钓师』称号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "现在我就和罗伊德老师\x01",
            "并驾齐驱了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "等丈夫回来之后\x01",
            "我一定要好好炫耀炫耀。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_D8B")

    label("loc_D28")


    ChrTalk(    #49
        0xFE,
        (
            "这次我……\x01",
            "获得了钓公师团授予的\x01",
            "『特级钓师』称号。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "等丈夫回来之后\x01",
            "我一定要好好炫耀炫耀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D8B")

    Jump("loc_E59")

    label("loc_D8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_E59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E28")

    ChrTalk(    #51
        0xFE,
        (
            "丈夫以前只顾工作和钓鱼，\x01",
            "对我看都不看一眼。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "所以我决定要在钓鱼\x01",
            "上胜过丈夫。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "这轻蔑家庭的罪……\x01",
            "我要他彻彻底底地偿还。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_E59")

    label("loc_E28")


    ChrTalk(    #54
        0xFE,
        (
            "最近我特喜欢送\x01",
            "丈夫出门。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        "哦呵呵呵呵！\x02",
    )

    CloseMessageWindow()

    label("loc_E59")

    TalkEnd(0xFE)
    Return()

    # Function_5_7EA end

    def Function_6_E5D(): pass

    label("Function_6_E5D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_EA5")

    ChrTalk(    #56
        0xFE,
        (
            "嗯～那么接下来\x01",
            "开始我家的避难训练！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "首先是点名！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_EA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_F13")

    ChrTalk(    #58
        0xFE,
        "哈哈哈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "果然我们这边的人\x01",
            "没有我管着不行。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "好～努力工作来攒出\x01",
            "全体人员的旅行费用～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_F80")

    ChrTalk(    #61
        0xFE,
        "呼，亚尔摩温泉啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        (
            "家庭旅行……这可是有板有眼的\x01",
            "节日呢……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "是不是该做个记号呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_F80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FDF")

    ChrTalk(    #64
        0xFE,
        "呼，饱餐一顿虽然能够提神……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "不过，还是喜好这类……\x01",
            "有竞争性的活动啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_FDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1009")

    ChrTalk(    #66
        0xFE,
        "哟，好像有股很香的味道……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1047")

    label("loc_1009")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1047")

    ChrTalk(    #67
        0xFE,
        "呼，真和平……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "和平真无聊……\x01",
            "也没心情工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1047")

    TalkEnd(0xFE)
    Return()

    # Function_6_E5D end

    def Function_7_104B(): pass

    label("Function_7_104B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_107D")

    ChrTalk(    #69
        0xFE,
        (
            "呵呵，在这种时候\x01",
            "感觉他真可靠。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_10AB")

    ChrTalk(    #70
        0xFE,
        "呵呵，他看来有精神了，太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_10AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_10F5")

    ChrTalk(    #71
        0xFE,
        (
            "拜托，带我去\x01",
            "亚尔摩温泉吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        (
            "当然旅游全部\x01",
            "由你来策划。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_10F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1167")

    ChrTalk(    #73
        0xFE,
        (
            "就算给他做好吃的，\x01",
            "也只能让他精神一小会儿，\x01",
            "家里的经济也要被压迫……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xFE,
        "嗯，到底是怎么了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_11BE")

    ChrTalk(    #75
        0xFE,
        (
            "看来果然只有用美味\x01",
            "才能让那个人打起精神来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "只能尝试各种方式了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_11FA")

    label("loc_11BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_11FA")

    ChrTalk(    #77
        0xFE,
        "真拿他没办法。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "得让他有精神\x01",
            "好好地工作……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11FA")

    TalkEnd(0xFE)
    Return()

    # Function_7_104B end

    def Function_8_11FE(): pass

    label("Function_8_11FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_125F")

    ChrTalk(    #79
        0xFE,
        (
            "因为现在是在紧急情况下，\x01",
            "我觉得这是很重要的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        (
            "爸爸这么高兴\x01",
            "真令人在意～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_12B3")

    ChrTalk(    #81
        0xFE,
        (
            "结论是我家的老大\x01",
            "果然是妈妈。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "爸爸只能一辈子\x01",
            "被操控于鼓掌之间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_12B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1300")

    ChrTalk(    #83
        0xFE,
        "原来如此……不愧是妈妈。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "得做个笔记……\x01",
            "将来说不定有用。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_1300")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1341")

    ChrTalk(    #85
        0xFE,
        "妈妈接下来会怎么做呢？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "我就慢慢\x01",
            "观战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_1341")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_139D")

    ChrTalk(    #87
        0xFE,
        (
            "为了给爸爸精神起来，\x01",
            "今天准备了上好的煎牛排哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "妈妈是不是\x01",
            "太宠爸爸了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1442")

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1442")

    ChrTalk(    #89
        0xFE,
        (
            "爸爸如果没像武术大会和诞辰庆典\x01",
            "这样的活动就会变得颓废。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "因为只有在有活动时\x01",
            "他才能管这个家。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xFE,
        "你不觉得这很正常吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        "因为在我家妈妈最有实力。\x02",
    )

    CloseMessageWindow()

    label("loc_1442")

    TalkEnd(0xFE)
    Return()

    # Function_8_11FE end

    def Function_9_1446(): pass

    label("Function_9_1446")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_14B1")

    ChrTalk(    #93
        0xFE,
        (
            "想不到不能使用导力器\x01",
            "这么令人不安……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        "不知他是否平安……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "至少能来个信\x01",
            "也好……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176F")

    label("loc_14B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1538")

    ChrTalk(    #96
        0xFE,
        (
            "虽说是在港口，\x01",
            "可也离这儿不远啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0xFE,
        (
            "丈夫不在家的时候\x01",
            "我一定要好好保护莉安妮……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        (
            "我不想让她再受政变时\x01",
            "那样的罪。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176F")

    label("loc_1538")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_15D0")

    ChrTalk(    #99
        0xFE,
        (
            "政变结束之后\x01",
            "我丈夫好像一直很忙。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "就算去格兰赛尔，\x01",
            "也没什么时间过来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "至少能让莉安妮\x01",
            "见上一面也好啊，\x01",
            "不过现在可能也没办法……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176F")

    label("loc_15D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_161E")

    ChrTalk(    #102
        0xFE,
        (
            "真没想到会有那种人\x01",
            "潜入我家……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "莉安妮没事真是\x01",
            "谢天谢地。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176F")

    label("loc_161E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16A3")

    ChrTalk(    #104
        0xFE,
        (
            "前不久希德中校\x01",
            "来这里玩过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "我孙女也很喜欢\x01",
            "亲近中校……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "呵呵，中校非常喜欢小孩子，\x01",
            "孩子们也能明白这点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176F")

    label("loc_16A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1713")

    ChrTalk(    #107
        0xFE,
        (
            "我那讨厌游击士的丈夫，\x01",
            "最近也常提到协会两个字呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        (
            "可能是受卡西乌斯的影响。\x01",
            "我真有点惊讶……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176F")

    label("loc_1713")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_176F")

    ChrTalk(    #109
        0xFE,
        (
            "听到卡西乌斯准将要复出的时候\x01",
            "我丈夫那股子高兴劲儿啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "真想让你们也看看。\x02",
    )

    CloseMessageWindow()

    label("loc_176F")

    TalkEnd(0xFE)
    Return()

    # Function_9_1446 end

    def Function_10_1773(): pass

    label("Function_10_1773")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17D6")

    ChrTalk(    #111
        0xFE,
        (
            "这种时候家里只有女人\x01",
            "真叫人不安～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0xFE,
        (
            "至少我要代替老爷来\x01",
            "保护夫人和莉安妮小姐！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F0")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1851")

    ChrTalk(    #113
        0xFE,
        (
            "哇，港口那边好像有\x01",
            "坦克大闹过了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "听说那坦克是冲着\x01",
            "市区去的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xFE,
        (
            "……也就是说本来\x01",
            "有可能经过这里～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F0")

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_18B3")

    ChrTalk(    #116
        0xFE,
        (
            "我倒是更担心那挂念着\x01",
            "老爷的太太自身的健康。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "她多少应该吃点好吃的\x01",
            "来补充体力～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F0")

    label("loc_18B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_18FF")

    ChrTalk(    #118
        0xFE,
        (
            "晚上我会\x01",
            "好好地锁门！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "一定不能再让那种\x01",
            "可疑的人进来了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F0")

    label("loc_18FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1938")

    ChrTalk(    #120
        0xFE,
        (
            "莉安妮小姐还饿着肚子，\x01",
            "我得抓紧了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F0")

    label("loc_1938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_198F")

    ChrTalk(    #121
        0xFE,
        "老爷最近似乎有点变化……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "不知是不是我多心，他好像\x01",
            "比以前更爱笑了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F0")

    label("loc_198F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_19F0")

    ChrTalk(    #123
        0xFE,
        (
            "老爷……摩尔根将军他\x01",
            "是个非常可怕的人～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "不过，呵呵……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#1S他拿夫人最没辙。\x02",
    )

    CloseMessageWindow()

    label("loc_19F0")

    TalkEnd(0xFE)
    Return()

    # Function_10_1773 end

    def Function_11_19F4(): pass

    label("Function_11_19F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A41")

    ChrTalk(    #126
        0xFE,
        (
            "太阳落山后\x01",
            "房间里变得漆黑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "太阳一直\x01",
            "不落山就好了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1A41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C7, 5)), scpexpr(EXPR_END)), "loc_1A93")

    ChrTalk(    #128
        0xFE,
        (
            "今天奶奶也\x01",
            "不让我出去……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "最近理查德哥哥也\x01",
            "不来玩，真没劲……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1A93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1AFB")

    ChrTalk(    #130
        0xFE,
        (
            "下次要让爷爷带我去\x01",
            "离宫～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        (
            "以前虽然在离宫发生了可怕的事，\x01",
            "不过和爷爷在一起我就不怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1AFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1B41")

    ChrTalk(    #132
        0xFE,
        (
            "我说我说，\x01",
            "怪盗是个怎样的人？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "莉安妮\x01",
            "好想见见他。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1B41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C4, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B82")

    ChrTalk(    #134
        0xFE,
        (
            "今天玩了很久，\x01",
            "肚子饿了！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "晚饭还没好吗～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C3, 2)), scpexpr(EXPR_END)), "loc_1BD5")

    ChrTalk(    #136
        0xFE,
        (
            "不久前我在大圣堂\x01",
            "碰到了穿白色衣服的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "真想和那孩子玩玩～\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C1E")

    label("loc_1BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C1, 3)), scpexpr(EXPR_END)), "loc_1C1E")
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #138
        0xFE,
        (
            "啊，你是救过莉安妮的\x01",
            "艾丝蒂尔！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        "是来找我玩的吗？\x02",
    )

    CloseMessageWindow()

    label("loc_1C1E")

    TalkEnd(0xFE)
    Return()

    # Function_11_19F4 end

    SaveToFile()

Try(main)
