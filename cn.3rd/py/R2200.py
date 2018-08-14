from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'R2200.x',
        MapIndex            = 101,
        MapDefaultBGM       = "ed60029",
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
        '卢西亚',                               # 9
        '库拉茨',                               # 10
        '玛诺利亚村方向',                       # 11
        '玛西亚孤儿院方向',                     # 12
        '卢安方向',                             # 13
        '目标用照相机',                         # 14
        '',                                     # 15
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
        'ED6_DT07/CH01070 ._CH',             # 00
        'ED6_DT07/CH01260 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01070P._CP',             # 00
        'ED6_DT07/CH01260P._CP',             # 01
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
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
        Direction           = 0,
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
        X                   = -139370,
        Z                   = -2020,
        Y                   = 15120,
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

    DeclNpc(
        X                   = -28630,
        Z                   = -1990,
        Y                   = 79340,
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

    DeclNpc(
        X                   = 7410,
        Z                   = -2000,
        Y                   = 29980,
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


    DeclEvent(
        X                   = -126380,
        Y                   = -2900,
        Z                   = 18770,
        Range               = -124520,
        Unknown_10          = 0xFA0,
        Unknown_14          = 0x2C60,
        Unknown_18          = 0x0,
        Unknown_1C          = 15,
    )


    DeclActor(
        TriggerX            = -114230,
        TriggerZ            = -6050,
        TriggerY            = 11770,
        TriggerRange        = 1000,
        ActorX              = -114730,
        ActorZ              = -6040,
        ActorY              = 12270,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21830,
        TriggerZ            = -2000,
        TriggerY            = 37790,
        TriggerRange        = 1500,
        ActorX              = -21830,
        ActorZ              = -800,
        ActorY              = 37790,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -18840,
        TriggerZ            = -2000,
        TriggerY            = 33860,
        TriggerRange        = 1500,
        ActorX              = -18840,
        ActorZ              = -500,
        ActorY              = 33860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -82860,
        TriggerZ            = -6070,
        TriggerY            = 8950,
        TriggerRange        = 1500,
        ActorX              = -82860,
        ActorZ              = -5570,
        ActorY              = 8950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -88900,
        TriggerZ            = -6050,
        TriggerY            = 6520,
        TriggerRange        = 1500,
        ActorX              = -88900,
        ActorZ              = -5500,
        ActorY              = 6520,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -96650,
        TriggerZ            = -5960,
        TriggerY            = 9640,
        TriggerRange        = 1500,
        ActorX              = -96650,
        ActorZ              = -5450,
        ActorY              = 9640,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -96730,
        TriggerZ            = -6100,
        TriggerY            = 14600,
        TriggerRange        = 1500,
        ActorX              = -96730,
        ActorZ              = -5600,
        ActorY              = 14600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -101200,
        TriggerZ            = -6000,
        TriggerY            = 11000,
        TriggerRange        = 1500,
        ActorX              = -101200,
        ActorZ              = -5500,
        ActorY              = 11000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54580,
        TriggerZ            = -1980,
        TriggerY            = 13860,
        TriggerRange        = 1500,
        ActorX              = -54580,
        ActorZ              = -980,
        ActorY              = 13860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2DE",          # 00, 0
        "Function_1_2DF",          # 01, 1
        "Function_2_3AE",          # 02, 2
        "Function_3_52B",          # 03, 3
        "Function_4_16D8",         # 04, 4
        "Function_5_1770",         # 05, 5
        "Function_6_1789",         # 06, 6
        "Function_7_1885",         # 07, 7
        "Function_8_1C1B",         # 08, 8
        "Function_9_1CC5",         # 09, 9
        "Function_10_1D98",        # 0A, 10
        "Function_11_1EA1",        # 0B, 11
        "Function_12_1F7C",        # 0C, 12
        "Function_13_2065",        # 0D, 13
        "Function_14_2152",        # 0E, 14
        "Function_15_2394",        # 0F, 15
        "Function_16_2451",        # 10, 16
        "Function_17_2496",        # 11, 17
    )


    def Function_0_2DE(): pass

    label("Function_0_2DE")

    Return()

    # Function_0_2DE end

    def Function_1_2DF(): pass

    label("Function_1_2DF")

    OP_16(0x2, 0xFA0, 0xFFFD21A0, 0xFFFE5638, 0x230026)
    OP_22(0x1C8, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_308")
    OP_6F(0x0, 0)
    Jump("loc_30F")

    label("loc_308")

    OP_6F(0x0, 60)

    label("loc_30F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_338")
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_B2(0x0, 0x0, 0x80)

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_347")
    OP_64(0x8, 0x1)

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_353")
    OP_B2(0x0, 0x0, 0x80)

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_END)), "loc_35E")
    OP_64(0x3, 0x1)

    label("loc_35E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_END)), "loc_369")
    OP_64(0x4, 0x1)

    label("loc_369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_END)), "loc_374")
    OP_64(0x5, 0x1)

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_END)), "loc_37F")
    OP_64(0x6, 0x1)

    label("loc_37F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_END)), "loc_38A")
    OP_64(0x7, 0x1)

    label("loc_38A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")
    OP_1B(0x2, 0x0, 0xE)
    OP_71(0x1, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x201, 0x0)
    ExitThread()

    label("loc_3AD")

    Return()

    # Function_1_2DF end

    def Function_2_3AE(): pass

    label("Function_2_3AE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D3")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_515")

    label("loc_3D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EC")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_515")

    label("loc_3EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_405")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_515")

    label("loc_405")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41E")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_515")

    label("loc_41E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_437")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_515")

    label("loc_437")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_450")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_515")

    label("loc_450")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_469")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_515")

    label("loc_469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_515")

    label("loc_482")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_515")

    label("loc_49B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_515")

    label("loc_4B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_515")

    label("loc_4CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E6")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_515")

    label("loc_4E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_515")

    label("loc_4FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_515")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_515")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_52A")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_515")

    label("loc_52A")

    Return()

    # Function_2_3AE end

    def Function_3_52B(): pass

    label("Function_3_52B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x14E, -107740, -6000, 11600, 300)
    SetChrPos(0x14F, -106440, -6000, 14040, 200)
    SetChrFlags(0x14E, 0x40)
    SetChrFlags(0x14F, 0x40)
    OP_6D(-105600, -5400, 11820, 0)
    OP_67(0, 6800, -10000, 0)
    OP_6B(2720, 0)
    OP_6C(306000, 0)
    OP_6E(282, 0)
    LoadEffect(0x0, "map\\\\evsepith.eff")
    FadeToBright(2000, 0)

    def lambda_5C3():
        OP_6B(2520, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5C3)
    OP_43(0x14E, 0x2, 0x0, 0x4)
    OP_43(0x14F, 0x2, 0x0, 0x5)
    OP_0D()
    WaitChrThread(0x15, 0x1)
    WaitChrThread(0x14E, 0x2)

    ChrTalk(    #0
        0x14E,
        (
            "#1716F……果然不行啊。\x01",
            "本来还觉得是个好主意呢……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(    #1
        0x14E,
        (
            "#1900F………………………\x02\x03",

            "（幸福之石……）\x02\x03",

            "#1719F（本来还想如果真的有，\x01",
            "  就送给老师当礼物的……）\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x14F, 0x2)

    def lambda_6B1():
        OP_6D(-105600, -5400, 11120, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_6B1)

    def lambda_6C9():
        OP_6B(2420, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6C9)

    def lambda_6D9():
        OP_8E(0xFE, 0xFFFE622C, 0xFFFFE890, 0x2EE0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_6D9)
    WaitChrThread(0x14F, 0x1)

    ChrTalk(    #2
        0x14F,
        (
            "#1733F玛丽，\x01",
            "你在想什么呢～？\x02\x03",

            "#1730F还是那石头的事～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x14E,
        "#1714F咦？　呃，嗯……\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 0, 500)
    Sleep(500)

    ChrTalk(    #4
        0x14E,
        (
            "#1718F我说啊，波利，\x01",
            "你觉得真的有幸福之石吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x14F,
        (
            "#1733F哎～？\x02\x03",

            "……玛丽\x01",
            "想得到幸福吗～？\x02",
        )
    )

    Jump("loc_7ED")

    label("loc_7ED")

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #6
        0x14E,
        (
            "#1714F哎呀，不是的。\x02\x03",

            "#1903F如果真的有，你不觉得很棒吗？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x14F,
        (
            "#1730F……………………\x02\x03",

            "#1732F幸福这种东西，到处都有啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x80, 0x0, 0x64)
    PlayEffect(0x0, 0x0, 0xFF, -108400, -5540, 9800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8C(0x14F, 200, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14F, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)

    ChrTalk(    #8
        0x14F,
        "#1733F玛丽，那是～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x14E,
        "#1714F咦……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x14E, 252, 400)
    Sleep(500)
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(1000)

    ChrTalk(    #10
        0x14E,
        (
            "#1714F是什么呢。\x01",
            "好像有东西在发光……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_99D():
        OP_6D(-108140, -5980, 10360, 1800)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_99D)

    def lambda_9B5():
        OP_6C(310000, 1800)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_9B5)

    def lambda_9C5():
        OP_8E(0xFE, 0xFFFE5C3C, 0xFFFFE8A4, 0x25F8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_9C5)
    Sleep(300)

    def lambda_9E5():
        OP_8E(0xFE, 0xFFFE5B4C, 0xFFFFE890, 0x2AF8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_9E5)
    WaitChrThread(0x14E, 0x1)
    WaitChrThread(0x14F, 0x1)
    WaitChrThread(0x15, 0x0)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #11
        "\x07\x00得到了\x07\x02金链子\x07\x00。\x02",
    )

    Jump("loc_A4D")

    label("loc_A4D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_82(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #12
        0x14E,
        (
            "#1900F金链子啊……\x01",
            "唔，\x01",
            "虽然确实很浪漫……\x02\x03",

            "不过只有链子而已。\x01",
            "这样还是没办法\x01",
            "当作礼物呢……\x02",
        )
    )

    Jump("loc_ADF")

    label("loc_ADF")

    CloseMessageWindow()
    Sleep(300)

    def lambda_AEB():
        TurnDirection(0xFE, 0x14F, 400)
        ExitThread()

    QueueWorkItem(0x14E, 2, lambda_AEB)
    Sleep(300)
    TurnDirection(0x14F, 0x14E, 300)
    Sleep(300)
    OP_8F(0x14E, 0xFFFE5B7E, 0xFFFFE89A, 0x2850, 0x3E8, 0x0)
    Sleep(400)

    ChrTalk(    #13
        0x14E,
        (
            "#1719F#6P给你，波利。\x01",
            "这是波利找到的嘛。\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x14E, 0xFFFE5C3C, 0xFFFFE8A4, 0x25F8, 0x3E8, 0x0)

    ChrTalk(    #14
        0x14E,
        (
            "#1710F虽然不能当礼物，\x01",
            "但还是很漂亮的东西呀。\x02\x03",

            "要好好保管哦？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x14F,
        (
            "#1730F……………………\x02\x03",

            "#1732F嗯，好的～！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(800)
    OP_62(0x14F, 0x0, 1600, 0x26, 0x27, 0xFA, 0x1)
    Sleep(500)
    OP_8C(0x14F, 50, 400)
    Sleep(500)

    ChrTalk(    #16
        0x14F,
        "#1733F啊～…………\x02",
    )

    CloseMessageWindow()
    OP_22(0x26, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x0, 0x1, 0xC8, 0x3)
    Sleep(500)
    OP_8C(0x14E, 50, 400)

    def lambda_C65():
        OP_6D(-106240, -5480, 19200, 4000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_C65)

    def lambda_C7D():
        OP_67(0, 7200, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C7D)

    def lambda_C95():
        OP_6B(2600, 4000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_C95)

    def lambda_CA5():
        OP_6C(306000, 4000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_CA5)

    def lambda_CB5():
        OP_6E(362, 4000)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_CB5)
    WaitChrThread(0x15, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0x10, -94410, -2000, 19980, 270)
    SetChrPos(0x11, -93280, -2000, 21020, 270)

    def lambda_D00():
        OP_8E(0xFE, 0xFFFE69AC, 0xFFFFF830, 0x4F4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_D00)
    Sleep(100)

    def lambda_D20():
        OP_8E(0xFE, 0xFFFE6EC0, 0xFFFFF830, 0x52BC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_D20)
    Sleep(2000)

    def lambda_D40():
        OP_8E(0xFE, 0xFFFE6380, 0xFFFFE890, 0x33F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_D40)

    def lambda_D5B():
        OP_8E(0xFE, 0xFFFE69FC, 0xFFFFE8CC, 0x3084, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_D5B)
    WaitChrThread(0x14F, 0x1)
    OP_8C(0x14F, 340, 400)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 340, 400)
    WaitChrThread(0x10, 0x1)

    ChrTalk(    #17
        0x14F,
        "#1732F#3S#2P是卢西亚～！\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 180, 400)
    Sleep(100)
    OP_8C(0x11, 180, 400)
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "啊，波利！\x01",
            "玛丽也在呀。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DF4():
        OP_6D(-106000, -5580, 18700, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_DF4)

    def lambda_E0C():
        OP_6B(2500, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_E0C)

    def lambda_E1C():
        OP_67(0, 6300, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_E1C)

    def lambda_E34():
        OP_8E(0xFE, 0xFFFE69C0, 0xFFFFF808, 0x4AB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E34)
    Sleep(100)

    def lambda_E54():
        OP_8F(0xFE, 0xFFFE6448, 0xFFFFE890, 0x3520, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_E54)

    def lambda_E6F():
        OP_8F(0xFE, 0xFFFE6AC4, 0xFFFFE8CC, 0x31B0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_E6F)
    Sleep(200)

    def lambda_E8F():
        OP_8E(0xFE, 0xFFFE6E98, 0xFFFFF830, 0x4C54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E8F)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x11, 0x1)

    NpcTalk(    #19
        0x11,
        "男人",
        (
            "#6P哟，这不是孤儿院那边的孩子吗。\x01",
            "在海滩上玩吗？\x02",
        )
    )

    Jump("loc_EF5")

    label("loc_EF5")

    CloseMessageWindow()

    ChrTalk(    #20
        0x14E,
        (
            "#1714F啊，是、是的！\x01",
            "我们收集了一点贝壳。\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #21
        0x11,
        "男人",
        "#6P是吗。\x02",
    )

    Jump("loc_F55")

    label("loc_F55")

    CloseMessageWindow()

    NpcTalk(    #22
        0x11,
        "男人",
        (
            "#6P玩耍是可以，\x01",
            "不过要小心魔兽哦。\x02",
        )
    )

    Jump("loc_F8F")

    label("loc_F8F")

    CloseMessageWindow()

    ChrTalk(    #23
        0x14E,
        (
            "#1710F嗯，没问题的。\x01",
            "今天好像都没出来……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x14F,
        (
            "#1730F#5P卢西亚\x01",
            "是出来干活的吗～？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        "#6P嗯，是啊～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#6P你不是知道嘛，\x01",
            "从今天开始玛诺利亚村要举办义卖会。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        (
            "#6P所以我要去卢安\x01",
            "张贴传单了～。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x14E,
        (
            "#1714F啊，是吗。\x01",
            "义卖会是今天开始啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x14F,
        "#1732F#5P波利很期待呢～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#6P嗯，很有趣的哦。\x02\x03",

            "要是方便的话，你们都要来哦★\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1122():
        OP_8E(0xFE, 0xFFFE6C40, 0xFFFFF830, 0x4BB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1122)
    WaitChrThread(0x10, 0x1)
    Sleep(500)

    ChrTalk(    #31
        0x10,
        "#6P好啦，快点快点！\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x2, 0x0, 0x6)
    Sleep(500)

    def lambda_1173():

        label("loc_1173")

        TurnDirection(0xFE, 0x10, 0)
        OP_48()
        Jump("loc_1173")

    QueueWorkItem2(0x14F, 2, lambda_1173)

    NpcTalk(    #32 op#A
        0x11,
        "男人",
        (
            "#6P#20A喂、喂！\x01",
            "别拉我啦！\x02",
        )
    )

    Jump("loc_11AF")

    label("loc_11AF")

    Sleep(2000)
    OP_56(0x0)
    WaitChrThread(0x10, 0x2)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    OP_44(0x14F, 0x2)
    OP_44(0x14E, 0x2)

    def lambda_11D3():
        OP_6D(-104740, -6020, 14260, 3000)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_11D3)

    def lambda_11EB():
        OP_67(0, 7200, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_11EB)

    def lambda_1203():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_1203)

    def lambda_1213():
        OP_6C(336000, 3000)
        ExitThread()

    QueueWorkItem(0x15, 3, lambda_1213)

    def lambda_1223():
        OP_6E(288, 3000)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_1223)
    WaitChrThread(0x15, 0x0)
    OP_62(0x14E, 0x0, 1600, 0x18, 0x1B, 0xC8, 0x2)
    Sleep(1600)
    OP_63(0x14E)

    ChrTalk(    #33
        0x14E,
        (
            "#1714F（……那个男人，\x01",
            "  好像是以前帮过我们的游击士吧。）\x02\x03",

            "#1712F（咦？　名字想不起来了……）\x02\x03",

            "#1900F（卡露娜姐姐，亚妮拉丝姐姐，\x01",
            "  唔，克鲁茨哥哥，还有……）\x02\x03",

            "（……………………？？）\x02",
        )
    )

    Sleep(1000)

    def lambda_1330():
        TurnDirection(0xFE, 0x14E, 400)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_1330)
    CloseMessageWindow()

    ChrTalk(    #34
        0x14F,
        (
            "#1732F#1P玛丽，\x01",
            "玛丽～！\x02",
        )
    )

    Jump("loc_1369")

    label("loc_1369")

    CloseMessageWindow()
    TurnDirection(0x14E, 0x14F, 400)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #35
        0x14E,
        (
            "#1714F哎……\x01",
            "……什么事，波利？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x14F,
        "#1731F#1P波利想去义卖会～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x14E,
        (
            "#1714F…………义卖会？\x02\x03",

            "#1718F啊，是玛诺利亚村的义卖会吧。\x02\x03",

            "#1900F嗯～，\x01",
            "说不定会有适合当礼物的东西……\x02\x03",

            "#1710F是啊，\x01",
            "那就去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14F,
        "#1732F#1P走吧走吧～。\x02",
    )

    CloseMessageWindow()

    def lambda_14A5():

        label("loc_14A5")

        TurnDirection(0xFE, 0x14F, 0)
        OP_48()
        Jump("loc_14A5")

    QueueWorkItem2(0x14E, 2, lambda_14A5)

    def lambda_14B6():
        OP_8E(0xFE, 0xFFFE712C, 0xFFFFE854, 0x3430, 0x1068, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_14B6)
    Sleep(400)
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)

    ChrTalk(    #39
        0x14E,
        "#1717F#3P……波、波利！\x02",
    )

    CloseMessageWindow()
    OP_44(0x14E, 0x2)

    def lambda_1510():
        OP_6D(-102480, -6020, 13720, 1500)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1510)

    def lambda_1528():
        OP_6C(320000, 1500)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_1528)

    def lambda_1538():

        label("loc_1538")

        TurnDirection(0xFE, 0x14E, 0)
        OP_48()
        Jump("loc_1538")

    QueueWorkItem2(0x14F, 2, lambda_1538)

    def lambda_1549():
        OP_8E(0xFE, 0xFFFE70C8, 0xFFFFE868, 0x31EC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1549)
    WaitChrThread(0x14E, 0x1)
    OP_8C(0x14E, 60, 400)
    Sleep(500)
    OP_44(0x14F, 0x2)

    ChrTalk(    #40
        0x14E,
        (
            "#1716F不要一个人\x01",
            "擅自走掉啦！\x02\x03",

            "#1710F一起去吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x14F,
        "#1732F#4P好～。\x02",
    )

    CloseMessageWindow()

    def lambda_15D8():
        OP_8E(0xFE, 0xFFFE717C, 0xFFFFE868, 0x3228, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_15D8)
    WaitChrThread(0x14E, 0x1)

    def lambda_15F8():
        OP_8E(0xFE, 0xFFFE988C, 0xFFFFE854, 0x3228, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_15F8)

    def lambda_1613():
        OP_8E(0xFE, 0xFFFE983C, 0xFFFFE854, 0x3430, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x14F, 1, lambda_1613)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6D(-88980, -5920, 11820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x14E, 0xFF)
    OP_44(0x14F, 0xFF)
    SetChrPos(0x14E, -88980, -5920, 11820, 0)
    SetChrPos(0x14F, -88980, -5920, 11820, 0)
    SetChrChipByIndex(0x14E, 65535)
    SetChrSubChip(0x14E, 0)
    SetChrChipByIndex(0x14F, 65535)
    SetChrSubChip(0x14F, 0)
    ClearChrFlags(0x14E, 0x40)
    OP_69(0x14E, 0x0)
    OP_A2(0x2F20)
    OP_B2(0x0, 0x0, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_3_52B end

    def Function_4_16D8(): pass

    label("Function_4_16D8")

    Sleep(1500)
    OP_8C(0x14E, 200, 400)
    Sleep(1000)
    OP_8C(0x14E, 90, 400)
    Sleep(500)

    def lambda_16FB():
        OP_8E(0xFE, 0xFFFE6A60, 0xFFFFE8E0, 0x2DDC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_16FB)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 50, 400)
    Sleep(800)
    OP_8C(0x14E, 130, 400)
    Sleep(1000)

    def lambda_1738():
        OP_8E(0xFE, 0xFFFE63E4, 0xFFFFE8A4, 0x29CC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14E, 1, lambda_1738)
    WaitChrThread(0x14E, 0x1)
    Sleep(500)
    OP_8C(0x14E, 120, 400)
    Sleep(1000)
    OP_8C(0x14E, 180, 400)
    Sleep(1000)
    Return()

    # Function_4_16D8 end

    def Function_5_1770(): pass

    label("Function_5_1770")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1788")
    TurnDirection(0xFE, 0x14E, 100)
    Sleep(100)
    Jump("Function_5_1770")

    label("loc_1788")

    Return()

    # Function_5_1770 end

    def Function_6_1789(): pass

    label("Function_6_1789")


    def lambda_178F():
        OP_8F(0xFE, 0xFFFE6858, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_178F)

    def lambda_17AA():
        OP_8F(0xFE, 0xFFFE6AB0, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_17AA)
    WaitChrThread(0x10, 0x1)
    Sleep(600)

    def lambda_17CF():
        OP_8F(0xFE, 0xFFFE6470, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_17CF)

    def lambda_17EA():
        OP_8F(0xFE, 0xFFFE66C8, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_17EA)
    WaitChrThread(0x10, 0x1)
    Sleep(600)

    def lambda_180F():
        OP_8F(0xFE, 0xFFFE6088, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_180F)

    def lambda_182A():
        OP_8F(0xFE, 0xFFFE62E0, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_182A)
    WaitChrThread(0x10, 0x1)
    Sleep(600)

    def lambda_184F():
        OP_8F(0xFE, 0xFFFE4968, 0xFFFFF830, 0x4BB4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_184F)

    def lambda_186A():
        OP_8F(0xFE, 0xFFFE4B70, 0xFFFFF830, 0x4C54, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_186A)
    WaitChrThread(0x10, 0x1)
    Return()

    # Function_6_1789 end

    def Function_7_1885(): pass

    label("Function_7_1885")

    SetMapFlags(0x20)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 2)), scpexpr(EXPR_END)), "loc_18C8")
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        "\x07\x05宝箱是空的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Jump("loc_1C12")

    label("loc_18C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_1AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1976")
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #43
        0x14E,
        (
            "#1714F这、这是……\x01",
            "…………宝箱！？\x02\x03",

            "里、里面有什么呢……\x02\x03",

            "#1712F难不成，\x01",
            "是波利躲在里面…………！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F45)

    label("loc_1976")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "打开看看\x01",      # 0
            "不打开\x01",        # 1
        )
    )

    Jump("loc_19B7")

    label("loc_19B7")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABC")

    ChrTalk(    #44
        0x14E,
        (
            "#1715F打、打开看看吧。\x01",
            "（紧张紧张）……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    Sleep(200)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05宝箱是空的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #46
        0x14E,
        "#1714F………………\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x14E,
        "#1717F#4S……真是捉弄人！#2S\x02",
    )

    OP_7C(0x0, 0x190, 0xBB8, 0xC8)
    CloseMessageWindow()
    OP_A2(0x2F1A)
    Jump("loc_1AE1")

    label("loc_1ABC")


    ChrTalk(    #48
        0x14E,
        "#1713F……真令人在意……\x02",
    )

    CloseMessageWindow()

    label("loc_1AE1")

    Jump("loc_1C12")

    label("loc_1AE4")

    OP_22(0x27, 0x0, 0x64)
    OP_62(0x14E, 0x0, 1600, 0x2, 0x7, 0xC8, 0x1)
    Sleep(1000)
    OP_63(0x14E)

    ChrTalk(    #49
        0x14E,
        "#1714F这、这是……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x14F,
        "#1732F是宝箱～。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x14E,
        (
            "#1712F打、打开看看吧。\x01",
            "（紧张紧张）……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #52
        "\x07\x05宝箱是空的。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_7C(0xC8, 0x96, 0xBB8, 0x1F4)

    ChrTalk(    #53
        0x14E,
        "#1717F#4S失望——！\x02",
    )


    ChrTalk(    #54
        0x14F,
        "#1733F#4S失望——！\x02",
    )

    OP_56(0x1)
    Sleep(1000)
    OP_59()
    OP_A2(0x2F1A)

    label("loc_1C12")

    ClearMapFlags(0x20)
    TalkEnd(0xFF)
    Return()

    # Function_7_1885 end

    def Function_8_1C1B(): pass

    label("Function_8_1C1B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #55
        "\x07\x05玛丽在沙子里寻找贝壳。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #56
        0x14E,
        (
            "#1713F唔，\x01",
            "没什么好看的呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1B)
    OP_64(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC1")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_1CC1")

    TalkEnd(0xFF)
    Return()

    # Function_8_1C1B end

    def Function_9_1CC5(): pass

    label("Function_9_1CC5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #57
        "\x07\x05玛丽在沙子里寻找贝壳。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #58
        0x14E,
        (
            "#1718F啊，漂亮的粉红色！\x02\x03",

            "#1716F……不过裂开了。\x01",
            "唉，好可惜……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1C)
    OP_64(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D94")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D94")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_1D94")

    TalkEnd(0xFF)
    Return()

    # Function_9_1CC5 end

    def Function_10_1D98(): pass

    label("Function_10_1D98")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #59
        "\x07\x05玛丽在沙子里寻找贝壳。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #60
        0x14E,
        (
            "#1712F这一带，\x01",
            "好像没什么好东西……\x02\x03",

            "#1900F……………………\x02\x03",

            "#1716F……幸福之石什么的，\x01",
            "不可能掉在这里吧～……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1D)
    OP_64(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9D")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_1E9D")

    TalkEnd(0xFF)
    Return()

    # Function_10_1D98 end

    def Function_11_1EA1(): pass

    label("Function_11_1EA1")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #61
        "\x07\x05玛丽在沙子里寻找贝壳。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #62
        0x14E,
        (
            "#1716F唔，这里只有垃圾。\x02\x03",

            "#1715F竟然乱扔烟头，\x01",
            "……这些大人真是不像话！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1E)
    OP_64(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F78")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_1F78")

    TalkEnd(0xFF)
    Return()

    # Function_11_1EA1 end

    def Function_12_1F7C(): pass

    label("Function_12_1F7C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #63
        "\x07\x05玛丽在沙子里寻找贝壳。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #64
        0x14E,
        (
            "#1710F……手感虽然还不错，\x01",
            "但是颜色实在不怎么样。\x02\x03",

            "#1900F要是颜色更明亮一些就好了……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F1F)
    OP_64(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2061")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2061")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 3)

    label("loc_2061")

    TalkEnd(0xFF)
    Return()

    # Function_12_1F7C end

    def Function_13_2065(): pass

    label("Function_13_2065")

    OP_8B(0x14F, 0xFFFF2ACC, 0x3624, 0x190)
    Sleep(500)

    ChrTalk(    #65
        0x14F,
        (
            "#1733F玛丽，这个～……\x02\x03",

            "#1732F当礼物怎么样？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x14E,
        (
            "#1714F嗯，这个嘛……\x02\x03",

            "#1710F虽然品味不错，\x01",
            "但是只有花朵的话，\x01",
            "院子里就有很多了。\x02\x03",

            "不能算是\x01",
            "很好的礼物呢。\x02",
        )
    )

    Jump("loc_2146")

    label("loc_2146")

    CloseMessageWindow()
    OP_A2(0x2F18)
    OP_64(0x8, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_13_2065 end

    def Function_14_2152(): pass

    label("Function_14_2152")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_END)), "loc_21EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_21BA")

    ChrTalk(    #67
        0x14E,
        (
            "#1713F得赶快找到波利才行……\x02\x03",

            "她会迷路\x01",
            "都是我的错……\x02",
        )
    )

    Jump("loc_21B6")

    label("loc_21B6")

    CloseMessageWindow()
    Jump("loc_21E7")

    label("loc_21BA")


    ChrTalk(    #68
        0x14E,
        (
            "#1713F波利好像\x01",
            "没到这边来……\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_21E7")

    Jump("loc_2344")

    label("loc_21EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 1)), scpexpr(EXPR_END)), "loc_224A")

    ChrTalk(    #69
        0x14E,
        (
            "#1710F古罗尼山道\x01",
            "不是这边吧。\x02\x03",

            "#1711F要从玛诺利亚村\x01",
            "往北边走才对！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_224A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 0)), scpexpr(EXPR_END)), "loc_22AB")

    ChrTalk(    #70
        0x14E,
        (
            "#1714F啊，这边是卢安方向呢。\x02\x03",

            "#1710F要去玛诺利亚村\x01",
            "得往反方向才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_22AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_END)), "loc_2344")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_22F0")

    ChrTalk(    #71
        0x14E,
        (
            "#1710F那片海滩\x01",
            "在去玛诺利亚村的路上吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2344")

    label("loc_22F0")


    ChrTalk(    #72
        0x14E,
        (
            "#1714F哦，\x01",
            "这边是卢安方向……\x02\x03",

            "#1710F那片海滩应该在反方向吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_2344")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, -5800, -2000, 30000, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4E)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_237A")
    SetChrPos(0x14F, -5800, -2000, 30000, 270)

    label("loc_237A")

    OP_6D(-7800, -2000, 30000, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_14_2152 end

    def Function_15_2394(): pass

    label("Function_15_2394")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_23D6")

    ChrTalk(    #73
        0x14E,
        (
            "#1710F这边是玛诺利亚村吧。\x01",
            "要去海滩才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_240F")

    label("loc_23D6")


    ChrTalk(    #74
        0x14E,
        (
            "#1714F啊，走过头了。\x01",
            "这边是玛诺利亚村吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_240F")

    OP_59()
    Fade(1000)
    SetChrPos(0x14E, -123000, -2060, 15120, 90)
    SetChrPos(0x14F, -123000, -2060, 15120, 90)
    OP_6D(-122820, -2060, 15120, 0)
    OP_0D()
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_15_2394 end

    def Function_16_2451(): pass

    label("Function_16_2451")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #75
        "\x07\x05北　玛西亚孤儿院\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_16_2451 end

    def Function_17_2496(): pass

    label("Function_17_2496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E3, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E4, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_250D")
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #76
        (
            "\x07\x05东　卢安市　　２３８塞尔矩\x01",
            "西　玛诺利亚村　７４塞尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Jump("loc_265B")

    label("loc_250D")


    ChrTalk(    #77
        0x14F,
        "#1733F玛丽，这个是～？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x14E,
        (
            "#1710F写着『卢安』呢。\x02\x03",

            "顺着这条道一直走，\x01",
            "就能到卢安市了吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x14F,
        "#1731F…………礼物。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x14E, 0x14F, 400)
    Sleep(300)

    ChrTalk(    #80
        0x14E,
        (
            "#1714F咦…………？\x02\x03",

            "你说把这个标志当礼物？\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x14E, 0x0, 1600, 0x28, 0x2B, 0x64, 0x2)
    Sleep(1500)

    ChrTalk(    #81
        0x14E,
        (
            "#1712F那、那还用说吗，\x01",
            "当然不行了！\x02\x03",

            "又不是克拉姆的\x01",
            "恶作剧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2F19)
    TalkEnd(0xFF)

    label("loc_265B")

    Return()

    # Function_17_2496 end

    SaveToFile()

Try(main)
