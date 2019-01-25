from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0300   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0300.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 24,
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
        '卡西乌斯',                             # 9
        '莱娜',                                 # 10
        '雪拉扎德',                             # 11
        '凯文神父',                             # 12
        '艾利兹街道方向',                       # 13
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
        'ED6_DT06/CH20161 ._CH',             # 00
        'ED6_DT07/CH02000 ._CH',             # 01
        'ED6_DT27/CH03740 ._CH',             # 02
        'ED6_DT26/CH20316 ._CH',             # 03
        'ED6_DT26/CH20339 ._CH',             # 04
        'ED6_DT26/CH20325 ._CH',             # 05
        'ED6_DT26/CH20317 ._CH',             # 06
        'ED6_DT26/CH20334 ._CH',             # 07
        'ED6_DT26/CH20319 ._CH',             # 08
        'ED6_DT26/CH20322 ._CH',             # 09
        'ED6_DT27/CH03780 ._CH',             # 0A
        'ED6_DT07/CH02000 ._CH',             # 0B
        'ED6_DT26/CH20239 ._CH',             # 0C
        'ED6_DT27/CH03080 ._CH',             # 0D
        'ED6_DT26/CH20240 ._CH',             # 0E
    )

    AddCharChipPat(
        'ED6_DT06/CH20161P._CP',             # 00
        'ED6_DT07/CH02000P._CP',             # 01
        'ED6_DT27/CH03740P._CP',             # 02
        'ED6_DT26/CH20316P._CP',             # 03
        'ED6_DT26/CH20339P._CP',             # 04
        'ED6_DT26/CH20325P._CP',             # 05
        'ED6_DT26/CH20317P._CP',             # 06
        'ED6_DT26/CH20334P._CP',             # 07
        'ED6_DT26/CH20319P._CP',             # 08
        'ED6_DT26/CH20322P._CP',             # 09
        'ED6_DT27/CH03780P._CP',             # 0A
        'ED6_DT07/CH02000P._CP',             # 0B
        'ED6_DT26/CH20239P._CP',             # 0C
        'ED6_DT27/CH03080P._CP',             # 0D
        'ED6_DT26/CH20240P._CP',             # 0E
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 4110,
        Z                   = -1000,
        Y                   = -46140,
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


    DeclEvent(
        X                   = -270,
        Y                   = 0,
        Z                   = -16990,
        Range               = 4310,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFC0CC,
        Unknown_18          = 0x0,
        Unknown_1C          = 14,
    )


    DeclActor(
        TriggerX            = -11800,
        TriggerZ            = 0,
        TriggerY            = 6720,
        TriggerRange        = 1000,
        ActorX              = -14930,
        ActorZ              = -2000,
        ActorY              = 9650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 27,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_206",          # 00, 0
        "Function_1_2FA",          # 01, 1
        "Function_2_3AF",          # 02, 2
        "Function_3_52C",          # 03, 3
        "Function_4_531",          # 04, 4
        "Function_5_906",          # 05, 5
        "Function_6_10E7",         # 06, 6
        "Function_7_11D4",         # 07, 7
        "Function_8_1497",         # 08, 8
        "Function_9_14B1",         # 09, 9
        "Function_10_14E6",        # 0A, 10
        "Function_11_151B",        # 0B, 11
        "Function_12_1575",        # 0C, 12
        "Function_13_1740",        # 0D, 13
        "Function_14_1785",        # 0E, 14
        "Function_15_2800",        # 0F, 15
        "Function_16_2830",        # 10, 16
        "Function_17_2C05",        # 11, 17
        "Function_18_2D6E",        # 12, 18
        "Function_19_2DF3",        # 13, 19
        "Function_20_303A",        # 14, 20
        "Function_21_30B8",        # 15, 21
        "Function_22_3124",        # 16, 22
        "Function_23_4059",        # 17, 23
        "Function_24_43AD",        # 18, 24
        "Function_25_450E",        # 19, 25
        "Function_26_52C9",        # 1A, 26
        "Function_27_5309",        # 1B, 27
        "Function_28_549A",        # 1C, 28
        "Function_29_5536",        # 1D, 29
        "Function_30_5588",        # 1E, 30
    )


    def Function_0_206(): pass

    label("Function_0_206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21F")
    SetChrFlags(0x9, 0x10)

    label("loc_21F")

    SetChrPos(0x9, -7530, 0, 2690, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_24D")
    OP_A3(0x10F0)
    Event(0, 6)
    Jump("loc_2F9")

    label("loc_24D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_25E")
    OP_A3(0x10F1)
    Event(0, 7)
    Jump("loc_2F9")

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_27D")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F2)
    Event(0, 12)
    Jump("loc_2F9")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_29C")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x10F3)
    Event(0, 16)
    Jump("loc_2F9")

    label("loc_29C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_2BB")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    OP_A3(0x10F4)
    Event(0, 22)
    Jump("loc_2F9")

    label("loc_2BB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D8")
    SetMapFlags(0x10000000)
    Event(0, 5)

    label("loc_2D8")

    Jump("loc_2F9")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_2F9")

    Return()

    # Function_0_206 end

    def Function_1_2FA(): pass

    label("Function_1_2FA")

    OP_16(0x2, 0xFA0, 0xFFFE17B8, 0xFFFDF878, 0x230003)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x305, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 7)), scpexpr(EXPR_END)), "loc_33F")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_354")

    label("loc_33F")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 3)), scpexpr(EXPR_END)), "loc_374")
    OP_64(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_374")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x2000000)

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_382")
    OP_43(0x101, 0x3, 0x0, 0xD)

    label("loc_382")

    OP_71(0x3, 0x4)
    OP_71(0x6, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x301, 5)), scpexpr(EXPR_END)), "loc_39A")
    OP_6F(0x7, 30)

    label("loc_39A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x340, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AE")
    OP_1B(0x0, 0x0, 0x1E)
    OP_82(0x80, 0x2)

    label("loc_3AE")

    Return()

    # Function_1_2FA end

    def Function_2_3AF(): pass

    label("Function_2_3AF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D4")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_516")

    label("loc_3D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3ED")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_516")

    label("loc_3ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_406")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_516")

    label("loc_406")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41F")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_516")

    label("loc_41F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_438")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_516")

    label("loc_438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_516")

    label("loc_451")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46A")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_516")

    label("loc_46A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_483")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_516")

    label("loc_483")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_516")

    label("loc_49C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B5")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_516")

    label("loc_4B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_516")

    label("loc_4CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E7")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_516")

    label("loc_4E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_500")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_516")

    label("loc_500")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_516")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_516")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52B")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_516")

    label("loc_52B")

    Return()

    # Function_2_3AF end

    def Function_3_52C(): pass

    label("Function_3_52C")

    Call(0, 23)
    Return()

    # Function_3_52C end

    def Function_4_531(): pass

    label("Function_4_531")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    SetChrPos(0x101, 1890, -1000, -18670, 0)
    SetChrPos(0x142, 3040, -1000, -20140, 0)
    OP_6D(1760, 6700, 2360, 0)
    OP_67(0, 9860, -10000, 0)
    OP_6B(3530, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    OP_C8(0x200, 0x46, "C_PLAC01._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)

    def lambda_5BB():
        OP_6D(990, 6700, -11410, 5000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5BB)

    def lambda_5D3():
        OP_67(0, 9860, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5D3)

    def lambda_5EB():
        OP_8E(0x101, 0x7BC, 0x0, 0xFFFFDE18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_5EB)

    def lambda_606():
        OP_8E(0x142, 0x97E, 0x0, 0xFFFFD922, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 1, lambda_606)
    Sleep(5000)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    Fade(1000)
    OP_6D(2550, 0, -8780, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    WaitChrThread(0x142, 0x0)
    WaitChrThread(0x142, 0x1)
    Sleep(1000)

    ChrTalk(    #0
        0x142,
        (
            "#1062F#4P嘿～\x01",
            "这里就是艾丝蒂尔的家吗？\x02\x03",

            "好漂亮的房子，而且\x01",
            "感觉真是温馨啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#008F#5P嘿嘿，真的吗？\x02\x03",

            "我和爸爸、妈妈……\x02\x03",

            "还有约修亚的回忆\x01",
            "都留存在这间屋子中呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x142,
        (
            "#1060F#4P是这样啊～～\x02\x03",

            "嗯，那么约修亚应该\x01",
            "已经回来了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#5P#006F嗯，肯定没错的。\x02\x03",

            "快进来吧！我来介绍你们俩认识！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A5():
        OP_8E(0x101, 0x7D9, 0x1C2, 0xFFFFF0A6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_7A5)

    def lambda_7C0():
        OP_6D(1750, 450, -4240, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7C0)

    def lambda_7D8():
        OP_67(0, 9500, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7D8)
    OP_62(0x142, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x142, 0x0)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_81D():
        OP_8E(0x101, 0x8DE, 0x1C2, 0xFFFFFA1A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 0, lambda_81D)
    Sleep(1200)

    def lambda_83D():
        OP_6D(1980, 0, -8680, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_83D)

    def lambda_855():
        OP_67(0, 9500, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_855)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)
    OP_63(0x142)
    Sleep(500)

    ChrTalk(    #4
        0x142,
        (
            "#1067F#4P虽然不知道他是个怎样的笨蛋… \x01",
            "但做出这么残酷的事……\x02\x03",

            "#1065F呼……真是过分。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8DA():
        OP_8E(0x142, 0x802, 0x1C2, 0xFFFFF150, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x142, 1, lambda_8DA)
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_531 end

    def Function_5_906(): pass

    label("Function_5_906")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_926")
    Call(0, 28)
    FadeToBright(0, 0)
    Call(0, 29)

    label("loc_926")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrPos(0x101, 1800, -1000, -27820, 0)
    SetChrPos(0x103, 2900, -1000, -27820, 0)
    SetChrPos(0xF8, 1700, -1000, -28820, 0)
    SetChrPos(0xF9, 2800, -1000, -28820, 0)
    OP_6D(5010, 0, 6710, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2980, 0)
    OP_6C(48000, 0)
    OP_6E(358, 0)

    def lambda_9C1():
        OP_6D(2660, 0, -15230, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C1)

    def lambda_9D9():
        OP_67(0, 9500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9D9)

    def lambda_9F1():
        OP_6B(1990, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_9F1)

    def lambda_A01():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A01)
    OP_C8(0x200, 0x46, "C_PLAC01._CH", 0x0, 0x7D0)
    FadeToBright(2000, 0)
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)

    def lambda_A43():
        OP_90(0xFE, 0x0, 0x0, 0x3138, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A43)
    Sleep(200)

    def lambda_A63():
        OP_90(0xFE, 0x0, 0x0, 0x3138, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A63)
    Sleep(200)

    def lambda_A83():
        OP_90(0xFE, 0x0, 0x0, 0x30D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 0, lambda_A83)
    Sleep(200)

    def lambda_AA3():
        OP_90(0xFE, 0x0, 0x0, 0x30D4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 0, lambda_AA3)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)

    ChrTalk(    #5
        0x101,
        (
            "#1015F#6P嗯……\x01",
            "这里的雾也很厉害啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B58")

    ChrTalk(    #6
        0x107,
        (
            "#560F哇……\x01",
            "这里就是姐姐的家吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x106,
        (
            "#051F那个大叔，还真会\x01",
            "挑选好住处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_B58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BC8")

    ChrTalk(    #8
        0x104,
        (
            "#033F这……\x01",
            "这里就是艾丝蒂尔的家吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x106,
        (
            "#051F那个大叔，还真会\x01",
            "挑选好住处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_BC8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C38")

    ChrTalk(    #10
        0x105,
        (
            "#048F啊……\x01",
            "这里就是艾丝蒂尔的家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x106,
        (
            "#051F那个大叔，还真会\x01",
            "挑选好住处啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_C38")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CB2")

    ChrTalk(    #12
        0x106,
        (
            "#051F呵……\x01",
            "这里就是大叔的家吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x108,
        (
            "#071F哈哈，和想象中的差不多，\x01",
            "感觉很温馨的房子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1E")

    ChrTalk(    #14
        0x107,
        (
            "#560F哇……\x01",
            "这里就是姐姐的家吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x104,
        (
            "#031F呼～一看就是个很有\x01",
            "情趣的家呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_D1E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D84")

    ChrTalk(    #16
        0x107,
        (
            "#560F哇……\x01",
            "这里就是姐姐的家吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x105,
        (
            "#041F呵呵……\x01",
            "看起来真不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_D84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFE")

    ChrTalk(    #18
        0x107,
        (
            "#560F哇……\x01",
            "这里就是姐姐的家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x108,
        (
            "#071F哈哈，和想象中的差不多，\x01",
            "感觉很温馨的房子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_DFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E6E")

    ChrTalk(    #20
        0x105,
        (
            "#048F啊……\x01",
            "这里就是艾丝蒂尔的家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x104,
        (
            "#031F呼～一看就是个很有\x01",
            "情趣的家呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_E6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EEC")

    ChrTalk(    #22
        0x104,
        (
            "#033F这……\x01",
            "这里就是艾丝蒂尔的家吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x108,
        (
            "#071F哈哈，和想象中的差不多，\x01",
            "感觉很温馨的房子啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F67")

    label("loc_EEC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F67")

    ChrTalk(    #24
        0x105,
        (
            "#048F啊……\x01",
            "这里就是艾丝蒂尔的家啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x108,
        (
            "#071F哈哈，和想象中的差不多，\x01",
            "感觉很温馨的房子啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F67")

    OP_8C(0x101, 180, 400)

    ChrTalk(    #26
        0x101,
        (
            "#1016F#5P嗯……\x01",
            "就是那样啦。\x02\x03",

            "#1011F好啦，我去泡茶给大家喝，\x01",
            "快点进来吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x103,
        (
            "#026F#2P茶就由我来泡吧。\x02\x03",

            "#027F你还是先去二楼阳台\x01",
            "看看比较好。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #28
        0x101,
        "#1004F#6P啊……为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x103,
        "#524F#2P看啊，都已经那样了。\x02",
    )

    CloseMessageWindow()

    def lambda_104D():
        OP_6D(2070, 0, 8140, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104D)

    def lambda_1065():
        OP_6C(9000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1065)

    def lambda_1075():
        OP_6B(2530, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1075)
    OP_8C(0x101, 0, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #30
        0x101,
        (
            "#1004F#1P啊……是吗。\x02\x03",

            "#1007F这么大的雾确实\x01",
            "会把房子都弄潮的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_906 end

    def Function_6_10E7(): pass

    label("Function_6_10E7")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6D(490, 6660, 350, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 420, 6700, 2930, 180)
    ClearChrFlags(0x101, 0x80)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_8E(0x101, 0x1A4, 0x1A2C, 0xFFFFFFC4, 0x7D0, 0x0)
    OP_8C(0x101, 225, 400)
    Sleep(500)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x1E)
    OP_23(0x6)

    def lambda_1195():
        OP_8F(0xFE, 0x262, 0x1A2C, 0x208, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1195)
    Sleep(500)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x7)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F3)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_10E7 end

    def Function_7_11D4(): pass

    label("Function_7_11D4")

    EventBegin(0x0)
    OP_22(0x1C2, 0x0, 0x64)
    OP_BB(0x0, 0x1, 0x0)
    AddParty(0x2, 0xF7, 0xFF)
    AddParty(0x6, 0xF8, 0xFF)
    AddParty(0x4, 0xF9, 0xFF)
    OP_6D(2280, 450, -2180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(38000, 0)
    OP_6E(280, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0x107, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrPos(0x101, 2110, 450, -1890, 180)
    SetChrPos(0x103, 2110, 450, -1890, 180)
    SetChrPos(0x107, 2110, 450, -1890, 180)
    SetChrPos(0x105, 2110, 450, -1890, 180)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(1000)
    OP_43(0x101, 0x1, 0x0, 0x8)
    Sleep(500)
    OP_43(0x103, 0x1, 0x0, 0x9)
    Sleep(500)
    OP_43(0x107, 0x1, 0x0, 0xA)
    Sleep(500)
    OP_43(0x105, 0x1, 0x0, 0xB)

    def lambda_131E():
        OP_6D(2060, 450, -5010, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_131E)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_23(0x1C2)

    ChrTalk(    #31
        0x101,
        (
            "#1004F#7P哇……\x01",
            "好像比昨天更厉害了呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x105,
        (
            "#043F#5P嗯……\x01",
            "雾确实更浓了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x107,
        (
            "#065F#5P不知道阿加特哥哥他们\x01",
            "是否还好……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1015F#7P嗯……是啊。\x02\x03",

            "虽然只是巡视，\x01",
            "不过还是有点担心呢……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x107, 400)

    ChrTalk(    #35
        0x103,
        (
            "#020F#6P这样的话，\x01",
            "我们赶快去协会看看吧！\x02\x03",

            "去问问昨夜\x01",
            "的情况吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1450():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1450)
    Sleep(50)

    def lambda_1463():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1463)
    Sleep(400)

    ChrTalk(    #36
        0x101,
        "#1006F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x181C)
    OP_28(0x90, 0x1, 0x800)
    OP_28(0x74, 0x4, 0x40)
    EventEnd(0x0)
    Return()

    # Function_7_11D4 end

    def Function_8_1497(): pass

    label("Function_8_1497")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x7E4, 0x1C2, 0xFFFFE89A, 0x7D0, 0x0)
    Return()

    # Function_8_1497 end

    def Function_9_14B1(): pass

    label("Function_9_14B1")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x820, 0x1C2, 0xFFFFF132, 0x7D0, 0x0)
    OP_8E(0xFE, 0x49C, 0x1C2, 0xFFFFEC78, 0x7D0, 0x0)
    OP_8C(0xFE, 226, 400)
    Return()

    # Function_9_14B1 end

    def Function_10_14E6(): pass

    label("Function_10_14E6")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x820, 0x1C2, 0xFFFFF132, 0x7D0, 0x0)
    OP_8E(0xFE, 0xB2C, 0x1C2, 0xFFFFEC78, 0x7D0, 0x0)
    OP_8C(0xFE, 136, 400)
    Return()

    # Function_10_14E6 end

    def Function_11_151B(): pass

    label("Function_11_151B")

    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x802, 0x1C2, 0xFFFFF25E, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Sleep(200)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x7ED, 0x1C2, 0xFFFFF060, 0x7D0, 0x0)
    Return()

    # Function_11_151B end

    def Function_12_1575(): pass

    label("Function_12_1575")

    EventBegin(0x0)
    OP_D6(0x0)
    OP_6D(3370, -1000, -30420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2990, -1000, -35620, 0)

    def lambda_15CD():
        OP_8E(0xFE, 0xCBC, 0xFFFFFC18, 0xFFFF83BE, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15CD)
    FadeToBright(4000, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #37
        0x101,
        "#1004F#6P啊……\x02",
    )

    CloseMessageWindow()

    def lambda_1611():
        OP_6D(3360, -1000, -18490, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1611)

    def lambda_1629():
        OP_67(0, 8000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1629)
    WaitChrThread(0x101, 0x1)
    Sleep(1000)
    Sleep(100)
    Fade(1000)
    OP_6D(3370, -1000, -30420, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #38
        0x101,
        "#1004F#6P这里是……我的家？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)
    Sleep(500)
    OP_8C(0x101, 270, 500)
    Sleep(500)
    OP_8C(0x101, 0, 400)
    Sleep(1000)

    ChrTalk(    #39
        0x101,
        (
            "#1015F#6P我……\x01",
            "应该在神秘森林才对…\x02\x03",

            "而且……\x01",
            "雾是什么时候散去的？\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1833)
    EventEnd(0x0)
    OP_1D(0xF)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x1)
    OP_43(0x101, 0x3, 0x0, 0xD)
    OP_1B(0x0, 0x0, 0x1E)
    Return()

    # Function_12_1575 end

    def Function_13_1740(): pass

    label("Function_13_1740")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1784")
    Sleep(2000)
    OP_22(0x11A, 0x0, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1784")

    label("loc_1758")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1784")
    Sleep(4000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1771")
    Jump("loc_1784")

    label("loc_1771")

    OP_22(0x11A, 0x0, 0x46)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1781")
    Jump("loc_1784")

    label("loc_1781")

    Jump("loc_1758")

    label("loc_1784")

    Return()

    # Function_13_1740 end

    def Function_14_1785(): pass

    label("Function_14_1785")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1792")
    Return()

    label("loc_1792")

    EventBegin(0x0)
    OP_A3(0x1)
    Fade(1000)
    SetChrPos(0x101, 1960, 0, -16680, 0)
    OP_6D(1440, 0, -16329, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_71(0x4, 0x4)
    OP_72(0x3, 0x4)
    OP_72(0x3, 0x20)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    SetChrChipByIndex(0x8, 3)
    SetChrSubChip(0x8, 2)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x800)
    SetChrPos(0x8, -8500, 0, -7490, 90)

    def lambda_1854():
        OP_6D(-8590, 0, -7270, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1854)

    def lambda_186C():
        OP_67(0, 5180, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_186C)

    def lambda_1884():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1884)
    OP_8C(0x101, 315, 400)
    WaitChrThread(0x101, 0x0)
    OP_99(0x8, 0x2, 0x0, 0x5DC)

    def lambda_18A9():
        OP_99(0x8, 0x0, 0x3, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_18A9)
    Sleep(200)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_22(0x11A, 0x0, 0x64)
    Sleep(300)
    WaitChrThread(0x8, 0x0)
    OP_99(0x8, 0x4, 0x8, 0x3E8)
    Sleep(500)

    ChrTalk(    #40
        0x8,
        "#085F#5P呼……真累啊。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x101, -1170, 0, -14210, 323)

    ChrTalk(    #41
        0x101,
        "#5P老、老爸……？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 9)

    def lambda_1949():
        OP_8E(0xFE, 0xFFFFEC5A, 0x0, 0xFFFFD4F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1949)

    def lambda_1964():
        OP_6D(-8160, 0, -7840, 2200)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1964)

    def lambda_197C():
        OP_6B(3050, 2200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_197C)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    OP_44(0x101, 0x3)

    ChrTalk(    #42
        0x8,
        (
            "#080F噢噢，艾丝蒂尔。\x02\x03",

            "怎么了？\x01",
            "竟然这么早就起床了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        "#1004F啊……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x8,
        (
            "#081F哈哈哈，我明白了。\x02\x03",

            "因为爸爸好久没回家了，\x01",
            "想和爸爸撒撒娇对不对？\x02\x03",

            "好啊！就像平时一样——\x01",
            "赶快扑到爸爸怀里来吧！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1019F别、别像哄小孩一样！\x02\x03",

            "#1007F平时总说什么忙不过来，\x01",
            "怎么忽然又放假了？\x02\x03",

            "#1009F要是早点告诉我\x01",
            "我也能多做点准备啊──\x02",
        )
    )

    CloseMessageWindow()
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)
    Sleep(500)
    SetChrPos(0x9, 2020, 450, -3650, 225)
    SetChrFlags(0x9, 0x40)
    ClearChrFlags(0x9, 0x80)

    NpcTalk(    #46
        0x9,
        "女性的声音",
        (
            "#1P哎呀哎呀。\x01",
            "一大清早就这么热闹啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0xBB8)

    def lambda_1B72():
        OP_6D(-3190, 450, -4810, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B72)

    def lambda_1B8A():
        OP_67(0, 4520, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B8A)

    def lambda_1BA2():
        OP_6B(3470, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BA2)

    def lambda_1BB2():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1BB2)
    TurnDirection(0x101, 0x9, 400)
    SetChrSubChip(0x8, 8)
    WaitChrThread(0x101, 0x0)
    Sleep(500)

    ChrTalk(    #47
        0x101,
        "#1004F#5P……………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x8,
        (
            "#084F#5P喔喔，是莱娜啊。\x02\x03",

            "#081F我正在砍柴，\x01",
            "艾丝蒂尔也醒了……\x02\x03",

            "我们父女两个正在\x01",
            "亲密地联络感情呢。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #49
        0x9,
        "女性",
        (
            "#866F#8P呵呵呵，是真的吗？\x02\x03",

            "可是我看艾丝蒂尔\x01",
            "好像一点都不情愿哦。\x02\x03",

            "#861F你要总这么乱来的话，\x01",
            "可是会被讨厌的哟……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #50
        0x8,
        "#086F#5P什、什么……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_1D31():
        OP_6D(-5460, 0, -9250, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D31)

    def lambda_1D49():
        OP_6C(319000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D49)
    Fade(250)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    OP_72(0x4, 0x4)
    OP_0D()
    ClearChrFlags(0x8, 0x800)
    SetChrFlags(0x8, 0x4)
    OP_8E(0x8, 0xFFFFE053, 0x0, 0xFFFFDA44, 0x9C4, 0x0)
    OP_8C(0x8, 90, 0)
    OP_8F(0x8, 0xFFFFE714, 0x0, 0xFFFFD59E, 0x9C4, 0x0)
    ClearChrFlags(0x8, 0x4)
    TurnDirection(0x8, 0x101, 400)
    OP_43(0x9, 0x0, 0x0, 0xF)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #51
        0x8,
        "#084F#5P喂、喂喂，艾丝蒂尔……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #52
        0x8,
        (
            "#084F#5P你不会真的讨厌\x01",
            "爸爸了吧！？\x02\x03",

            "#083F那个，虽然我经常因为工作\x01",
            "太忙回不了家……\x02\x03",

            "#082F爸爸可是这个世界上最疼爱\x01",
            "艾丝蒂尔的人啊！！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        "#1026F#6P等、等一下啦……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 0x0)

    NpcTalk(    #54
        0x9,
        "女性",
        (
            "#861F#4P呵呵呵……\x02\x03",

            "#866F这孩子只是因为好久没看到你，\x01",
            "有点不好意思了而已。\x02\x03",

            "对吧，艾丝蒂尔？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)
    Sleep(500)

    ChrTalk(    #55
        0x101,
        (
            "#1026F#5P那、那个……\x01",
            "难、难道你是……\x02\x03",

            "…………………………\x01",
            "………妈妈………？\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #56
        0x9,
        "女性",
        (
            "#866F#4P哎呀呀，真是个奇怪的孩子，\x02\x03",

            "难道把妈妈都忘掉了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1025F#5P啊……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_1D(0x53)
    Sleep(300)

    def lambda_1FC9():
        OP_6B(3190, 1000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1FC9)
    Fade(1000)
    OP_BB(0x0, 0x1, 0x44)
    OP_BD()
    OP_0D()
    Sleep(500)

    ChrTalk(    #58
        0x101,
        (
            "#297F#5P妈——妈妈……\x01",
            "真的是妈妈……\x02\x03",

            "呜呜呜呜……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x9,
        "#864F#4P哎……？\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #60
        0x101,
        "#298F#5P#4S妈妈———！！！\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    def lambda_2072():
        OP_6D(-4460, 0, -9250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2072)
    OP_8E(0x101, 0xFFFFF31C, 0x0, 0xFFFFD634, 0x1388, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x20)
    SetChrChipByIndex(0x9, 6)
    SetChrSubChip(0x9, 0)

    def lambda_20B7():
        OP_99(0x9, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20B7)
    OP_8F(0x9, 0xFFFFF4AC, 0x0, 0xFFFFD602, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #61
        0x9,
        (
            "#866F#4P哎呀呀……\x01",
            "怎么了？艾丝蒂尔。\x02\x03",

            "难道是做了恶梦了吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#298F#5P呜……呜呜……\x02\x03",

            "虽、虽然已经\x01",
            "记不太清了，可是……\x02\x03",

            "#297F我……做了好可怕的梦，\x01",
            "梦见妈妈……\x02\x03",

            "不知去了哪里……\x01",
            "……再也……没有回来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x9,
        (
            "#863F#4P是吗……\x02\x03",

            "#866F呵呵，已经没事了。\x01",
            "妈妈就在这里，\x02\x03",

            "哪里都不会去的。\x02\x03",

            "别再害怕啦，乖孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        "#299F#5P嗯……嗯……\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #65
        0x8,
        (
            "#083F#5P那个……\x02\x03",

            "爸爸一个人…\x01",
            "好寂寞啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x9,
        "#864F#4P啊，亲爱的，你还在这里啊？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x8,
        "#082F#5P莱娜，你太过分了啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        (
            "#861F#4P呵呵，开个玩笑而已。\x02\x03",

            "#866F……来，接住，亲爱的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x8,
        "#085F#5P嗯、嗯。\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x2, 0x0, 0x5DC)
    SetChrPos(0x101, -3400, 0, -10700, 90)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 2)
    SetChrSubChip(0x9, 0)
    OP_8F(0x101, 0xFFFFF18C, 0x0, 0xFFFFD634, 0x3E8, 0x0)
    OP_8E(0x8, 0xFFFFEB1A, 0x0, 0xFFFFD6D4, 0x3E8, 0x0)
    TurnDirection(0x101, 0x8, 400)
    Sleep(500)

    ChrTalk(    #70
        0x101,
        (
            "#299F#6P嘿……嘿嘿嘿。\x02\x03",

            "#291F早上好～爸爸！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23B7():
        OP_6D(-5460, 0, -9250, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_23B7)
    OP_8E(0x101, 0xFFFFED2C, 0x0, 0xFFFFD698, 0x1388, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 8)
    SetChrSubChip(0x8, 0)
    OP_8F(0x8, 0xFFFFEAB6, 0x0, 0xFFFFD6D4, 0xBB8, 0x0)

    def lambda_2410():
        OP_99(0x8, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2410)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #71
        0x8,
        (
            "#081F#5P噢！传得漂亮。\x02\x03",

            "好！爸爸今天要\x01",
            "陪艾丝蒂尔玩个够！\x01",
            "随便你要玩什么都可以～\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#293F#6P真的吗！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        (
            "#080F#5P那当然！男子汉卡西乌斯·布莱特\x01",
            "说过的话什么时候不算数了！\x02\x03",

            "就算是扮家家酒，\x01",
            "爸爸也会陪你玩！\x02",
        )
    )

    CloseMessageWindow()
    OP_99(0x8, 0x2, 0x0, 0x5DC)
    SetChrPos(0x101, -4920, 0, -10600, 270)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    OP_8F(0x101, 0xFFFFEE08, 0x0, 0xFFFFD6D4, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #74
        0x101,
        (
            "#290F#6P嗯……那么……\x02\x03",

            "#291F我就要……\x01",
            "去钓鱼！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x8,
        (
            "#081F#5P哦！不愧是我的女儿。\x01",
            "连爱好都这么棒。\x02\x03",

            "#084F……嗯，等一下，\x01",
            "钓鱼好像是男孩子玩的…\x02\x03",

            "还是玩扮家家酒比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        "#294F#6P不要！人家就要去钓鱼！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x8,
        "#083F#5P嗯……那好吧。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x9,
        (
            "#861F#4P呵呵，只要她喜欢\x01",
            "就随她的意吧。\x02\x03",

            "#866F不过，不管去玩什么……\x01",
            "还是先吃过早餐后\x01",
            "再去比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x8,
        "#084F#5P哦，说的对。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #80
        0x101,
        (
            "#293F#5P早餐吗！？\x02\x03",

            "#291F妈妈～～！\x01",
            "我的肚子都饿得在叫了！\x02\x03",

            "我也来帮你一起做吧！\x01",
            "这样可以快点吃到！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x8,
        (
            "#080F#5P嗯，那我就去\x01",
            "泡咖啡吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        (
            "#861F#4P呵呵，那可谢谢你们啦。\x02\x03",

            "#866F不过在那之前……\x01",
            "请先去把手洗干净吧？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_20(0xFA0)
    OP_0D()
    OP_21()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #83
        "\x07\x05──幸福的日子一天天过着。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_1D(0x75)
    Sleep(500)
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/T0310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1785 end

    def Function_15_2800(): pass

    label("Function_15_2800")

    OP_8E(0xFE, 0x758, 0x0, 0xFFFFDC2E, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF43E, 0x0, 0xFFFFD5EE, 0x7D0, 0x0)
    OP_8C(0xFE, 270, 0)
    Return()

    # Function_15_2800 end

    def Function_16_2830(): pass

    label("Function_16_2830")

    EventBegin(0x0)
    LoadEffect(0x0, "map\\\\mp071_01.eff")
    LoadEffect(0x1, "map\\\\mp071_02.eff")
    LoadEffect(0x2, "map\\\\mp071_03.eff")
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x101, -12380, -200, 7130, 304)
    SetChrPos(0x8, -13750, -200, 4230, 333)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x8, 5)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, -9360, -200, -1530, 314)
    SetChrChipByIndex(0x9, 2)
    ClearChrFlags(0x9, 0x80)
    OP_6D(-12910, -200, 5270, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(152000, 0)
    OP_6E(262, 0)

    def lambda_290C():

        label("loc_290C")

        OP_99(0x101, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_290C")

    QueueWorkItem2(0x101, 2, lambda_290C)

    def lambda_291F():

        label("loc_291F")

        OP_99(0x8, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_291F")

    QueueWorkItem2(0x8, 2, lambda_291F)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1500)
    PlayEffect(0x0, 0x1, 0xFF, -13700, -1800, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_9E(0x101, 0x0, 0x32, 0x12C, 0x3E8)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_29A5():

        label("loc_29A5")

        OP_99(0x101, 0x4, 0x5, 0x3E8)
        OP_48()
        Jump("loc_29A5")

    QueueWorkItem2(0x101, 2, lambda_29A5)
    OP_43(0x101, 0x3, 0x0, 0x11)
    Sleep(500)

    def lambda_29C4():

        label("loc_29C4")

        OP_99(0x8, 0x8, 0xB, 0x5DC)
        OP_48()
        Jump("loc_29C4")

    QueueWorkItem2(0x8, 2, lambda_29C4)
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_44(0x8, 0x2)
    Fade(500)

    def lambda_29FC():
        OP_96(0xFE, 0xFFFFCCF2, 0x0, 0x1022, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_29FC)
    ClearChrFlags(0x8, 0x4)
    Sleep(10)
    SetChrChipByIndex(0x8, 1)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x8, 0x1)
    OP_8E(0x8, 0xFFFFD1AC, 0xFFFFFF38, 0x13F6, 0x7D0, 0x0)
    OP_8E(0x8, 0xFFFFD062, 0xFFFFFF38, 0x18EC, 0x7D0, 0x0)
    OP_8C(0x8, 293, 400)
    Sleep(500)
    OP_44(0x101, 0x2)
    Sleep(1000)

    def lambda_2A70():
        OP_99(0xFE, 0x6, 0xE, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A70)
    OP_22(0x18, 0x0, 0x64)
    OP_44(0x101, 0x3)
    OP_82(0x1, 0x0)
    PlayEffect(0x2, 0x2, 0xFF, -13700, -1800, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0x101, 0x1)
    OP_62(0x8, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(100)
    OP_62(0x101, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    def lambda_2AF4():
        OP_6D(-11880, -200, 4500, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2AF4)

    def lambda_2B0C():
        OP_67(0, 8080, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B0C)

    def lambda_2B24():
        OP_6C(140000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2B24)
    OP_8E(0x9, 0xFFFFD18E, 0xFFFFFF38, 0xC44, 0x5DC, 0x0)
    TurnDirection(0x9, 0x101, 400)
    Sleep(500)
    TurnDirection(0x8, 0x9, 400)
    Sleep(200)
    OP_99(0x101, 0xE, 0x11, 0x3E8)
    Sleep(100)
    OP_62(0x101, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x9, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #84
        (
            "\x07\x05在父母的注视和陪伴下\x01",
            "在大自然中尽情嬉戏……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 19)
    Return()

    # Function_16_2830 end

    def Function_17_2C05(): pass

    label("Function_17_2C05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D6D")
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    PlayEffect(0x1, 0x1, 0xFF, -13700, -1700, 7500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    Jump("Function_17_2C05")

    label("loc_2D6D")

    Return()

    # Function_17_2C05 end

    def Function_18_2D6E(): pass

    label("Function_18_2D6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DF2")
    OP_8C(0x101, 338, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(200)
    OP_8C(0x101, 248, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(500)
    OP_8C(0x101, 248, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(200)
    OP_8C(0x101, 338, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(500)
    OP_8C(0x101, 338, 0)
    Sleep(200)
    OP_8C(0x101, 293, 0)
    Sleep(500)
    Jump("Function_18_2D6E")

    label("loc_2DF2")

    Return()

    # Function_18_2D6E end

    def Function_19_2DF3(): pass

    label("Function_19_2DF3")

    OP_6D(21780, 0, 200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(60000, 0)
    OP_6E(262, 0)
    SetChrPos(0x9, 20640, 0, -1190, 90)
    ClearChrFlags(0x9, 0x80)
    OP_72(0x6, 0x20)
    OP_72(0x6, 0x4)
    OP_6F(0x6, 1)
    OP_70(0x6, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x6, 1)
    OP_70(0x6, 0x2)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)
    OP_8F(0x9, 0x50A0, 0x0, 0xFFFFFDC6, 0x7D0, 0x0)
    OP_6F(0x6, 2)
    OP_70(0x6, 0x3)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)
    OP_8C(0x9, 45, 400)
    OP_8E(0x9, 0x50A0, 0x0, 0x320, 0x3E8, 0x0)
    OP_43(0x101, 0x0, 0x0, 0x14)
    OP_8C(0x9, 90, 400)

    def lambda_2EF5():
        OP_6D(19970, 0, 490, 4000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2EF5)

    def lambda_2F0D():
        OP_6C(50000, 4000)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2F0D)
    Sleep(400)
    OP_43(0x8, 0x0, 0x0, 0x15)
    Sleep(1000)

    def lambda_2F2E():

        label("loc_2F2E")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_2F2E")

    QueueWorkItem2(0x9, 1, lambda_2F2E)
    WaitChrThread(0x101, 0x0)
    OP_44(0x9, 0x1)
    OP_99(0x101, 0x10, 0x12, 0x3E8)
    Sleep(200)
    OP_8C(0x9, 90, 400)
    OP_6F(0x6, 3)
    OP_70(0x6, 0x4)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(500)
    OP_8F(0x9, 0x50A0, 0x0, 0x5C8, 0x7D0, 0x0)
    OP_6F(0x6, 4)
    OP_70(0x6, 0x5)
    OP_73(0x6)
    SetChrChipByIndex(0x9, 7)
    Sleep(500)
    SetChrChipByIndex(0x9, 2)
    Sleep(300)
    OP_8C(0x9, 180, 400)
    OP_62(0x9, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(2000)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #85
        "\x07\x05有时也会帮忙做家务……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 65535)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T0311   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_2DF3 end

    def Function_20_303A(): pass

    label("Function_20_303A")

    SetChrChipByIndex(0x101, 9)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrPos(0x101, 12520, 0, 350, 90)

    def lambda_306A():
        OP_8E(0xFE, 0x4F1A, 0x0, 0xFFFFFFC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_306A)

    def lambda_3085():

        label("loc_3085")

        OP_99(0xFE, 0x1, 0x7, 0x5DC)
        OP_48()
        Jump("loc_3085")

    QueueWorkItem2(0x101, 2, lambda_3085)
    Sleep(1300)
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    WaitChrThread(0x101, 0x1)
    OP_44(0x101, 0x2)
    SetChrSubChip(0x101, 0)
    Return()

    # Function_20_303A end

    def Function_21_30B8(): pass

    label("Function_21_30B8")

    SetChrChipByIndex(0x8, 9)
    SetChrSubChip(0x8, 8)
    ClearChrFlags(0x8, 0x4)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 12350, 0, 1350, 90)

    def lambda_30ED():
        OP_8E(0xFE, 0x4844, 0x0, 0x3AC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_30ED)

    def lambda_3108():

        label("loc_3108")

        OP_99(0xFE, 0x9, 0xF, 0x5DC)
        OP_48()
        Jump("loc_3108")

    QueueWorkItem2(0x8, 2, lambda_3108)
    WaitChrThread(0x8, 0x1)
    OP_44(0x8, 0x2)
    SetChrSubChip(0x8, 8)
    Return()

    # Function_21_30B8 end

    def Function_22_3124(): pass

    label("Function_22_3124")

    EventBegin(0x0)
    OP_6D(3070, 0, -13180, 0)
    OP_67(0, 7710, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 2590, 0, -13750, 180)
    SetChrPos(0xA, 2450, 0, -15050, 0)
    SetChrPos(0x9, 3100, 0, -12520, 180)
    SetChrPos(0x8, 1980, 0, -12580, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0xA, 10)
    SetChrSubChip(0xA, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #86
        0xA,
        (
            "#870F……那…\x01",
            "我这就回去啦。\x02\x03",

            "艾丝蒂尔。\x01",
            "等春天我再来找你玩哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#295F#5P呜……等一下嘛……\x02\x03",

            "难得才来一次，\x01",
            "为什么这么快就要走……\x02\x03",

            "再多住一两天\x01",
            "好不好嘛。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xA,
        (
            "#872F嗯～我当然也想\x01",
            "那样。\x02\x03",

            "可是戏班的各位都在等我回去呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        "#295F#5P喔——真是没意思。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "#861F#5P好啦～别耍小孩子脾气了。\x02\x03",

            "#866F雪拉，真是谢谢你了。\x02\x03",

            "为了陪艾丝蒂尔玩，\x01",
            "总是大老远特意跑来。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xA,
        (
            "#871F哪里～\x01",
            "我也很开心的啦。\x02\x03",

            "#875F而且莱娜阿姨做的料理，\x01",
            "美味得让我不想走呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x9,
        (
            "#861F#5P哎呀，还真会说话，\x01",
            "能让你喜欢，我也很高兴。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x8,
        (
            "#080F#5P以后一定要再来玩啊。\x02\x03",

            "#081F下次我会把珍藏的白兰地\x01",
            "拿出来和你一起喝！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xA,
        "#875F哇～！真的吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)
    Sleep(500)

    ChrTalk(    #95
        0x9,
        "#863F#3S#2P亲～爱～的～？\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #96
        0x8,
        "#083F#6P玩、玩笑而已啦。\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)
    OP_8C(0x8, 180, 400)

    ChrTalk(    #97
        0x9,
        (
            "#862F#5P雪拉你也不许酗酒哦！\x02\x03",

            "不管你酒量有多好，\x01",
            "毕竟现在才１２岁而已。\x02\x03",

            "等长大一点后\x01",
            "再喝就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xA,
        "#873F唉～可是～……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        "#861F#3S#5P雪～拉～？\x02",
    )

    CloseMessageWindow()
    OP_62(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #100
        0xA,
        (
            "#874F明、明……我明白了……\x02\x03",

            "不、不过我肯定\x01",
            "也喝不了酒的啦～\x02\x03",

            "团长自然是不用说，\x01",
            "姐姐管我也管得很严呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x9,
        (
            "#866F#5P呵呵，那样最好啦。\x02\x03",

            "#861F雪拉，\x01",
            "代我向戏班的各位问好哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "#080F#5P下次把大家都\x01",
            "带来玩吧。\x02\x03",

            "这个院子很大，\x01",
            "办个野餐会都没问题的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xA,
        (
            "#875F是！我会转告给大家的。\x02\x03",

            "#872F好了，就这样。艾丝蒂尔。\x01",
            "……你也要做个听话的好孩子哦！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#291F#5P嗯！！\x02\x03",

            "雪拉姐，拜拜啦！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 180, 400)

    def lambda_36F5():
        OP_6D(3430, -1000, -25690, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36F5)

    def lambda_370D():
        OP_8E(0xFE, 0xD34, 0xFFFFFC18, 0xFFFF79BE, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_370D)
    WaitChrThread(0xA, 0x1)
    SetChrFlags(0xA, 0x80)
    Fade(1000)
    OP_6D(2730, 0, -12880, 0)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #105
        0x9,
        (
            "#866F#5P呵呵……\x01",
            "以后可要寂寞了啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x8,
        (
            "#080F#5P好啦，她不是说了吗，\x01",
            "到了春天还会再来玩的。\x02\x03",

            "正好我也休假在家，\x01",
            "不如办个大型联欢会吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x9,
        "#861F呵呵，那当然好啦。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_8C(0x101, 0, 400)

    ChrTalk(    #108
        0x101,
        (
            "#290F爸爸～！妈妈～～！\x02\x03",

            "#291F我……\x01",
            "我想要个弟弟！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #109
        0x8,
        "#084F#5P什、什么！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x9,
        "#864F#5P哎呀……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x101,
        (
            "#295F雪拉姐只是偶尔\x01",
            "才能来找我玩……\x02\x03",

            "我想有个随时都可以\x01",
            "一起玩的弟弟！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x8,
        (
            "#083F#5P你、你这孩子啊……\x02\x03",

            "那种事可不是想要\x01",
            "就马上能有的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x9,
        (
            "#861F#5P呵呵呵……\x01",
            "艾丝蒂尔想要个弟弟吗？\x02\x03",

            "#860F可是呢～这个愿望我们也\x01",
            "不能向你保证会实现哦。\x02\x03",

            "因为这要看女神的安排了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x101,
        "#293F是那样吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x9,
        (
            "#866F#5P嗯，女神会在宁静的傍晚\x01",
            "悄悄地把小宝宝放在菜园里……\x02\x03",

            "然后爸爸和妈妈就可以\x01",
            "发现那个孩子。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        (
            "#290F是、是那样啊……\x02\x03",

            "#291F我就要……\x01",
            "那我要向女神祈愿！！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x9,
        (
            "#861F#5P呵呵，这样当然好……\x02\x03",

            "#866F只要艾丝蒂尔做个听话的好孩子，\x01",
            "女神说不定就会把小宝宝作为奖励\x01",
            "赐给我们呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        "#294F啊！那我一定要做个好孩子！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)
    Sleep(500)

    ChrTalk(    #119
        0x8,
        (
            "#080F#6P呼……\x01",
            "你还是那么会哄小孩啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #120
        0x9,
        (
            "#866F#2P呵呵，不要说得好像是\x01",
            "别人的事情一样。\x02\x03",

            "#861F你自己也要努力\x01",
            "才行啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0x8,
        (
            "#081F#6P嗯、嗯。\x02\x03",

            "好～～～那我们现在\x01",
            "就赶快回房间努力吧……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0x9,
        (
            "#863F#2P我是说在常识的范围内努力！\x02\x03",

            "#860F好了！我现在要去\x01",
            "准备晚饭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #123
        0x8,
        "#083F#6P……是。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x101,
        "#293F？？？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x9,
        (
            "#861F#2P呵呵呵，\x01",
            "那我这就要去厨房了。\x02\x03",

            "#866F你们现在\x01",
            "要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x8,
        "#080F#6P说的也是啊……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x8, 180, 400)
    Sleep(500)

    ChrTalk(    #127
        0x8,
        (
            "#081F#5P艾丝蒂尔，要和爸爸\x01",
            "一起去钓鱼吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x9, 180, 400)

    ChrTalk(    #128
        0x101,
        (
            "#290F呜……今天就算了。\x02\x03",

            "我想自己玩一会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x8,
        (
            "#084F#5P#3S（受打击——）#2S\x02\x03",

            "#083F真是没办法……\x01",
            "那我只能回书房看书去了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x9,
        (
            "#861F#5P呵呵，\x01",
            "被女儿抛弃了啊。\x02\x03",

            "#865F艾丝蒂尔，\x01",
            "玩的时候要注意安全哦。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x8,
        (
            "#080F#5P一个人玩的时候\x01",
            "一定不要靠近水池。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        "#291F是——\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    OP_8C(0x8, 0, 400)

    def lambda_3E4E():
        OP_6D(2040, 0, -9450, 4000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E4E)

    def lambda_3E66():
        OP_8E(0xFE, 0x780, 0x1C2, 0xFFFFF1F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E66)
    Sleep(200)
    OP_8C(0x9, 315, 400)

    def lambda_3E8D():
        OP_8E(0xFE, 0x76C, 0x0, 0xFFFFD8FA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E8D)
    WaitChrThread(0x9, 0x1)

    def lambda_3EAD():
        OP_8E(0xFE, 0x76C, 0x1C2, 0xFFFFECAA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3EAD)
    WaitChrThread(0x8, 0x1)
    OP_72(0x0, 0x10)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x3B)
    OP_73(0x0)

    def lambda_3EE3():
        OP_8E(0xFE, 0x8A2, 0x1C2, 0xFFFFFA4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3EE3)
    WaitChrThread(0x9, 0x1)
    Sleep(300)

    def lambda_3F08():
        OP_8E(0xFE, 0x8A2, 0x1C2, 0xFFFFFA4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3F08)
    WaitChrThread(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    WaitChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x0, 59)
    OP_70(0x0, 0x0)
    OP_23(0x6)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x0)
    OP_71(0x0, 0x10)
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_6D(2590, 0, -13750, 2000)
    OP_63(0x101)
    Sleep(600)

    ChrTalk(    #133
        0x101,
        (
            "#290F#5P……弟弟吗……\x02\x03",

            "#293F……………………………\x02\x03",

            "#295F为什么……\x01",
            "我的胸口会隐隐作痛……\x02\x03",

            "好像忘掉了……\x01",
            "什么…非常重要的东西……\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 500)
    Sleep(500)
    OP_8C(0x101, 270, 500)
    Sleep(500)
    OP_8C(0x101, 180, 500)
    Sleep(500)

    ChrTalk(    #134
        0x101,
        "#292F#5P……不把它找出来的话……\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1834)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_22_3124 end

    def Function_23_4059(): pass

    label("Function_23_4059")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x307, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43AC")
    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435C")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(-7910, 0, 2760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -8650, 0, 2630, 90)
    OP_0D()
    Sleep(200)

    ChrTalk(    #135
        0x9,
        (
            "#864F#5P嗯……\x02\x03",

            "剩下的洋葱… \x01",
            "我记得确实是放在这里啊……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#291F#6P妈妈！\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #137
        0x9,
        (
            "#861F#2P啊～艾丝蒂尔。\x02\x03",

            "#866F呵呵呵，怎么了？\x01",
            "是不是已经饿坏了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0x101,
        (
            "#290F#6P啊，不是。\x01",
            "肚子还不算太饿……\x02\x03",

            "只是想问妈妈\x01",
            "一点事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x9,
        "#864F#2P？\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #140
        "\x07\x05把寻找二楼储物室钥匙的事情告诉了妈妈。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    ChrTalk(    #141
        0x9,
        (
            "#864F#2P哎呀哎呀……\x01",
            "想去储物室探险吗？\x02\x03",

            "#863F嗯，那里面都是灰尘，\x01",
            "会把衣服弄脏的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#295F#6P唔……不能去吗？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x9,
        (
            "#860F#2P………………………\x02\x03",

            "#861F算啦，想去就去吧。\x02\x03",

            "#865F妈妈和爸爸的床边上\x01",
            "不是有个小柜子吗？\x02\x03",

            "钥匙就放在\x01",
            "最上边的抽屉里。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x101,
        "#291F#6P哇～谢谢妈妈！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x9, 90, 400)
    ClearChrFlags(0x9, 0x10)
    OP_A2(0x1837)
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Jump("loc_43A9")

    label("loc_435C")


    ChrTalk(    #145
        0x9,
        (
            "#865F妈妈和爸爸的床边上\x01",
            "不是有个小柜子吗？\x02\x03",

            "钥匙就放在\x01",
            "最上边的抽屉里。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A9")

    TalkEnd(0x9)

    label("loc_43AC")

    Return()

    # Function_23_4059 end

    def Function_24_43AD(): pass

    label("Function_24_43AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x3F9), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_43C3")
    Return()

    label("loc_43C3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43D4")
    Call(0, 25)
    Return()

    label("loc_43D4")

    SetMapFlags(0x80)
    OP_C2()
    OP_48()
    EventBegin(0x0)
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_22(0x11B, 0x0, 0x64)

    def lambda_43FE():

        label("loc_43FE")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_43FE")

    QueueWorkItem2(0x101, 2, lambda_43FE)
    Sleep(15000)
    OP_44(0x101, 0x2)
    OP_1D(0x75)
    Fade(500)
    SetChrSubChip(0x101, 8)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44B4")

    ChrTalk(    #146
        0x101,
        (
            "#290F声音很好听呢，不过……\x01",
            "似乎有些难吹啊。\x02\x03",

            "#296F可是，真奇怪啊……\x02\x03",

            "这个声音……\x01",
            "总觉得以前在哪里听过。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_A2(0x0)
    Jump("loc_4506")

    label("loc_44B4")


    ChrTalk(    #147
        0x101,
        (
            "#296F这声音……\x01",
            "以前在哪里听到过呢？\x02\x03",

            "就去那个地方吹吹看吧。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_0D()

    label("loc_4506")

    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_24_43AD end

    def Function_25_450E(): pass

    label("Function_25_450E")

    SetMapFlags(0x80)
    OP_C2()
    OP_48()
    EventBegin(0x0)
    OP_20(0x5DC)
    Fade(1000)
    SetChrPos(0x101, -5540, 3450, 2200, 270)
    OP_6D(-5540, 3450, 2200, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    def lambda_4576():
        OP_8E(0xFE, 0xFFFFE6A6, 0xD7A, 0x8B6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4576)

    def lambda_4591():
        OP_6D(-6490, 3450, 2230, 1200)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4591)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_20(0x5DC)
    OP_21()
    OP_22(0x11B, 0x0, 0x64)

    def lambda_45D3():

        label("loc_45D3")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_45D3")

    QueueWorkItem2(0x101, 2, lambda_45D3)
    Sleep(15000)
    OP_44(0x101, 0x2)
    Fade(500)
    SetChrSubChip(0x101, 8)
    OP_0D()
    Sleep(500)

    ChrTalk(    #148
        0x101,
        (
            "#295F嗯……\x01",
            "还是吹不好啊。\x02\x03",

            "#292F这只口琴还\x01",
            "真是气人啊。\x02\x03",

            "看起来很好吹，\x01",
            "但真吹起来却这么难。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #149
        (
            "\x07\x05比起你擅长的棒术，\x01",
            "我倒觉得这个简单多了……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #150
        "关键是集中力的问题。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #151
        0x101,
        "#293F啊……？！\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #152
        (
            "不过，真是首节奏很好的曲子。\x01",
            "旋律明快，却又有点悲伤的意境……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #153
        (
            "虽然其它的曲子也都不错，\x01",
            "不过我最喜欢的还是这首了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #154
        "对了……叫什么名字来的？\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(1500, 0)
    OP_0D()

    ChrTalk(    #155
        0x101,
        (
            "#292F……………………………\x02\x03",

            "啊……确实就是……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()
    OP_22(0x11C, 0x0, 0x64)

    def lambda_4812():

        label("loc_4812")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_4812")

    QueueWorkItem2(0x101, 2, lambda_4812)
    Sleep(20000)
    OP_44(0x101, 0x2)
    Fade(500)
    SetChrSubChip(0x101, 9)
    OP_0D()
    Sleep(500)

    ChrTalk(    #156
        0x101,
        (
            "#295F嗯嗯……不是那样的……\x02\x03",

            "#290F对了……\x01",
            "就是这种感觉……\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 12)
    SetChrSubChip(0x101, 0)
    OP_0D()

    def lambda_488F():
        OP_6B(2600, 15000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_488F)

    def lambda_489F():

        label("loc_489F")

        OP_99(0x101, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_489F")

    QueueWorkItem2(0x101, 2, lambda_489F)
    OP_1D(0x46)
    OP_1F(0x50, 0xC8)
    Sleep(10000)
    Fade(5000)
    OP_6D(-18140, 3450, 51220, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -18140, 3450, 51220, 264)
    OP_0D()
    LoadEffect(0x0, "map\\\\mp058_00.eff")
    Fade(2500)
    OP_9F(0x101, 0x0, 0x0, 0x0, 0x96, 0x0)
    SetChrChipByIndex(0x101, 14)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x9C4)
    OP_0D()
    OP_21()
    OP_44(0x101, 0x2)
    Sleep(1000)
    OP_99(0x101, 0x8, 0x9, 0x320)
    Sleep(500)
    Fade(500)
    SetChrSubChip(0x101, 10)
    OP_0D()
    Sleep(500)

    ChrTalk(    #157
        0x101,
        (
            "#1012F听到了吗……约修亚……\x02\x03",

            "『星之所在』……\x01",
            "我终于会吹了哦。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, -14330, 3450, 50770, 270)
    ClearChrFlags(0x9, 0x80)
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMessageWindowPos(300, 50, -1, -1)
    SetChrName("女性的声音")

    AnonymousTalk(    #158
        "\x07\x05呵呵，很好听的曲子啊。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x50)
    OP_BB(0x0, 0x1, 0x0)
    OP_BD()
    SetChrChipByIndex(0x101, 65535)

    def lambda_4A3F():
        OP_6D(-15800, 3450, 51080, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A3F)

    def lambda_4A57():
        OP_67(0, 8300, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A57)

    def lambda_4A6F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4A6F)
    OP_8C(0x101, 90, 300)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x9, 0x2)

    ChrTalk(    #159
        0x101,
        "#1025F#6P……妈妈……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #160
        0x9,
        (
            "\x07\x05#866F正确的说……\x01",
            "我并不是你的妈妈。\x02\x03",

            "而是由你的回忆所构建\x01",
            "出的一个虚拟存在体。\x02\x03",

            "到现在为止发生的全部事情\x01",
            "都只是你的一场梦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0x101,
        (
            "#1016F#6P是吗…\x02\x03",

            "#1025F可是，就算是在梦中，\x01",
            "妈妈也还是妈妈啊。\x02\x03",

            "和妈妈在一起的每一天……\x01",
            "我都非常幸福快乐。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x9,
        (
            "\x07\x05#861F呵呵……我也是呢。\x02\x03",

            "#860F不过……\x01",
            "你还是要回去对吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x101,
        (
            "#1012F#6P……嗯。\x02\x03",

            "#1017F现在的我，已经想起了\x01",
            "应该回去的地方……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x9,
        (
            "\x07\x05#863F嗯……\x02\x03",

            "#866F他是叫约修亚吧？\x02\x03",

            "呵呵呵～很帅气的\x01",
            "男孩子呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #165
        0x101,
        "#1013F#6P妈、妈妈你真是的……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0x9,
        (
            "\x07\x05#861F哎呀～\x01",
            "小脸竟然变得通红。\x02\x03",

            "#866F呵呵……真是不可思议啊……\x02\x03",

            "我虽然不是真正的莱娜，\x01",
            "但现在却感到非常欣慰……\x02\x03",

            "我的小艾丝蒂尔现在已经\x01",
            "是一个可靠的大人了……\x02\x03",

            "而且还那么认真地在恋爱……\x02\x03",

            "#861F身为母亲……\x01",
            "没有比这个更值得高兴的了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #167
        0x101,
        (
            "#1026F#6P……妈妈……\x02\x03",

            "#1027F我……我……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x9,
        (
            "\x07\x05#866F好了啦！\x01",
            "那种表情可是不行的哦！\x02\x03",

            "你不是都已经想起应该\x01",
            "回去的地方了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 7)

    def lambda_4E31():
        OP_6D(-13040, 3450, 52280, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E31)

    def lambda_4E49():
        OP_67(0, 3380, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4E49)

    def lambda_4E61():
        OP_6C(71000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_4E61)

    def lambda_4E71():
        OP_6E(500, 4000)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4E71)

    def lambda_4E81():
        OP_6B(1870, 4000)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_4E81)
    Sleep(1000)
    PlayEffect(0x0, 0x0, 0xFF, -8090, 4000, 54040, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x11D, 0x1, 0x46)
    WaitChrThread(0x101, 0x1)
    Sleep(500)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    OP_8C(0x9, 306, 0)

    ChrTalk(    #169
        0x9,
        (
            "\x07\x05#863F#2P这场梦已经结束了……\x02\x03",

            "那里就是通往现实世界\x01",
            "的出口。\x02\x03",

            "#866F好孩子……\x01",
            "挺起你的胸，向前去吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x101,
        "#1025F#6P嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 102, 400)
    Sleep(500)

    ChrTalk(    #171
        0x101,
        (
            "#1016F#6P嘿嘿嘿，其实…我还想再吃一次\x01",
            "妈妈做的煎蛋卷呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0x9,
        (
            "\x07\x05#864F#2P哎呀呀……\x02\x03",

            "#860F傻孩子，要是想吃的话\x01",
            "可以自己试着去做啊。\x02\x03",

            "你做出来的味道，\x01",
            "肯定会和我做的一样。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0x101,
        "#1004F#6P啊……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0x9,
        (
            "\x07\x05#861F#2P家的味道…\x01",
            "孩子是可以从妈妈身上继承的。\x02\x03",

            "就算是没有亲身教导过，\x01",
            "但一样也可以完全继承下来。\x02\x03",

            "#866F我想你早就已经…\x01",
            "将那种味道继承下来了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0x101,
        (
            "#1025F#6P是吗……\x02\x03",

            "……………………………\x02\x03",

            "#1012F嗯，听妈妈这么一说，\x01",
            "我总算是放心了。\x02\x03",

            "#1017F那么，妈妈……\x01",
            "我，这就要走了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x9,
        (
            "\x07\x05#861F#2P嗯，别忘了替我向你爸爸\x01",
            "和约修亚问好。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0x101,
        (
            "#1017F#6P嗯！\x02\x03",

            "#1018F再见了……妈妈！\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 70, 400)
    Sleep(500)

    def lambda_51CC():
        OP_6D(-9890, 3450, 53440, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_51CC)
    OP_43(0x101, 0x1, 0x0, 0x1A)
    Sleep(500)

    def lambda_51F0():

        label("loc_51F0")

        TurnDirection(0xFE, 0x101, 400)
        OP_48()
        Jump("loc_51F0")

    QueueWorkItem2(0x9, 3, lambda_51F0)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    Sleep(500)
    OP_82(0x0, 0x2)
    OP_24(0x11D, 0x3C)
    Sleep(300)
    OP_24(0x11D, 0x32)
    Sleep(300)
    OP_24(0x11D, 0x28)
    Sleep(300)
    OP_24(0x11D, 0x1E)
    Sleep(300)
    OP_24(0x11D, 0x14)
    Sleep(300)
    OP_24(0x11D, 0xA)
    Sleep(300)
    OP_23(0x11D)

    def lambda_524C():
        OP_6D(-11020, 3450, 52690, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_524C)
    WaitChrThread(0x101, 0x2)
    Sleep(500)

    ChrTalk(    #178
        0x9,
        (
            "\x07\x05#866F#6P再见……#1480W #20W \x01",
            "#861F我可爱的艾丝蒂尔。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(3000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_44(0x101, 0x1)
    ClearMapFlags(0x2000000)
    OP_D6(0x1)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C0303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_25_450E end

    def Function_26_52C9(): pass

    label("Function_26_52C9")

    OP_8E(0xFE, 0xFFFFD6FC, 0xD7A, 0xD066, 0x1388, 0x0)

    def lambda_52E3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_52E3)
    OP_8E(0xFE, 0xFFFFE066, 0xD7A, 0xD318, 0x1388, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_26_52C9 end

    def Function_27_5309(): pass

    label("Function_27_5309")

    EventBegin(0x1)

    ChrTalk(    #179
        0x101,
        "#1001F这里好像可以钓上什么来。\x02",
    )

    CloseMessageWindow()

    def lambda_5335():
        OP_6D(-12120, 0, 6790, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5335)

    def lambda_534D():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_534D)

    def lambda_535D():
        OP_6C(0, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_535D)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #180
        "\x07\x05钓鱼吗？\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "钓鱼\x01",      # 0
            "离开\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_548A")
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x5, 0xFFFFD008, 0x0, 0x19DC, 0x13B, 0xFFFFC478, 0xFFFFF95C, 0x2184)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_5484")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_547E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_547B")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x20)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #181
        (
            "\x07\x05将在布莱特家发现钓鱼场的事情\x01",
            "记录在游击士手册上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_547B")

    Jump("loc_5484")

    label("loc_547E")

    OP_28(0x73, 0x1, 0x2000)

    label("loc_5484")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_5499")

    label("loc_548A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5499")
    EventEnd(0x1)

    label("loc_5499")

    Return()

    # Function_27_5309 end

    def Function_28_549A(): pass

    label("Function_28_549A")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5517"),
        (1, "loc_551D"),
        (SWITCH_DEFAULT, "loc_5523"),
    )


    label("loc_5517")

    OP_A2(0x1200)
    Jump("loc_5523")

    label("loc_551D")

    OP_A2(0x1201)
    Jump("loc_5523")

    label("loc_5523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_5531")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_5535")

    label("loc_5531")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_5535")

    Return()

    # Function_28_549A end

    def Function_29_5536(): pass

    label("Function_29_5536")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    OP_C9(0x0, 0x4, 0x0, 0x2, 0xFF, 0xFF, 0x5, 0x3, 0x4, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_29_5536 end

    def Function_30_5588(): pass

    label("Function_30_5588")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x306, 4)), scpexpr(EXPR_END)), "loc_55DB")

    ChrTalk(    #182
        0x101,
        (
            "#290F一个人跑到外面\x01",
            "是不行的哦。\x02\x03",

            "趁还没有被责备之前\x01",
            "赶快回家吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5616")

    label("loc_55DB")


    ChrTalk(    #183
        0x101,
        (
            "#1011F……从家的方向\x01",
            "传来什么声响。\x02\x03",

            "（去确认一下看看吧）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5616")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_30_5588 end

    SaveToFile()

Try(main)
