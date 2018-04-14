from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1310   ._SN',
        MapName             = 'Bose',
        Location            = 'T1310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T1310_1 ._SN',
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
        '赛尔斯特队长',                         # 9
        '赛罗斯副队长',                         # 10
        '士兵艾格尔',                           # 11
        '士兵迈奇',                             # 12
        '芙拉瑟',                               # 13
        '雷伊',                                 # 14
        '安东尼',                               # 15
        '小说',                                 # 16
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
        'ED6_DT07/CH01310 ._CH',             # 00
        'ED6_DT07/CH01300 ._CH',             # 01
        'ED6_DT07/CH01300 ._CH',             # 02
        'ED6_DT07/CH01300 ._CH',             # 03
        'ED6_DT07/CH01090 ._CH',             # 04
        'ED6_DT07/CH01220 ._CH',             # 05
        'ED6_DT07/CH01700 ._CH',             # 06
        'ED6_DT06/CH20021 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH01310P._CP',             # 00
        'ED6_DT07/CH01300P._CP',             # 01
        'ED6_DT07/CH01300P._CP',             # 02
        'ED6_DT07/CH01300P._CP',             # 03
        'ED6_DT07/CH01090P._CP',             # 04
        'ED6_DT07/CH01220P._CP',             # 05
        'ED6_DT07/CH01700P._CP',             # 06
        'ED6_DT06/CH20021P._CP',             # 07
    )

    DeclNpc(
        X                   = 82120,
        Z                   = 0,
        Y                   = 12850,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 19950,
        Z                   = 0,
        Y                   = 22480,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 20000,
        Z                   = 0,
        Y                   = 7310,
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
        X                   = 80100,
        Z                   = 0,
        Y                   = 11110,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 82940,
        Z                   = 0,
        Y                   = 52010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 20490,
        Z                   = 0,
        Y                   = 14850,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 20480,
        Z                   = 0,
        Y                   = 13660,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 77080,
        Z                   = 750,
        Y                   = 6240,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1703943,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1E6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 20950,
        TriggerZ            = 0,
        TriggerY            = 22480,
        TriggerRange        = 800,
        ActorX              = 19950,
        ActorZ              = 1600,
        ActorY              = 22480,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 20950,
        TriggerZ            = 0,
        TriggerY            = 7310,
        TriggerRange        = 800,
        ActorX              = 20000,
        ActorZ              = 1600,
        ActorY              = 7310,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 18440,
        TriggerZ            = 0,
        TriggerY            = 12120,
        TriggerRange        = 1000,
        ActorX              = 18440,
        ActorZ              = 1000,
        ActorY              = 12120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_2F7",          # 01, 1
        "Function_2_390",          # 02, 2
        "Function_3_50D",          # 03, 3
        "Function_4_C7E",          # 04, 4
        "Function_5_19FD",         # 05, 5
        "Function_6_214B",         # 06, 6
        "Function_7_26AD",         # 07, 7
        "Function_8_2DC7",         # 08, 8
        "Function_9_3343",         # 09, 9
        "Function_10_3359",        # 0A, 10
        "Function_11_335E",        # 0B, 11
        "Function_12_3363",        # 0C, 12
        "Function_13_36FF",        # 0D, 13
        "Function_14_3ADC",        # 0E, 14
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26F")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_26F")

    Jump("loc_2F6")

    label("loc_272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_2C3")
    SetChrPos(0xB, 77380, 0, 7430, 186)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297")
    ClearChrFlags(0xF, 0x80)

    label("loc_297")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C0")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C0")
    SetChrFlags(0xC, 0x10)

    label("loc_2C0")

    Jump("loc_2F6")

    label("loc_2C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_2DE")
    SetChrPos(0xB, 82080, 0, 56640, 357)
    Jump("loc_2F6")

    label("loc_2DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0xB, 19210, 0, 15060, 270)

    label("loc_2F6")

    Return()

    # Function_0_256 end

    def Function_1_2F7(): pass

    label("Function_1_2F7")

    OP_B1("T1310_n")
    OP_72(0x2, 0x10)
    OP_6F(0x2, 99)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31D")
    OP_1B(0x0, 0x0, 0xC)

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32E")
    OP_1B(0x5, 0x0, 0xD)

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 3)), scpexpr(EXPR_END)), "loc_33A")
    SetChrFlags(0xF, 0x80)

    label("loc_33A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38F")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_38F")

    Return()

    # Function_1_2F7 end

    def Function_2_390(): pass

    label("Function_2_390")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4F7")

    label("loc_3B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4F7")

    label("loc_3CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4F7")

    label("loc_3E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_400")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4F7")

    label("loc_400")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_419")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4F7")

    label("loc_419")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_432")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4F7")

    label("loc_432")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4F7")

    label("loc_44B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_464")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4F7")

    label("loc_464")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4F7")

    label("loc_47D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_496")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4F7")

    label("loc_496")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4AF")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4F7")

    label("loc_4AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4F7")

    label("loc_4C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4F7")

    label("loc_4E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_50C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4F7")

    label("loc_50C")

    Return()

    # Function_2_390 end

    def Function_3_50D(): pass

    label("Function_3_50D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_616")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CF")

    ChrTalk(    #0
        0xFE,
        (
            "听说王立学院中\x01",
            "出事了呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "还听说军队马上\x01",
            "派遣了守备队…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "能有这么快的应对措施，\x01",
            "多亏了通信装置的恢复啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "看来最可怕的事情\x01",
            "就是信息和情报的无法传送了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_613")

    label("loc_5CF")


    ChrTalk(    #4
        0xFE,
        (
            "听说军队向王立学院\x01",
            "派遣了部队。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "我们也加强警备\x01",
            "比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_613")

    Jump("loc_C7A")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_75B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DB")

    ChrTalk(    #6
        0xFE,
        (
            "多亏了那些发生器，\x01",
            "通信总算是恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "这样一来，至少\x01",
            "王国军可以进行整体规划行动了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "虽然还有很多困难要克服，\x01",
            "不过凭卡西乌斯准将的指挥能力，\x01",
            "相信一定没有问题的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_758")

    label("loc_6DB")


    ChrTalk(    #9
        0xFE,
        (
            "多亏了那些发生器，\x01",
            "通信总算是恢复了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "虽然还有很多困难要克服，\x01",
            "不过凭卡西乌斯准将的指挥能力，\x01",
            "相信一定没有问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_758")

    Jump("loc_C7A")

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_81D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7B6")

    ChrTalk(    #11
        0xFE,
        (
            "希望暂时别再\x01",
            "发生什么意外了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "士兵们也需要\x01",
            "稍微缓解一下神经啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_81A")

    label("loc_7B6")


    ChrTalk(    #13
        0xFE,
        (
            "我们的警备状态\x01",
            "终于解除了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "当队长的话就\x01",
            "不能示弱。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "希望暂时别再\x01",
            "发生什么意外了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_81A")

    Jump("loc_C7A")

    label("loc_81D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_8AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_84F")

    ChrTalk(    #16
        0xFE,
        (
            "传说中的龙\x01",
            "竟然真的出现了…\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7")

    label("loc_84F")


    ChrTalk(    #17
        0xFE,
        (
            "传说中的龙\x01",
            "竟然真的出现了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "哎呀呀，看来空之女神\x01",
            "真的很眷顾\x01",
            "我们王国军呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_8A7")

    Jump("loc_C7A")

    label("loc_8AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_9B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_91F")

    ChrTalk(    #19
        0xFE,
        (
            "不但平息了王都的动乱，\x01",
            "国内的不安分者也全部被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "这样我们守备部队\x01",
            "就可以高枕无忧了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9B1")

    label("loc_91F")


    ChrTalk(    #21
        0xFE,
        (
            "原情报部队的上校会出现，\x01",
            "真是让人不敢相信…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "平息了那个事件，\x01",
            "国内的不安分者也全部被逮捕了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "这样我们守备部队\x01",
            "就可以高枕无忧了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_9B1")

    Jump("loc_C7A")

    label("loc_9B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_A87")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A25")

    ChrTalk(    #24
        0xFE,
        (
            "听说王立学院中\x01",
            "潜藏着一名犯罪组织的成员啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "真是的，\x01",
            "稍微一不留神就会被他们趁虚而入。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A84")

    label("loc_A25")

    OP_A2(0x0)

    ChrTalk(    #26
        0xFE,
        (
            "听说王立学院中\x01",
            "潜藏着一名犯罪组织的成员啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "军队高层也对那组织\x01",
            "展开严密的调查了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A84")

    Jump("loc_C7A")

    label("loc_A87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_B74")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AEA")

    ChrTalk(    #28
        0xFE,
        (
            "卢安市的市长选举\x01",
            "马上也要投票了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "这次的选举\x01",
            "要是能平安结束就好了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B71")

    label("loc_AEA")

    OP_A2(0x0)

    ChrTalk(    #30
        0xFE,
        (
            "卢安市的市长选举\x01",
            "马上也要投票了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        (
            "虽然最近一直处于混乱状况，\x01",
            "不过选举还是进入到白热化状态了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "虽然应该不会出什么事。\x02",
    )

    CloseMessageWindow()

    label("loc_B71")

    Jump("loc_C7A")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_C7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BD1")

    ChrTalk(    #33
        0xFE,
        (
            "王国军\x01",
            "依然保持着高度警戒状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "情报部的余党和空贼团\x01",
            "都去向不明。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C7A")

    label("loc_BD1")

    OP_A2(0x0)

    ChrTalk(    #35
        0xFE,
        (
            "王国军\x01",
            "依然保持着高度警戒状态。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "情报部的余党和空贼团\x01",
            "都去向不明。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "空贼团也就罢了，\x01",
            "但特务部队实在是个隐患啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "再怎么说，\x01",
            "他们也是正规的精锐部队。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C7A")

    TalkEnd(0xFE)
    Return()

    # Function_3_50D end

    def Function_4_C7E(): pass

    label("Function_4_C7E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_D5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0A")

    ChrTalk(    #39
        0x9,
        (
            "导力器不能用了，\x01",
            "现在想做料理也很难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x9,
        (
            "不能使用导力炉\x01",
            "真是让人头疼啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x9,
        (
            "那个神奇的发生器\x01",
            "真想要1个呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_D5A")

    label("loc_D0A")


    ChrTalk(    #42
        0x9,
        (
            "导力器不能用了，\x01",
            "现在想做料理也很难。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x9,
        (
            "那个神奇的发生器\x01",
            "真想要１个呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5A")

    Jump("loc_19F9")

    label("loc_D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_E6C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E09")

    ChrTalk(    #44
        0x9,
        (
            "以前袭击这里的红莲士兵\x01",
            "还带着武装精良的魔兽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x9,
        (
            "虽然不知道他们的来历，\x01",
            "不过确实是强敌啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x9,
        (
            "现在那些家伙要是再来的话\x01",
            "就真的无法抵挡了啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_E69")

    label("loc_E09")


    ChrTalk(    #47
        0x9,
        (
            "那些红莲士兵们\x01",
            "还带着武装精良的魔兽呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x9,
        (
            "现在那些家伙要是再来的话\x01",
            "就真的无法抵挡了啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E69")

    Jump("loc_19F9")

    label("loc_E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_129C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_FB8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EF0")

    ChrTalk(    #49
        0x9,
        (
            "不管怎么说，这次的事件\x01",
            "协会也出了很多力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x9,
        (
            "高层打算和协会深度合作，\x01",
            "我也觉得这方针是正确的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB5")

    label("loc_EF0")


    ChrTalk(    #51
        0x9,
        "哟，辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x9,
        (
            "不管怎么说，这次的事件\x01",
            "协会也出了很多力呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x9,
        (
            "最近高层领导们决定\x01",
            "和协会加强合作的方针，\x01",
            "果然这是正确的方针啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x9,
        (
            "军队要是和游击士联手的话，\x01",
            "一定可以克服任何的困难。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_FB5")

    Jump("loc_1299")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_109F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_1031")

    ChrTalk(    #55
        0x9,
        (
            "龙好像逃到\x01",
            "迷雾峡谷中去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x9,
        (
            "那里的雾很浓，\x01",
            "飞船根本飞不进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x9,
        "……呼，真是厉害的生物啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_109C")

    label("loc_1031")


    ChrTalk(    #58
        0x9,
        (
            "龙好像逃到\x01",
            "迷雾峡谷中去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        (
            "那里的雾很浓，\x01",
            "飞船根本飞不进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x9,
        "……呼，真是厉害的生物啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_109C")

    Jump("loc_1299")

    label("loc_109F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1128")

    ChrTalk(    #61
        0x9,
        (
            "最近我们关所的警备\x01",
            "多少也是轻松一点了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        (
            "能回到平常状态，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "这下子终于也有空\x01",
            "做些自己喜欢吃的料理了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1299")

    label("loc_1128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_11CF")

    ChrTalk(    #64
        0x9,
        (
            "王立学院的事情…\x01",
            "协会已经通知我们了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x9,
        (
            "似乎是一名犯罪组织的成员，\x01",
            "呼～又出现奇怪的家伙了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        (
            "真是一波未平一波又起。\x01",
            "正义的一方总是得不到喘息啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1299")

    label("loc_11CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_1229")

    ChrTalk(    #67
        0x9,
        (
            "这附近的魔兽\x01",
            "都十分强悍。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "之前有个准游击士小哥\x01",
            "打不过它们逃回来了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1299")

    label("loc_1229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_1299")

    ChrTalk(    #69
        0x9,
        (
            "关所的警备\x01",
            "还是很严密的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        (
            "情报部的余党\x01",
            "似乎还潜伏在各地。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x9,
        (
            "总之要和游击士协会\x01",
            "联手应对啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1299")

    Jump("loc_19F9")

    label("loc_129C")

    OP_A2(0x122C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_14C4")

    ChrTalk(    #72
        0x9,
        "啊！？我还以为是谁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x106,
        (
            "#051F啊！好久不见了。\x02\x03",

            "上次一起打退魔兽之后就没再见面了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1337")

    ChrTalk(    #74
        0x103,
        "#023F嘿，有这种事啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1395")

    label("loc_1337")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_136A")

    ChrTalk(    #75
        0x104,
        (
            "#033F噢～～……\x01",
            "有那种事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1395")

    label("loc_136A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1395")

    ChrTalk(    #76
        0x108,
        "#073F喔，还有那种事啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1395")


    ChrTalk(    #77
        0x101,
        (
            "#1015F嗯，那次确实是\x01",
            "第一次和阿加特并肩战斗呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        "哈哈，那时真是谢谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        (
            "不过…\x01",
            "今天有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x106,
        (
            "#050F啊，其实我们\x01",
            "正在寻找通缉魔兽。\x02\x03",

            "顺便就来\x01",
            "这里看看。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x9,
        "那可辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "这样的话，\x01",
            "在这里稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x9,
        (
            "这附近的通缉魔兽\x01",
            "都十分强悍的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x101,
        (
            "#1001F谢谢啦。\x01",
            "那就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1735")

    label("loc_14C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1735")
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x106, 0)
    Sleep(400)

    ChrTalk(    #85
        0x9,
        "啊！？我还以为是谁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x106,
        (
            "#051F啊！好久不见了。\x02\x03",

            "上次一起打退魔兽之后就没再见面了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1571")

    ChrTalk(    #87
        0x107,
        (
            "#064F啊……\x01",
            "有那种事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FB")

    label("loc_1571")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_159D")

    ChrTalk(    #88
        0x103,
        "#023F嘿，有这种事啊？\x02",
    )

    CloseMessageWindow()
    Jump("loc_15FB")

    label("loc_159D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15D0")

    ChrTalk(    #89
        0x104,
        (
            "#033F噢～～……\x01",
            "有那种事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15FB")

    label("loc_15D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FB")

    ChrTalk(    #90
        0x108,
        "#073F喔，还有那种事啊。\x02",
    )

    CloseMessageWindow()

    label("loc_15FB")


    ChrTalk(    #91
        0x101,
        (
            "#1015F嗯，那次确实是\x01",
            "第一次和阿加特并肩战斗呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #92
        0x9,
        "哈哈，那时真是谢谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x9,
        (
            "不过…\x01",
            "今天有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x106,
        (
            "#050F啊，其实我们\x01",
            "正在寻找通缉魔兽。\x02\x03",

            "顺便就来\x01",
            "这里看看。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x106, 400)

    ChrTalk(    #95
        0x9,
        "那可辛苦了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x9,
        (
            "这样的话，\x01",
            "在这里稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        (
            "这附近的通缉魔兽\x01",
            "都十分强悍的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1006F谢谢啦。\x01",
            "那就这样吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1735")

    Jump("loc_19F9")

    label("loc_1738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_17E6")

    ChrTalk(    #99
        0x9,
        "啊！？我还以为是谁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x106,
        (
            "#051F啊！好久不见了。\x02\x03",

            "上次一起打退魔兽之后就没再见面了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        (
            "#1011F啊，还有那种事吗？\x02\x03",

            "#1015F那时确实是\x01",
            "第一次和阿加特并肩战斗呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_189C")

    label("loc_17E6")

    TurnDirection(0x9, 0x101, 0)

    ChrTalk(    #102
        0x9,
        "啊！？我还以为是谁。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        (
            "#1011F啊，好久不见了。\x02\x03",

            "上次在这里一起打退\x01",
            "魔兽之后就一直没见啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x103,
        "#023F嘿，有这种事啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        (
            "#1006F嗯，那时还是第一次\x01",
            "和阿加特并肩作战呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_189C")


    ChrTalk(    #106
        0x9,
        "哈哈，那时真是谢谢了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        (
            "不过…\x01",
            "今天有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1901")

    ChrTalk(    #108
        0x106,
        (
            "#050F啊，只是顺路\x01",
            "过来看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_1901")


    ChrTalk(    #109
        0x103,
        (
            "#020F没什么，只是顺路\x01",
            "过来看看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1927")


    ChrTalk(    #110
        0x9,
        (
            "原来如此。\x01",
            "是在修行中吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x9,
        (
            "哈，难得来一趟。\x01",
            "就在这里稍微休息一下吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x9,
        "这附近的魔兽可是很强的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        (
            "#1001F嗯，谢谢了。\x01",
            "那就这样吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x9,
        "好了，我也要回去工作了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "如果有事的话\x01",
            "就再来找我哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F9")

    TalkEnd(0x9)
    Return()

    # Function_4_C7E end

    def Function_5_19FD(): pass

    label("Function_5_19FD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_1B13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAE")

    ChrTalk(    #116
        0xFE,
        (
            "导力枪无法使用\x01",
            "对我们来说是最大的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "除了士官以上的长官，\x01",
            "普通的士兵并不会什么剑术。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xFE,
        (
            "要是那群红莲士兵再来袭击的话\x01",
            "我们还能应付得了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1B10")

    label("loc_1AAE")


    ChrTalk(    #119
        0xFE,
        (
            "导力枪无法使用\x01",
            "对我们来说是最大的问题。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "除了士官以上的长官，\x01",
            "普通的士兵并不会什么剑术。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B10")

    Jump("loc_2147")

    label("loc_1B13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1C28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC9")

    ChrTalk(    #121
        0xFE,
        (
            "空中出现了奇怪的东西，\x01",
            "导力器也无法使用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "利贝尔王国这次\x01",
            "真是面临重大危机了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "如、如果帝国\x01",
            "在这时候乘人之危的话…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        "……还、还是不要想了。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_1C25")

    label("loc_1BC9")


    ChrTalk(    #125
        0xFE,
        (
            "空中出现了奇怪的东西，\x01",
            "导力器也无法使用……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        (
            "利贝尔王国这次\x01",
            "真是面临重大危机了啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C25")

    Jump("loc_2147")

    label("loc_1C28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_1C9C")

    ChrTalk(    #127
        0xFE,
        (
            "虽然不知道具体过程，\x01",
            "不过龙的骚乱总算是平息了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xFE,
        (
            "嗯，摩尔根将军在关键时刻\x01",
            "果然还是值得信赖的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2147")

    label("loc_1C9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_1D77")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1D03")

    ChrTalk(    #129
        0xFE,
        (
            "龙明明在峡谷，\x01",
            "为什么我们要在这里警戒？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xFE,
        (
            "军队这种机构\x01",
            "就是这样不讲究效率啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D74")

    label("loc_1D03")


    ChrTalk(    #131
        0xFE,
        (
            "呼，进入警备状态之后\x01",
            "又要开始夜间巡逻了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        "不过，龙在峡谷吧？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        (
            "为什么我们古罗尼关所\x01",
            "也要警备呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1D74")

    Jump("loc_2147")

    label("loc_1D77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_1F59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 3)), scpexpr(EXPR_END)), "loc_1DE4")

    ChrTalk(    #134
        0xFE,
        (
            "这样一来，剩下的乐趣\x01",
            "就只有副队长的料理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "虽然不是很懂，\x01",
            "不过那真是职业水准啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F56")

    label("loc_1DE4")


    ChrTalk(    #136
        0xFE,
        "啊啊！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        (
            "这本书本来打算\x01",
            "吃完晚饭再看的，\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        (
            "不过看得太入神，\x01",
            "这么快就已经看完了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xFE,
        (
            "这个关所里\x01",
            "真是没什么娱乐啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        "算了，这本书就送你们吧。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0xF, 0x80)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #141
        "\x07\x00得到了\x1F\x40\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x240, 1)
    OP_A2(0x10BB)
    OP_0D()

    ChrTalk(    #142
        0xFE,
        (
            "这样一来，剩下的乐趣\x01",
            "就只有副队长的料理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "虽然不是很懂，\x01",
            "不过那真是职业水准啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "最近比较有时间，\x01",
            "经常在厨房里待着。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F56")

    Jump("loc_2147")

    label("loc_1F59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_1FE9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_1F98")

    ChrTalk(    #145
        0xFE,
        "今天轮到副队长做饭了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xFE,
        "真是期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FE6")

    label("loc_1F98")

    OP_A2(0x2)

    ChrTalk(    #147
        0xFE,
        "今天轮到副队长做饭了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0xFE,
        (
            "嗯～今天会做\x01",
            "什么菜呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "真是期待啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1FE6")

    Jump("loc_2147")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_203D")

    ChrTalk(    #150
        0xFE,
        (
            "柴火已经准备好了，\x01",
            "食材也准备完毕。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0xFE,
        (
            "呼～接下来\x01",
            "总算可以休息了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2147")

    label("loc_203D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_2147")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_20A4")

    ChrTalk(    #152
        0xFE,
        (
            "说起这里的乐趣，\x01",
            "也就只剩下副队长的料理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xFE,
        (
            "他退役之后\x01",
            "完全可以开家餐厅呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2147")

    label("loc_20A4")

    OP_A2(0x2)

    ChrTalk(    #154
        0xFE,
        (
            "哈哈～在山上真是\x01",
            "没有什么乐趣可言。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xFE,
        (
            "听说卢安开了新的\x01",
            "游戏吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xFE,
        (
            "说起这里的乐趣，\x01",
            "也就只剩下副队长的料理了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xFE,
        (
            "他退役之后\x01",
            "完全可以开家餐厅呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2147")

    TalkEnd(0xFE)
    Return()

    # Function_5_19FD end

    def Function_6_214B(): pass

    label("Function_6_214B")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_224D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F4")

    ChrTalk(    #158
        0xA,
        (
            "虽然现在关所这么严格，\x01",
            "谁也不能通过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0xA,
        (
            "呼～其实这种时候\x01",
            "也不会有人来旅行啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0xA,
        (
            "除了真的很闲很闲的人，\x01",
            "也就只有你们游击士会来这里了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_224A")

    label("loc_21F4")


    ChrTalk(    #161
        0xA,
        (
            "虽然现在关所这么严格，\x01",
            "谁也不能通过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0xA,
        (
            "呼～其实这种时候\x01",
            "也不会有人来旅行啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_224A")

    Jump("loc_26A9")

    label("loc_224D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EF")

    ChrTalk(    #163
        0xA,
        (
            "大门的开关坏了，\x01",
            "所以现在的通行检查更加严格。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0xA,
        (
            "不过，你们游击士是\x01",
            "可以自由通行的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xA,
        (
            "上面有命令下达。\x01",
            "和协会的合作是必不可少的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_2321")

    label("loc_22EF")


    ChrTalk(    #166
        0xA,
        (
            "你们游击士\x01",
            "可以自由通行的。\x01",
            "上面下达过命令。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2321")

    Jump("loc_26A9")

    label("loc_2324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_2388")

    ChrTalk(    #167
        0xA,
        (
            "听说那条龙\x01",
            "终于不再作乱了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xA,
        (
            "连飞行舰队都出动了，\x01",
            "这样的结果也是可以预料到的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A9")

    label("loc_2388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23DF")

    ChrTalk(    #169
        0xA,
        (
            "情报部的余党…\x01",
            "然后又出现古代龙…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xA,
        (
            "真是的，\x01",
            "这也太夸张了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_243E")

    label("loc_23DF")


    ChrTalk(    #171
        0xA,
        "还要继续警备啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xA,
        (
            "情报部的余党…\x01",
            "然后又出现古代龙…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xA,
        (
            "真是的，\x01",
            "这也太夸张了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_243E")

    Jump("loc_26A9")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x341, 5)), scpexpr(EXPR_END)), "loc_253B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_24AE")

    ChrTalk(    #174
        0xA,
        (
            "卢安的新市长\x01",
            "已经选中诺曼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xA,
        (
            "他虽然主张发展观光旅游业，\x01",
            "但也考虑到了港湾的维持。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2538")

    label("loc_24AE")


    ChrTalk(    #176
        0xA,
        (
            "卢安的新市长\x01",
            "已经选中诺曼了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xA,
        (
            "他虽然主张发展观光旅游业，\x01",
            "但也考虑到了港湾的维持。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xA,
        (
            "呼，果然把两边处理平衡\x01",
            "才能得人心啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_2538")

    Jump("loc_26A9")

    label("loc_253B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_25DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2581")

    ChrTalk(    #179
        0xA,
        (
            "啊啊～能不能尽快\x01",
            "将情报部的余党统统抓捕起来呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25DA")

    label("loc_2581")

    OP_A2(0x1)

    ChrTalk(    #180
        0xA,
        (
            "这样的警备状态\x01",
            "究竟要持续到什么时候啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0xA,
        (
            "夜里出来巡逻的时候\x01",
            "真是寒风刺骨啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25DA")

    Jump("loc_26A9")

    label("loc_25DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_264A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_261B")

    ChrTalk(    #182
        0xA,
        (
            "不过无论工不工作，\x01",
            "领的薪水都是一样的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2647")

    label("loc_261B")

    OP_A2(0x1)

    ChrTalk(    #183
        0xA,
        (
            "最近都没有客人，\x01",
            "这里也暂时停业了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2647")

    Jump("loc_26A9")

    label("loc_264A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_26A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2676")

    ChrTalk(    #184
        0xA,
        (
            "难道你们\x01",
            "喜欢爬山吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26A9")

    label("loc_2676")

    OP_A2(0x1)

    ChrTalk(    #185
        0xA,
        "竟然现在还来这里……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #186
        0xA,
        "还真是有闲心啊。\x02",
    )

    CloseMessageWindow()

    label("loc_26A9")

    TalkEnd(0xA)
    Return()

    # Function_6_214B end

    def Function_7_26AD(): pass

    label("Function_7_26AD")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_26C1")
    Call(1, 0)
    Jump("loc_2DC3")

    label("loc_26C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7A, 0x1, 0x4000)"), scpexpr(EXPR_END)), "loc_27B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_278B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_271C")

    ChrTalk(    #187
        0xFE,
        (
            "我正在参观\x01",
            "这里的设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xFE,
        (
            "不好意思，\x01",
            "能不能别打扰我？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2788")

    label("loc_271C")


    ChrTalk(    #189
        0xFE,
        "啊，各位…\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #190
        0xFE,
        (
            "再来这里\x01",
            "有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xFE,
        (
            "我正在参观\x01",
            "这里的设施。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #192
        0xFE,
        (
            "不好意思，\x01",
            "能不能别打扰我？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_2788")

    Jump("loc_27B6")

    label("loc_278B")


    ChrTalk(    #193
        0xFE,
        (
            "我还要继续\x01",
            "参观。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #194
        0xFE,
        "那么，失陪了。\x02",
    )

    CloseMessageWindow()

    label("loc_27B6")

    Jump("loc_2DC3")

    label("loc_27B9")


    ChrTalk(    #195
        0xFE,
        (
            "呼，总算\x01",
            "来到关所了…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0xFE,
        (
            "就一直待在这里\x01",
            "绝对不能回去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #197
        0xFE,
        (
            "如果\x01",
            "不安排人来迎接我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x101,
        (
            "#1019F（嗯……！？）\x02\x03",

            "#1015F（啊，这个人……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x0, 400)

    ChrTalk(    #199
        0xFE,
        "啊……！？\x02",
    )

    CloseMessageWindow()
    Sleep(700)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #200
        0xFE,
        "啊，艾丝蒂尔！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xFE,
        (
            "啊？你还记得我吗？\x01",
            "我是王立学院的芙拉瑟啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F1")

    ChrTalk(    #202
        0x101,
        (
            "#1018F啊，嗯！\x01",
            "当然记得。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x105,
        (
            "#040F你好啊，芙拉瑟。\x02\x03",

            "真没想到能在这种地方\x01",
            "再见到你。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #204
        0xFE,
        "啊？！科洛丝竟然也在！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0xFE,
        (
            "你们两个\x01",
            "为什么会来这种地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x101,
        (
            "#1006F嗯，我们的工作\x01",
            "是来这里寻找通缉魔兽。\x02\x03",

            "倒是芙拉瑟你，\x01",
            "为什么会在关所呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AD0")

    label("loc_29F1")


    ChrTalk(    #207
        0x101,
        (
            "#1001F啊，嗯！\x01",
            "当然记得。\x02\x03",

            "幽灵骚乱的时候\x01",
            "曾经在王立学院见过面呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #208
        0xFE,
        "嗯，能再次见面真是高兴啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #209
        0xFE,
        (
            "不过，为什么\x01",
            "要来这种地方呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #210
        0x101,
        (
            "#1006F嗯，我们的工作\x01",
            "是来这里寻找通缉魔兽。\x02\x03",

            "倒是芙拉瑟你，\x01",
            "为什么会在关所呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AD0")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #211
        0xFE,
        "……………啊！？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #212
        0x101,
        "#1015F嗯？怎么啦？\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #213
        0xFE,
        (
            "啊，没、没什么……\x01",
            "什么事也没有……\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #214
        0xFE,
        (
            "那……什…么……\x01",
            "那个，就是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xFE, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(600)
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #215
        0xFE,
        (
            "对了！社会参观…\x01",
            "我来关所进行社会参观考察！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0xFE,
        (
            "准备用做休假时的\x01",
            "研究课题！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #217
        0x101,
        (
            "#1004F嘿～是这样啊。\x01",
            "你还真是用心学习。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C8B")

    ChrTalk(    #218
        0x105,
        (
            "#044F？？？\x02\x03",

            "（有那样的课题吗？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4B")

    label("loc_2C8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CDA")

    ChrTalk(    #219
        0x107,
        (
            "#560F社会参观吗？\x02\x03",

            "学院的课题好有趣啊，\x01",
            "真是让提妲羡慕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4B")

    label("loc_2CDA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D15")

    ChrTalk(    #220
        0x103,
        (
            "#021F呵呵，不愧是王国\x01",
            "最好的学校啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4B")

    label("loc_2D15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D4B")

    ChrTalk(    #221
        0x108,
        (
            "#070F嗯，不愧是王立学院\x01",
            "的学生啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D4B")


    ChrTalk(    #222
        0xFE,
        (
            "那么，我还在\x01",
            "参观中，所以…\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #223
        0x101,
        (
            "#1008F啊，抱歉！\x01",
            "打扰你了。\x02\x03",

            "#1006F那么，再见啦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xFE,
        "嗯，再见！\x02",
    )

    CloseMessageWindow()
    OP_28(0x7A, 0x1, 0x4000)
    OP_A2(0x4)

    label("loc_2DC3")

    TalkEnd(0xC)
    Return()

    # Function_7_26AD end

    def Function_8_2DC7(): pass

    label("Function_8_2DC7")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x415, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B6")

    ChrTalk(    #225
        0xFE,
        (
            "哎呀，各位游击士。\x01",
            "能在这里见面真是奇遇啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E76")
    OP_62(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #226
        0x107,
        (
            "#064F啊！雷伊先生！？\x02\x03",

            "啊，你为什么会\x01",
            "在这种地方呢？！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x107, 400)
    OP_A2(0x20B0)
    Jump("loc_2EC2")

    label("loc_2E76")


    ChrTalk(    #227
        0x101,
        (
            "#1004F啊……！？\x01",
            "是中央工房的人啊，\x02\x03",

            "为、为什么会在这种地方呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    label("loc_2EC2")


    ChrTalk(    #228
        0xFE,
        (
            "嗯，其实我刚从『埃尔赛尤』下船，\x01",
            "现在正好返回蔡斯的途中。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0xFE,
        (
            "已经帮完博士的忙了，\x01",
            "接下来就该回实验室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x101,
        (
            "#1016F所、所以要\x01",
            "步行去蔡斯吗…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x102,
        (
            "#1035F不过，现在似乎\x01",
            "也没有别的交通工具啊。\x02\x03",

            "#1040F不如我们\x01",
            "把你送回去吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #232
        0xFE,
        (
            "哈哈～不用担心。\x01",
            "有人和我同行的。\x02",
        )
    )

    CloseMessageWindow()
    OP_4A(0xE, 255)
    TurnDirection(0xE, 0x0, 400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #233
        0xE,
        "喵～\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 400)

    ChrTalk(    #234
        0x101,
        (
            "#1001F哈哈……\x01",
            "安东尼也在一起吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #235
        0xFE,
        "其实它真的很可靠呢。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #236
        0xFE,
        (
            "另外我还准备了\x01",
            "各种对抗魔兽的食品武器…\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xFE,
        (
            "……对了，难得见面，\x01",
            "不如你们也试试吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)
    SetChrName("")

    AnonymousTalk(    #238
        "\x07\x00得到了\x1F\xE6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x1E6, 1)

    ChrTalk(    #239
        0xFE,
        "我发明的攻击性食品。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0xFE,
        (
            "平时你们也可以自己制作，\x01",
            "有兴趣的话试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x45)"), scpexpr(EXPR_END)), "loc_3136")
    Jump("loc_317D")

    label("loc_3136")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #241
        "\x1F\xE6\x01\x07\x00的做法已经学会了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_317D")

    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #242
        0x101,
        (
            "#1016F啊，谢谢……\x02\x03",

            "#1015F嗯、嗯……\x02\x03",

            "让、让他一个人回去\x01",
            "真的没问题吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #243
        0x102,
        (
            "#1048F其实我也很担心呢……\x02\x03",

            "#1040F……不过，他本人已经说没问题……\x01",
            "那，路上请一定小心啊。\x02\x03",

            "特别是卡鲁迪亚隧道，\x01",
            "那里现在非常危险呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #244
        0xFE,
        "呵呵，多谢忠告。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #245
        0xFE,
        "那么，下次在蔡斯再见吧。\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #246
        0xE,
        "喵～\x02",
    )

    CloseMessageWindow()
    OP_8C(0xE, 0, 400)
    OP_4B(0xE, 255)
    OP_A2(0x20AF)
    Jump("loc_333F")

    label("loc_32B6")


    ChrTalk(    #247
        0xFE,
        (
            "已经帮完博士的忙了，\x01",
            "我必须要早点回实验室了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #248
        0xFE,
        (
            "不能把温室交给蒂亚利\x01",
            "一个人照看呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #249
        0xFE,
        (
            "那么，再见啦，各位。\x01",
            "下次在蔡斯再见吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333F")

    TalkEnd(0xD)
    Return()

    # Function_8_2DC7 end

    def Function_9_3343(): pass

    label("Function_9_3343")

    TalkBegin(0xE)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #250
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xE)
    Return()

    # Function_9_3343 end

    def Function_10_3359(): pass

    label("Function_10_3359")

    Call(0, 4)
    Return()

    # Function_10_3359 end

    def Function_11_335E(): pass

    label("Function_11_335E")

    Call(0, 6)
    Return()

    # Function_11_335E end

    def Function_12_3363(): pass

    label("Function_12_3363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3532")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3448")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33E6")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #251
        0x103,
        (
            "#020F通过这里就是柏斯地区了啊。\x02\x03",

            "接下来要去的应该是蔡斯地区。\x01",
            "还是乘坐定期船去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3445")

    label("loc_33E6")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #252
        0x103,
        (
            "#020F通过这里就是柏斯地区了啊。\x02\x03",

            "接下来要去的应该是蔡斯地区。\x01",
            "还是乘坐定期船去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3445")

    Jump("loc_3514")

    label("loc_3448")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3514")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B9")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #253
        0x106,
        (
            "#050F前方就是柏斯地区了啊。\x02\x03",

            "接下来要去的应该是蔡斯地区。\x01",
            "还是去乘坐定期船吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3514")

    label("loc_34B9")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #254
        0x106,
        (
            "#050F前方就是柏斯地区了啊。\x02\x03",

            "接下来要去的应该是蔡斯地区。\x01",
            "还是去乘坐定期船吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3514")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Jump("loc_36FE")

    label("loc_3532")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_360B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A9")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #255
        0x103,
        (
            "#020F通过这里就是柏斯地区了啊。\x02\x03",

            "现在没时间去其它的地方了，\x01",
            "集中解决卢安的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3608")

    label("loc_35A9")

    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #256
        0x103,
        (
            "#020F通过这里就是柏斯地区了啊。\x02\x03",

            "现在没时间去其它的地方了，\x01",
            "集中解决卢安的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3608")

    Jump("loc_36E3")

    label("loc_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_36E3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3682")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #257
        0x106,
        (
            "#050F前方就是柏斯地区了啊。\x02\x03",

            "现在没时间去其它的地方了，\x01",
            "赶快集中精力解决卢安的工作！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E3")

    label("loc_3682")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #258
        0x106,
        (
            "#050F前方就是柏斯地区了啊。\x02\x03",

            "现在没时间去其它的地方了，\x01",
            "赶快集中精力解决卢安的工作！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E3")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_36FE")

    Return()

    # Function_12_3363 end

    def Function_13_36FF(): pass

    label("Function_13_36FF")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x380, 1)), scpexpr(EXPR_END)), "loc_3948")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3766")
    TurnDirection(0x108, 0x0, 400)

    ChrTalk(    #259
        0x108,
        (
            "#070F嗯，那边就是卢安了吗。\x02\x03",

            "也没什么事要去那边，\x01",
            "还是赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_3766")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_37C3")
    TurnDirection(0x109, 0x0, 400)

    ChrTalk(    #260
        0x109,
        (
            "#1060F那边就是卢安了啊。\x02\x03",

            "也没什么特别的事要过去，\x01",
            "还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_37C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_382C")
    TurnDirection(0x104, 0x0, 400)

    ChrTalk(    #261
        0x104,
        (
            "#030F嗯，通过这里\x01",
            "就是卢安地区了。\x02\x03",

            "现在还没必要过去吧，\x01",
            "今天还是回去好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_382C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_388A")
    TurnDirection(0x105, 0x0, 400)

    ChrTalk(    #262
        0x105,
        (
            "#040F前方就是卢安地区了啊。\x02\x03",

            "也没什么重要的事，\x01",
            "今天还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_388A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_38E4")
    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #263
        0x106,
        (
            "#050F前边就是卢安地区了啊。\x02\x03",

            "也没什么事情，\x01",
            "今天还是回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3945")

    label("loc_38E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3945")
    TurnDirection(0x103, 0x0, 400)

    ChrTalk(    #264
        0x103,
        (
            "#020F前面就是卢安地区了啊。\x02\x03",

            "反正也没有什么事要过去，\x01",
            "不如早点回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3945")

    Jump("loc_3AC0")

    label("loc_3948")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 4)), scpexpr(EXPR_END)), "loc_3A00")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39AC")

    ChrTalk(    #265
        0x108,
        (
            "#070F嗯，那边就是卢安了吗。\x02\x03",

            "现在的当务之急是抓捕龙！\x01",
            "赶快去迷雾峡谷吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39FD")

    label("loc_39AC")

    TurnDirection(0x106, 0x0, 400)

    ChrTalk(    #266
        0x106,
        (
            "#050F前边就是卢安地区了啊。\x02\x03",

            "现在的首要任务是龙！\x01",
            "赶快去迷雾峡谷吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39FD")

    Jump("loc_3AC0")

    label("loc_3A00")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A5B")

    ChrTalk(    #267
        0x108,
        (
            "#070F喂，那边就是卢安地区了啊。\x02\x03",

            "现在没空去其他的地方了，\x01",
            "赶快回去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AC0")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A71")
    TurnDirection(0x106, 0x1, 400)
    Jump("loc_3A78")

    label("loc_3A71")

    TurnDirection(0x106, 0x0, 400)

    label("loc_3A78")


    ChrTalk(    #268
        0x106,
        (
            "#050F前边就是卢安地区了啊。\x02\x03",

            "现在没空去其他的地方了，\x01",
            "赶快回去吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC0")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_13_36FF end

    def Function_14_3ADC(): pass

    label("Function_14_3ADC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2F")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #269
        "\x07\x05好像是导力停止了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_3CED")

    label("loc_3B2F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #270
        "\x07\x05这是一台可供旅行者回复体力的导力器装置。\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CD2")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x32)
    OP_73(0x5)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 18440, 1000, 12120, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x5, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_3CD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3CEC")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_3CEC")

    Return()

    label("loc_3CED")

    Return()

    # Function_14_3ADC end

    SaveToFile()

Try(main)
