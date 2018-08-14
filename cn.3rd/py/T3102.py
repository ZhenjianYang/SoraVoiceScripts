from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3102   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3102.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '乘客',                                 # 9
        '乘客',                                 # 10
        '女孩子',                               # 11
        '女性客人',                             # 12
        '男孩',                                 # 13
        '乘客',                                 # 14
        '乘客',                                 # 15
        '乘客',                                 # 16
        '接待员吉拉尔',                         # 17
        '格斯塔夫维修长',                       # 18
        '巴拉特',                               # 19
        '赛希莉亚号',                           # 20
        '赛希莉亚号影',                         # 21
        '目标用照相机',                         # 22
        '蔡斯市·工房区',                       # 23
        '',                                     # 24
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH01150 ._CH',             # 01
        'ED6_DT07/CH01170 ._CH',             # 02
        'ED6_DT07/CH01130 ._CH',             # 03
        'ED6_DT07/CH01470 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01360 ._CH',             # 06
        'ED6_DT07/CH01290 ._CH',             # 07
        'ED6_DT07/CH01450 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01020 ._CH',             # 0A
        'ED6_DT07/CH01210 ._CH',             # 0B
        'ED6_DT07/CH01140 ._CH',             # 0C
        'ED6_DT07/CH01680 ._CH',             # 0D
        'ED6_DT07/CH02440 ._CH',             # 0E
        'ED6_DT07/CH01180 ._CH',             # 0F
        'ED6_DT07/CH01200 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH01150P._CP',             # 01
        'ED6_DT07/CH01170P._CP',             # 02
        'ED6_DT07/CH01130P._CP',             # 03
        'ED6_DT07/CH01470P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01360P._CP',             # 06
        'ED6_DT07/CH01290P._CP',             # 07
        'ED6_DT07/CH01450P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01020P._CP',             # 0A
        'ED6_DT07/CH01210P._CP',             # 0B
        'ED6_DT07/CH01140P._CP',             # 0C
        'ED6_DT07/CH01680P._CP',             # 0D
        'ED6_DT07/CH02440P._CP',             # 0E
        'ED6_DT07/CH01180P._CP',             # 0F
        'ED6_DT07/CH01200P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -20110,
        Z                   = 8000,
        Y                   = 121830,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -42770,
        Z                   = 8000,
        Y                   = 129500,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -44640,
        Z                   = -4000,
        Y                   = 151290,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -18770,
        Z                   = 8000,
        Y                   = 89560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -19980,
        TriggerZ            = 8000,
        TriggerY            = 119710,
        TriggerRange        = 400,
        ActorX              = -20110,
        ActorZ              = 9500,
        ActorY              = 121830,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -41010,
        TriggerZ            = 8000,
        TriggerY            = 122500,
        TriggerRange        = 800,
        ActorX              = -41010,
        ActorZ              = 10200,
        ActorY              = 122500,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38900,
        TriggerZ            = 8400,
        TriggerY            = 122040,
        TriggerRange        = 800,
        ActorX              = -38900,
        ActorZ              = 9900,
        ActorY              = 122040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_37E",          # 00, 0
        "Function_1_3B0",          # 01, 1
        "Function_2_3E8",          # 02, 2
        "Function_3_555",          # 03, 3
        "Function_4_55A",          # 04, 4
        "Function_5_734",          # 05, 5
        "Function_6_AE9",          # 06, 6
        "Function_7_BB2",          # 07, 7
        "Function_8_1014",         # 08, 8
        "Function_9_1113",         # 09, 9
        "Function_10_116B",        # 0A, 10
        "Function_11_11A5",        # 0B, 11
        "Function_12_1243",        # 0C, 12
    )


    def Function_0_37E(): pass

    label("Function_0_37E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38A")

    label("loc_38A")

    OP_A3(0x3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_3AF")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_A2(0x3)
    Event(0, 7)

    label("loc_3AF")

    Return()

    # Function_0_37E end

    def Function_1_3B0(): pass

    label("Function_1_3B0")

    OP_16(0x2, 0xFA0, 0xFFFD6020, 0x4E20, 0x230053)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3D8")
    OP_A3(0x3)
    OP_B1("T3102_1")
    Jump("loc_3E7")

    label("loc_3D8")

    OP_B1("T3102_2")
    OP_71(0x400, 0x0)
    ExitThread()

    label("loc_3E7")

    Return()

    # Function_1_3B0 end

    def Function_2_3E8(): pass

    label("Function_2_3E8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40D")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_53F")

    label("loc_40D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_426")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_53F")

    label("loc_426")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43F")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_53F")

    label("loc_43F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_53F")

    label("loc_458")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_53F")

    label("loc_471")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_53F")

    label("loc_48A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A3")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_53F")

    label("loc_4A3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4BC")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_53F")

    label("loc_4BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DE")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_53F")

    label("loc_4DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_53F")

    label("loc_4F7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_510")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_53F")

    label("loc_510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_53F")

    label("loc_529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_53F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_554")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_53F")

    label("loc_554")

    Return()

    # Function_2_3E8 end

    def Function_3_555(): pass

    label("Function_3_555")

    Call(0, 4)
    Return()

    # Function_3_555 end

    def Function_4_55A(): pass

    label("Function_4_55A")

    TalkBegin(0x18)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_730")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 3)), scpexpr(EXPR_END)), "loc_672")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5E7")

    ChrTalk(    #0
        0x18,
        (
            "由于我长时间观察客人，\x01",
            "所以他们是因为工作还是因为私事而来\x01",
            "我还是能分清楚的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x18,
        "所以别这么盯着我看……\x02",
    )

    CloseMessageWindow()
    Jump("loc_66F")

    label("loc_5E7")


    ChrTalk(    #2
        0x18,
        "刚才开玩笑是我不好。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x18,
        (
            "不过啊，\x01",
            "既然是做这行的……\x02",
        )
    )

    Jump("loc_631")

    label("loc_631")

    CloseMessageWindow()

    ChrTalk(    #4
        0x18,
        (
            "经过这里的人\x01",
            "是因为工作还是私事\x01",
            "我还是能分清楚的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_66F")

    Jump("loc_730")

    label("loc_672")


    ChrTalk(    #5
        0x18,
        (
            "哟，阿加特。\x01",
            "你很遵守时间嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x18,
        "哈哈哈，我知道的。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x18,
        (
            "『月末的星期五』\x01",
            "你有要事对吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x106,
        "#057F…………………………（瞪）\x02",
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #9
        0x18,
        "别、别这么生气嘛……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F8B)

    label("loc_730")

    TalkEnd(0x18)
    Return()

    # Function_4_55A end

    def Function_5_734(): pass

    label("Function_5_734")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_AE5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F1, 5)), scpexpr(EXPR_END)), "loc_8CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_7DA")

    ChrTalk(    #10
        0x19,
        (
            "#691F既然丹已经回来了，\x01",
            "真想也把他带去\x01",
            "进行打捞作业……\x02\x03",

            "不过那家伙似乎挺忙的，\x01",
            "今天也没时间出来。\x02\x03",

            "下次再说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C8")

    label("loc_7DA")


    ChrTalk(    #11
        0x19,
        (
            "#690F啊啊，这么说来\x01",
            "我听说丹和小艾莉卡\x01",
            "已经回来了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x106,
        (
            "#552F（……小艾莉卡…………？）\x02\x03",

            "（是说艾莉卡·拉赛尔吗？）\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x19,
        (
            "#691F今天好像\x01",
            "没有见面的时间啊。\x02\x03",

            "算了，\x01",
            "下次再请她去喝酒吧。\x02",
        )
    )

    Jump("loc_8C4")

    label("loc_8C4")

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_8C8")

    Jump("loc_AE5")

    label("loc_8CB")


    ChrTalk(    #14
        0x19,
        (
            "#691F哟，这不是阿加特吗。\x01",
            "好久不见了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        (
            "#052F啊啊，是你。\x02\x03",

            "#051F听说『辉之环』事件之后\x01",
            "你们工房船正在各地巡回\x01",
            "对导力设施进行修复……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x19,
        (
            "#691F哈哈，算是吧。\x02\x03",

            "#690F那之后，因为埃尔赛尤的修补作业\x01",
            "而一直待在雷斯顿要塞里。\x02\x03",

            "好不容易才回到蔡斯。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x106,
        "#555F那、那可真够呛……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x19,
        (
            "#691F而且事情\x01",
            "才刚刚开始呢。\x02\x03",

            "重新整理好船载装备，\x01",
            "接下来才要进入\x01",
            "真正的重点——打捞作业。\x02\x03",

            "虽然打捞『利贝尔·方舟』\x01",
            "是从很早以前就开始的计划……\x02\x03",

            "但这边也一直没什么空。\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_A2(0x2F8D)

    label("loc_AE5")

    TalkEnd(0xFE)
    Return()

    # Function_5_734 end

    def Function_6_AE9(): pass

    label("Function_6_AE9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F0, 5)), scpexpr(EXPR_END)), "loc_BAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_B55")

    ChrTalk(    #19
        0xFE,
        (
            "接下来好像是\x01",
            "要前往瓦雷利亚湖。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "听说是要去调查，\x01",
            "……到底是在调查什么呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BAE")

    label("loc_B55")


    ChrTalk(    #21
        0xFE,
        (
            "哎呀，\x01",
            "离出港时间只有１５分钟了。\x02",
        )
    )

    Jump("loc_B86")

    label("loc_B86")

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "唉，这艘工房船也真是够忙的。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_BAE")

    TalkEnd(0xFE)
    Return()

    # Function_6_AE9 end

    def Function_7_BB2(): pass

    label("Function_7_BB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x1)
    ClearMapFlags(0x10)
    OP_6D(-32960, -4000, 149340, 0)
    OP_67(0, 10520, -10000, 0)
    OP_6B(10800, 0)
    OP_6C(70000, 0)
    OP_6E(175, 0)
    SetChrFlags(0x19, 0x80)
    OP_71(0x400, 0x0)
    ExitThread()
    OP_A1(0x1B, 0x4)
    OP_72(0x404, 0x0)
    ExitThread()
    OP_72(0x2004, 0x0)
    ExitThread()
    SetChrPos(0x1B, -34000, -150, 148000, 0)
    SetChrFlags(0x1B, 0x4)
    OP_A1(0x1C, 0x5)
    OP_72(0x405, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    SetChrPos(0x1C, -34000, -10150, 148000, 0)
    SetChrFlags(0x1C, 0x4)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x406, 0x0)
    ExitThread()
    OP_6F(0x3, 100)
    OP_6F(0x4, 60)
    OP_6F(0x5, 0)
    FadeToBright(1500, 0)
    OP_C8(0x200, 0x46, "C_PLAC08._CH", 0x0, 0x7D0)

    def lambda_CA2():
        OP_6D(-32960, -6000, 149340, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_CA2)

    def lambda_CBA():
        OP_6C(50000, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_CBA)

    def lambda_CCA():
        OP_67(0, 6880, -10000, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_CCA)

    def lambda_CE2():
        OP_6B(7800, 11000)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_CE2)
    Call(0, 8)
    OP_43(0x16, 0x3, 0x0, 0x9)
    Sleep(1200)
    OP_43(0x15, 0x3, 0x0, 0x9)
    Sleep(900)
    OP_43(0x10, 0x3, 0x0, 0x9)
    Sleep(1400)
    OP_43(0x17, 0x3, 0x0, 0x9)
    Sleep(2000)
    OP_43(0x106, 0x3, 0x0, 0xA)
    Sleep(6000)
    Fade(1000)
    OP_6D(-47600, -4000, 144600, 0)
    OP_67(0, 7080, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(302000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x106, 0x3)
    Sleep(300)

    ChrTalk(    #23
        0x106,
        (
            "#551F哎呀，真麻烦啊…………\x01",
            "要是没做那种约定就好了。\x02\x03",

            "当时被那小鬼逼着，\x01",
            "不知不觉就说出什么\x01",
            "『月末的星期五』来……\x02\x03",

            "#552F为了去吃一次饭，\x01",
            "每个月还得\x01",
            "特地调整行程…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_62(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x106)
    Sleep(300)
    OP_8C(0x106, 180, 400)
    Sleep(300)

    ChrTalk(    #24
        0x106,
        (
            "#556F#11P……唉，算了。\x01",
            "反正也欠那家伙的人情。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_EB2():
        OP_6D(-47600, -4000, 142500, 1500)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_EB2)

    def lambda_ECA():
        OP_8E(0xFE, 0xFFFF4A5C, 0xFFFFF060, 0x22858, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_ECA)
    WaitChrThread(0x1D, 0x0)
    WaitChrThread(0x106, 0x1)

    def lambda_EEF():
        OP_9E(0xFE, 0xF, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_EEF)
    Sleep(1000)
    OP_62(0x106, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #25
        0x106,
        (
            "#055F#11P怎、怎么…………？\x01",
            "突然感觉一股寒气…………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F6B():
        OP_9E(0xFE, 0xA, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_F6B)
    Sleep(1500)

    ChrTalk(    #26
        0x106,
        (
            "#555F#11P？？？\x02\x03",

            "算、算了……\x02\x03",

            "#552F好像\x01",
            "也不是感冒……\x02",
        )
    )

    Jump("loc_FDB")

    label("loc_FDB")

    CloseMessageWindow()

    def lambda_FE2():
        OP_8E(0xFE, 0xFFFF4A5C, 0x0, 0x1EE88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_FE2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T3121   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_BB2 end

    def Function_8_1014(): pass

    label("Function_8_1014")


    def lambda_101A():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_101A)

    def lambda_1035():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFE412, 0x24220, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1035)
    WaitChrThread(0x1B, 0x1)

    def lambda_1055():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD85A, 0x24220, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1055)
    WaitChrThread(0x1B, 0x1)

    def lambda_1075():
        OP_8F(0xFE, 0xFFFF7B30, 0xFFFFD472, 0x24220, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1075)
    WaitChrThread(0x1B, 0x1)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    SetChrPos(0x1B, -34000, -11150, 148000, 0)
    Sleep(1000)
    OP_22(0x76, 0x0, 0x46)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x1)
    Sleep(1100)
    OP_22(0x78, 0x0, 0x64)
    OP_6F(0x3, 100)
    OP_70(0x3, 0xC8)
    Sleep(2500)
    OP_6F(0x4, 410)
    OP_70(0x4, 0x1CC)
    OP_22(0x6, 0x0, 0x64)
    Sleep(800)
    OP_22(0x6, 0x0, 0x64)
    OP_73(0x4)
    OP_44(0x0, 0x1)
    Return()

    # Function_8_1014 end

    def Function_9_1113(): pass

    label("Function_9_1113")

    SetChrPos(0xFE, -33850, -4000, 149000, 180)
    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    OP_8E(0xFE, 0xFFFF7BC6, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A5C, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A5C, 0x0, 0x1EE88, 0x7D0, 0x0)
    Return()

    # Function_9_1113 end

    def Function_10_116B(): pass

    label("Function_10_116B")

    SetChrPos(0xFE, -33850, -4000, 149000, 180)
    OP_8E(0xFE, 0xFFFF7BC6, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFF4A5C, 0xFFFFF060, 0x2321C, 0x7D0, 0x0)
    Return()

    # Function_10_116B end

    def Function_11_11A5(): pass

    label("Function_11_11A5")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #27
        (
            "\x07\x05定期船起降坪\x01",
            "≡　开往王都格兰赛尔\x01",
            "≡　开往卢安市\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #28
        (
            "\x07\x05※请勿携带易燃物和危险品\x01",
            "　　　　　利贝尔飞艇公社\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_11A5 end

    def Function_12_1243(): pass

    label("Function_12_1243")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        (
            "\x07\x05　　　飞艇坪塔台　　　　\x01",
            "　※无关人员禁止入内　　\x01",
            "      『利贝尔飞艇公社』　\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_12_1243 end

    SaveToFile()

Try(main)
