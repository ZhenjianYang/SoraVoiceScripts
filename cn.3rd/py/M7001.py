from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7001   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7001.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60220",
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
        '骸骨战士',                             # 9
        '骸骨战士',                             # 10
        '骸骨射手',                             # 11
        '封印石①',                             # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT27/CH04080 ._CH',             # 00
        'ED6_DT27/CH04150 ._CH',             # 01
        'ED6_DT26/CH20622 ._CH',             # 02
        'ED6_DT29/CH14400 ._CH',             # 03
        'ED6_DT29/CH14401 ._CH',             # 04
        'ED6_DT29/CH14410 ._CH',             # 05
        'ED6_DT29/CH14411 ._CH',             # 06
        'ED6_DT29/CH14404 ._CH',             # 07
        'ED6_DT29/CH14414 ._CH',             # 08
        'ED6_DT29/CH14420 ._CH',             # 09
        'ED6_DT29/CH14421 ._CH',             # 0A
        'ED6_DT29/CH14010 ._CH',             # 0B
        'ED6_DT29/CH14011 ._CH',             # 0C
        'ED6_DT29/CH14020 ._CH',             # 0D
        'ED6_DT26/CH20621 ._CH',             # 0E
        'ED6_DT29/CH14403 ._CH',             # 0F
        'ED6_DT29/CH14413 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT27/CH04080P._CP',             # 00
        'ED6_DT27/CH04150P._CP',             # 01
        'ED6_DT26/CH20622P._CP',             # 02
        'ED6_DT29/CH14400P._CP',             # 03
        'ED6_DT29/CH14401P._CP',             # 04
        'ED6_DT29/CH14410P._CP',             # 05
        'ED6_DT29/CH14411P._CP',             # 06
        'ED6_DT29/CH14404P._CP',             # 07
        'ED6_DT29/CH14414P._CP',             # 08
        'ED6_DT29/CH14420P._CP',             # 09
        'ED6_DT29/CH14421P._CP',             # 0A
        'ED6_DT29/CH14010P._CP',             # 0B
        'ED6_DT29/CH14011P._CP',             # 0C
        'ED6_DT29/CH14020P._CP',             # 0D
        'ED6_DT26/CH20621P._CP',             # 0E
        'ED6_DT29/CH14403P._CP',             # 0F
        'ED6_DT29/CH14413P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 31910,
        Z                   = -12000,
        Y                   = -23720,
        Unknown_0C          = 0,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35140,
        Z                   = -20000,
        Y                   = -24440,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17780,
        Z                   = -8000,
        Y                   = -9960,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 17820,
        Z                   = -24000,
        Y                   = -37930,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -4019,
        Z                   = -24000,
        Y                   = -9290,
        Unknown_0C          = 180,
        Unknown_0E          = 5,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2400,
        Z                   = -52000,
        Y                   = -72420,
        Unknown_0C          = 180,
        Unknown_0E          = 3,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x6B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9770,
        Z                   = -56000,
        Y                   = -120260,
        Unknown_0C          = 0,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x66,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 45680,
        Y                   = -61000,
        Z                   = -76530,
        Range               = 49490,
        Unknown_10          = 0xFFFF2928,
        Unknown_14          = 0xFFFEFA2A,
        Unknown_18          = 0x0,
        Unknown_1C          = 9,
    )

    DeclEvent(
        X                   = 4410,
        Y                   = -53000,
        Z                   = -101960,
        Range               = -380,
        Unknown_10          = 0xFFFF4480,
        Unknown_14          = 0xFFFE8F2C,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = -19850,
        Y                   = -53000,
        Z                   = -84720,
        Range               = -28180,
        Unknown_10          = 0xFFFF4868,
        Unknown_14          = 0xFFFED27A,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )


    DeclActor(
        TriggerX            = 60400,
        TriggerZ            = -60000,
        TriggerY            = -72100,
        TriggerRange        = 1000,
        ActorX              = 60400,
        ActorZ              = -59000,
        ActorY              = -72100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -46120,
        TriggerZ            = -52000,
        TriggerY            = -82000,
        TriggerRange        = 1500,
        ActorX              = -46120,
        ActorZ              = -49000,
        ActorY              = -82000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -37300,
        TriggerZ            = -20000,
        TriggerY            = -24130,
        TriggerRange        = 1000,
        ActorX              = -38000,
        ActorZ              = -19000,
        ActorY              = -24000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 30,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8700,
        TriggerZ            = -8000,
        TriggerY            = -10110,
        TriggerRange        = 1000,
        ActorX              = 8000,
        ActorZ              = -7000,
        ActorY              = -10000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 31,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -3720,
        TriggerZ            = -24000,
        TriggerY            = -7100,
        TriggerRange        = 1000,
        ActorX              = -4000,
        ActorZ              = -24000,
        ActorY              = -6000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 32,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_38A",          # 00, 0
        "Function_1_425",          # 01, 1
        "Function_2_5A8",          # 02, 2
        "Function_3_CE1",          # 03, 3
        "Function_4_1583",         # 04, 4
        "Function_5_15DF",         # 05, 5
        "Function_6_1640",         # 06, 6
        "Function_7_16A1",         # 07, 7
        "Function_8_24D6",         # 08, 8
        "Function_9_253D",         # 09, 9
        "Function_10_26A2",        # 0A, 10
        "Function_11_2744",        # 0B, 11
        "Function_12_2CBA",        # 0C, 12
        "Function_13_38E4",        # 0D, 13
        "Function_14_390F",        # 0E, 14
        "Function_15_393A",        # 0F, 15
        "Function_16_411E",        # 10, 16
        "Function_17_42B5",        # 11, 17
        "Function_18_4433",        # 12, 18
        "Function_19_44FB",        # 13, 19
        "Function_20_45A6",        # 14, 20
        "Function_21_4695",        # 15, 21
        "Function_22_4748",        # 16, 22
        "Function_23_47FB",        # 17, 23
        "Function_24_48D9",        # 18, 24
        "Function_25_4995",        # 19, 25
        "Function_26_4A51",        # 1A, 26
        "Function_27_4B0D",        # 1B, 27
        "Function_28_4BC9",        # 1C, 28
        "Function_29_4CDF",        # 1D, 29
        "Function_30_4D2D",        # 1E, 30
        "Function_31_4E53",        # 1F, 31
        "Function_32_4F79",        # 20, 32
    )


    def Function_0_38A(): pass

    label("Function_0_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A4")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_3C8"),
        (101, "loc_3CF"),
        (102, "loc_3D6"),
        (103, "loc_3DD"),
        (SWITCH_DEFAULT, "loc_3E4"),
    )


    label("loc_3C8")

    Event(0, 20)
    Jump("loc_3E4")

    label("loc_3CF")

    Event(0, 21)
    Jump("loc_3E4")

    label("loc_3D6")

    Event(0, 22)
    Jump("loc_3E4")

    label("loc_3DD")

    Event(0, 23)
    Jump("loc_3E4")

    label("loc_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_411")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 7)), scpexpr(EXPR_END)), "loc_401")
    Event(0, 19)
    Jump("loc_40E")

    label("loc_401")

    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_40E")

    Jump("loc_424")

    label("loc_411")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_424")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_424")

    Return()

    # Function_0_38A end

    def Function_1_425(): pass

    label("Function_1_425")

    OP_16(0x2, 0xFA0, 0xFFFE5444, 0xFFFD1DB8, 0x23007D)
    OP_C0(0x1E, 0x2, 0x1, 0xFA0A22E8, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_479")
    OP_1B(0x0, 0x0, 0x18)
    OP_1B(0x1, 0x0, 0x19)
    OP_1B(0x2, 0x0, 0x1A)
    OP_1B(0x3, 0x0, 0x1B)

    label("loc_479")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_535")
    ClearChrFlags(0x13, 0x80)
    OP_9F(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 60400, -59000, -72100, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x13, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_539")

    label("loc_535")

    OP_64(0x0, 0x1)

    label("loc_539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 5)), scpexpr(EXPR_END)), "loc_546")
    OP_71(0x404, 0x0)
    ExitThread()

    label("loc_546")

    OP_82(0x85, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x1, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_559")
    OP_82(0x86, 0x0)
    Jump("loc_55C")

    label("loc_559")

    OP_82(0x87, 0x0)

    label("loc_55C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_56E")
    OP_6F(0x0, 0)
    Jump("loc_575")

    label("loc_56E")

    OP_6F(0x0, 60)

    label("loc_575")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_587")
    OP_6F(0x1, 0)
    Jump("loc_58E")

    label("loc_587")

    OP_6F(0x1, 60)

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A0")
    OP_6F(0x2, 0)
    Jump("loc_5A7")

    label("loc_5A0")

    OP_6F(0x2, 60)

    label("loc_5A7")

    Return()

    # Function_1_425 end

    def Function_2_5A8(): pass

    label("Function_2_5A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 82750, -8000, -23510, 270)
    SetChrPos(0x10F, 83090, -8000, -24830, 270)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(82380, -8000, -23400, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(4400, 0)
    OP_6C(315000, 0)
    OP_6E(209, 0)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    Sleep(1000)

    def lambda_657():
        OP_6B(3800, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_657)
    FadeToBright(2000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 82870, -8000, -24100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Sleep(200)

    def lambda_6C8():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6C8)

    def lambda_6DA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_6DA)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(1000)

    def lambda_6FB():
        OP_8E(0xFE, 0x13330, 0xFFFFE0C0, 0xFFFFA39E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6FB)
    Sleep(300)

    def lambda_71B():
        OP_8E(0xFE, 0x135CE, 0xFFFFE0C0, 0xFFFF9D54, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_71B)
    OP_6D(78070, -8000, -23700, 1500)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    Sleep(500)

    ChrTalk(    #0
        0x109,
        "#1079F#5P这里是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        (
            "#1443F的确……\x01",
            "好像是『入口』呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0xDC)

    def lambda_7AB():
        OP_6D(57610, -7450, -24140, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7AB)

    def lambda_7C3():
        OP_67(0, 5640, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7C3)

    def lambda_7DB():
        OP_6B(7160, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7DB)

    def lambda_7EB():
        OP_6C(292000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7EB)

    def lambda_7FB():
        OP_6E(537, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_7FB)
    StopSound(0x1F018, 0x2B750, 0x1388)
    OP_C8(0x200, 0x46, "C_PLAC32._CH", 0x0, 0xBB8)
    WaitChrThread(0x109, 0x2)
    Sleep(1000)
    Fade(500)
    OP_6D(78070, -8000, -23700, 0)
    OP_67(0, 6810, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(315000, 0)
    OP_6E(209, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0xEE48, 0x27CB8, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #2
        0x109,
        (
            "#1063F#5P还是这样\x01",
            "奇怪的异空间吗……\x02\x03",

            "看来前路还很漫长啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1802F嗯……\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x10F,
        "#1441F凯文……！\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    LoadEffect(0x1, "map\\mp309_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, 71650, -7400, -23580, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0xFF, 71720, -7400, -25780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xFF, 70040, -7400, -24510, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x137, 0x0, 0x64)

    def lambda_A07():
        OP_6D(74350, -8000, -23480, 1600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A07)

    def lambda_A1F():
        OP_67(0, 5530, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A1F)

    def lambda_A37():
        OP_6B(3800, 1600)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A37)

    def lambda_A47():
        OP_6C(315000, 1600)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A47)

    def lambda_A57():
        OP_6E(229, 1600)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A57)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 71650, -8000, -23580, 90)
    SetChrPos(0x11, 71720, -8000, -25780, 90)
    SetChrPos(0x12, 70040, -8000, -24510, 90)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_AD4():

        label("loc_AD4")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AD4")

    QueueWorkItem2(0x10, 3, lambda_AD4)
    Sleep(30)

    def lambda_AEC():

        label("loc_AEC")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_AEC")

    QueueWorkItem2(0x11, 3, lambda_AEC)
    Sleep(30)

    def lambda_B04():

        label("loc_B04")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B04")

    QueueWorkItem2(0x12, 3, lambda_B04)

    def lambda_B17():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B17)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x2)
    Sleep(100)

    def lambda_B36():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B36)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x1, 0x2)
    Sleep(100)

    def lambda_B55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B55)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x2, 0x2)
    OP_23(0x137)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_1D(0x97)
    Sleep(1000)

    ChrTalk(    #5
        0x109,
        "#1069F这些家伙……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        "#1802F#6P魔、魔兽……？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x10)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    Sleep(300)

    def lambda_C10():
        OP_6D(76160, -8000, -23500, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C10)

    def lambda_C28():
        OP_67(0, 6030, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C28)

    def lambda_C40():
        OP_6B(3250, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C40)
    SetChrChipByIndex(0x10, 4)

    def lambda_C55():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_C55)
    Sleep(30)
    SetChrChipByIndex(0x11, 4)

    def lambda_C7A():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_C7A)
    Sleep(30)
    SetChrChipByIndex(0x12, 6)

    def lambda_C9F():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_C9F)
    WaitChrThread(0x109, 0x1)
    WaitChrThread(0x109, 0x2)
    WaitChrThread(0x109, 0x3)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    Battle(0x67, 0x0, 0x0, 0x0, 0xFF)
    Call(0, 3)
    Return()

    # Function_2_5A8 end

    def Function_3_CE1(): pass

    label("Function_3_CE1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapFlags(0x10)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x10, 71650, -8000, -23580, 90)
    SetChrPos(0x11, 71720, -8000, -25780, 90)
    SetChrPos(0x12, 70040, -8000, -24510, 90)
    SetChrChipByIndex(0x10, 15)
    SetChrSubChip(0x10, 0)
    SetChrChipByIndex(0x11, 15)
    SetChrSubChip(0x11, 0)
    SetChrChipByIndex(0x12, 16)
    SetChrSubChip(0x12, 0)
    OP_44(0x10, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0x12, 0xFF)
    SetChrPos(0x109, 78030, -8000, -23670, 270)
    SetChrPos(0x10F, 78300, -8000, -25280, 270)
    SetChrChipByIndex(0x109, 0)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 1)
    SetChrSubChip(0x10F, 0)
    OP_6D(73150, -8000, -22990, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(315000, 0)
    OP_6E(219, 0)
    LoadEffect(0x0, "battle\\mgblood2.eff")
    FadeToBright(1000, 0)
    OP_6B(4500, 1000)
    OP_0D()
    Sleep(500)
    OP_43(0x10, 0x0, 0x0, 0x4)
    OP_43(0x11, 0x0, 0x0, 0x5)
    OP_43(0x12, 0x0, 0x0, 0x6)
    WaitChrThread(0x10, 0x0)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    Sleep(1500)

    def lambda_E37():
        OP_6D(76870, -8000, -23160, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E37)

    def lambda_E4F():
        OP_67(0, 4860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E4F)

    def lambda_E67():
        OP_6B(3840, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_E67)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    Sleep(100)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #7
        0x109,
        "#1063F#5P……………………………\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 500)

    ChrTalk(    #8
        0x10F,
        "#1441F#6P凯文，刚才那是……！？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #9
        0x109,
        (
            "#1065F#2P啊啊……我知道。\x02\x03",

            "#1067F虽然魔兽的种类多种多样，\x01",
            "但这种类型的还是第一次看见……\x02\x03",

            "看来我们的常识\x01",
            "在这地方越来越不通用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10F,
        (
            "#1445F#6P……………………………\x02\x03",

            "#1446F不光是魔兽……\x01",
            "还有更奇怪的事。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1063F#2P啊啊……\x01",
            "是『属性』造成的影响变化吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1443F#6P嗯……\x02\x03",

            "『地』、『水』、『火』、『风』……\x02\x03",

            "除了这四属性以外，\x01",
            "『空』、『幻』、『时』的属性\x01",
            "似乎也起作用了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#2P你连这都发现了吗。\x02\x03",

            "#1060F本来，『空』、『幻』、『时』这种\x01",
            "高等属性是不会对其它事物产生影响的。\x02\x03",

            "虽然有惧怕『火』属性的魔兽，\x01",
            "但没有惧怕『幻』属性的魔兽。\x02\x03",

            "这是因为我们住的世界\x01",
            "在灵性上属于低等的次元。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        (
            "#1446F#6P女神与我们住的世界\x01",
            "没有任何交点……\x02\x03",

            "女神只会从遥远的高处\x01",
            "投下名为奇迹的小石而已。\x02\x03",

            "#1440F……和圣典上说的一样呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1060F#2P对，就是教会的基本理念。\x02\x03",

            "#1065F然而，在这个地方\x01",
            "高等属性却会产生影响……\x02\x03",

            "#1067F……说实话，这是不可能的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        (
            "#1445F#6P………………………………\x02\x03",

            "#1802F那么……\x01",
            "那个骸骨一样的魔兽也是？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1065F#2P与其说是『魔兽』，\x01",
            "不如说是『魔物』比较正确呢。\x02\x03",

            "#1063F在我们的世界\x01",
            "不可能存在的东西……\x02\x03",

            "似乎在这里若无其事地徘徊啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1802F#6P………………………………\x02\x03",

            "#1445F……就这样继续前进\x01",
            "没问题吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1065F#2P虽然相当棘手……\x01",
            "但并不是无法处置。\x02\x03",

            "#1060F就这样在可能的限度内\x01",
            "尽量继续前进吧。\x02\x03",

            "不过，导力器的设置\x01",
            "最好还是重新调整一下比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10F,
        "#1443F#6P……是啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x260B)
    OP_28(0x28, 0x1, 0x10)
    OP_28(0x28, 0x1, 0x20)
    OP_28(0x28, 0x1, 0x40)
    OP_28(0x28, 0x1, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    Sleep(500)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_3_CE1 end

    def Function_4_1583(): pass

    label("Function_4_1583")

    PlayEffect(0x0, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_15BE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_15BE)
    OP_22(0x214, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Return()

    # Function_4_1583 end

    def Function_5_15DF(): pass

    label("Function_5_15DF")

    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_161F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_161F)
    OP_22(0x214, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_5_15DF end

    def Function_6_1640(): pass

    label("Function_6_1640")

    Sleep(400)
    PlayEffect(0x0, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1680():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1680)
    OP_22(0x214, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_6_1640 end

    def Function_7_16A1(): pass

    label("Function_7_16A1")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS499._CH")
    OP_C5(0x1, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS445._CH")
    OP_C5(0x2, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS448._CH")
    OP_C6(0x0, 0x3, -1, 500, 0)
    Fade(500)
    SetChrPos(0x109, 58550, -60000, -72010, 90)
    SetChrPos(0x10F, 59260, -60000, -70430, 135)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    OP_6D(58520, -60000, -70440, 0)
    OP_67(0, 5400, -10000, 0)
    OP_6B(3600, 0)
    OP_6C(315000, 0)
    OP_6E(216, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #21
        0x109,
        "#1079F#5P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10F,
        (
            "#1442F#5P……好漂亮………\x02\x03",

            "七耀石的宝珠……？\x01",
            "但是，又有些……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1060F#5P唔……\x01",
            "总之先碰一下看看吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1864():
        OP_6D(59080, -60000, -70580, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1864)
    OP_8E(0x109, 0xE808, 0xFFFF15A0, 0xFFFEE6E8, 0x3E8, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 14)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x13, 0xE902, 0xFFFF1988, 0xFFFEE774, 0x1F4, 0x0)
    Sleep(500)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x13, 0x80)
    OP_0D()
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x00得到了\x1F\x52\x03\x07\x00。\x02",
    )

    Jump("loc_1909")

    label("loc_1909")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x352, 1)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #25
        0x10F,
        "#1443F#2P好像没有危险……？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #26
        0x109,
        (
            "#1075F#6P啊啊，好像没问题。\x02\x03",

            "#1060F而且……\x01",
            "这光芒感觉很温暖。\x02\x03",

            "就像心脏的跳动一样\x01",
            "缓缓地闪烁着……\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x15F, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #27
        0x10F,
        "#1444F#2P这是……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        "#1063F#5P又是『方石』吗……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 2)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8C(0x10F, 135, 400)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #29
        "\x07\x0C\x18#2S#80W……异邦者啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #30
        "\x07\x0C\x18#2S#80W手持『方石』者啊……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #31
        0x10F,
        "#1802F#5P刚才的声音……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x109,
        (
            "#1069F#5P喂，你是谁！？\x01",
            "在哪里说话呢？\x02\x03",

            "你到底是什么人！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #33
        (
            "\x07\x0C\x18#2S#80W……请将此『封印石』……\x01",
            "放在庭院的石碑上……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #34
        (
            "\x07\x0C\x18#2S#80W这样的话……\x01",
            "结界和……被囚禁的……就会……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)

    ChrTalk(    #35
        0x109,
        (
            "#1063F#5P可恶……\x01",
            "听不清楚……\x02\x03",

            "#1069F就是把刚才的宝石，\x01",
            "拿到最开始的石碑那里就行了吧！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #36
        (
            "\x07\x0C\x18#2S#80W……『方石』的力量\x01",
            "已经进一步……解放……\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #37
        "\x07\x0C\x18#2S#80W……请好好利用……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    OP_22(0x15F, 0x0, 0x64)
    Sleep(1000)
    LoadEffect(0x0, "map\\mp252_01.eff")
    PlayEffect(0x0, 0x0, 0x109, 270, 1250, 100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xC9, 0x0, 0x64)
    Sleep(1500)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        (
            "\x07\x05『方石』的传送功能\x01",
            "现在可以使用了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    OP_23(0xC9)
    Sleep(500)
    OP_C6(0x1, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x0, 592000, 16000, 0)
    OP_C6(0x2, 0x1, 250, 250, 0)
    OP_A3(0x1)
    OP_43(0x0, 0x0, 0x0, 0x8)
    Sleep(1500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05单击画面右上显示的\x01",
            "【方石按钮】，\x01",
            "选择需要前往的场所。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_3F(0x33E, 1)
    OP_3E(0x211, 1)
    OP_A2(0x1)
    Sleep(500)
    OP_C6(0x1, 0x3, 16777215, 500, 0)
    FadeToBright(300, 0)
    OP_C6(0x0, 0x3, -1, 500, 0)
    OP_22(0xC9, 0x0, 0x64)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_82(0x0, 0x0)
    OP_23(0xC9)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #40
        0x109,
        "#1079F#5P这、这是……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #41
        "\x07\x0C\x18#2S#80W那个人……要小心……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #42
        (
            "\x07\x0C\x18#2S#80W如果不集中力量……\x01",
            "……你们也会永远………\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #43
        "\x07\x0C\x18#2S#80W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)

    def lambda_2026():
        OP_6D(58430, -60000, -70120, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2026)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    WaitChrThread(0xEE, 0x0)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #44
        0x10F,
        "#1443F#2P……我说。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1068F#5P别问我了……\x02\x03",

            "说实话，\x01",
            "我也正为意想不到的发展而头昏脑涨呢。\x02",
        )
    )

    Jump("loc_2100")

    label("loc_2100")

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #46
        0x109,
        (
            "#1060F#6P不过看起来……\x01",
            "刚才的声音，\x01",
            "好像是想引导我们吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10F,
        (
            "#1446F#2P……的确是这样。\x02\x03",

            "#1443F会是这『方石』的意识\x01",
            "在跟我们说话吗……？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x109,
        (
            "#1065F#6P不，\x01",
            "刚才声音的主人将『方石』当作了客观对象来称呼。\x02\x03",

            "所以他们应该不是同一实体。\x02\x03",

            "#1063F而且，\x01",
            "好像还提到了『那个人』。\x02\x03",

            "是指那时的黑衣男子\x01",
            "还是别人就不知道了。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #49
        0x10F,
        "#1445F#2P……脑袋开始痛起来了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x109,
        (
            "#1068F#6P我也一样……\x02\x03",

            "#1060F唉，算了，\x01",
            "也只好一个个解决了。\x02\x03",

            "那么现在……\x01",
            "就来试试『方石』的力量吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x10F,
        "#1444F#2P你是说真的……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1075F#6P当然是说真的。\x02\x03",

            "#1062F隐藏着传送之力的\x01",
            "古代遗物\x01",
            "可是相当珍贵的哦？\x02\x03",

            "事到如今能用的东西\x01",
            "就要彻底的利用。\x02",
        )
    )

    Jump("loc_2435")

    label("loc_2435")

    CloseMessageWindow()

    ChrTalk(    #53
        0x10F,
        (
            "#1446F#2P……明白了。\x02\x03",

            "#1443F不过，\x01",
            "使用时可要多加小心。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        "#1060F#6P嗯，交给我吧。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x260C)
    OP_28(0x28, 0x1, 0x100)
    OP_28(0x28, 0x1, 0x200)
    OP_28(0x28, 0x1, 0x400)
    OP_64(0x0, 0x1)
    Sleep(300)
    OP_C6(0x0, 0x3, 16777215, 500, 0)
    EventEnd(0x0)
    Return()

    # Function_7_16A1 end

    def Function_8_24D6(): pass

    label("Function_8_24D6")

    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(500)

    label("loc_24F9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_253C")
    Sleep(200)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2525")
    Jump("loc_253C")

    label("loc_2525")

    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    Jump("loc_24F9")

    label("loc_253C")

    Return()

    # Function_8_24D6 end

    def Function_9_253D(): pass

    label("Function_9_253D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 5)), scpexpr(EXPR_END)), "loc_2548")
    Return()

    label("loc_2548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2551")
    Return()

    label("loc_2551")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25EE")
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #55
        0x109,
        (
            "#1078F哦，机会难得，\x01",
            "就使用『方石』试试吧。\x02\x03",

            "也好测试一下传送功能。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #56
        0x10F,
        "#1801F……我觉得很不保险。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2686")

    label("loc_25EE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2686")
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #57
        0x109,
        (
            "#1078F哦，机会难得，\x01",
            "就使用『方石』试试吧。\x02\x03",

            "也好测试一下传送功能。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #58
        0x10F,
        "#1801F……我觉得很不保险。\x02",
    )

    CloseMessageWindow()

    label("loc_2686")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_253D end

    def Function_10_26A2(): pass

    label("Function_10_26A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    OP_6D(-4830, -49650, -96300, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_26FB():
        OP_6B(4200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_26FB)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    Fade(1000)
    OP_22(0x117, 0x0, 0x64)
    OP_71(0x404, 0x0)
    ExitThread()
    OP_0D()
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/U7000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_10_26A2 end

    def Function_11_2744(): pass

    label("Function_11_2744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2750")
    Return()

    label("loc_2750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 6)), scpexpr(EXPR_END)), "loc_2758")
    Return()

    label("loc_2758")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x109, 1750, -52000, -98180, 270)
    SetChrPos(0x10F, 2590, -52000, -97130, 270)
    SetChrPos(0x107, 3530, -52000, -98900, 270)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(-160, -52000, -96500, 0)
    OP_67(0, 5880, -10000, 0)
    OP_6B(4140, 0)
    OP_6C(315000, 0)
    OP_6E(228, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #59
        0x10F,
        (
            "#1444F……？\x02\x03",

            "凯文……\x01",
            "这前面刚才不是被阻隔的吗？\x02",
        )
    )

    Jump("loc_2843")

    label("loc_2843")

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        "#1063F是啊，什么时候……\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)
    OP_8C(0x107, 315, 400)
    Sleep(300)

    ChrTalk(    #61
        0x107,
        "#064F#6P怎么了？\x02",
    )

    CloseMessageWindow()

    def lambda_28B4():
        OP_6D(2100, -52000, -97400, 1300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_28B4)

    def lambda_28CC():
        OP_67(0, 5980, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28CC)

    def lambda_28E4():
        OP_6B(4000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_28E4)

    def lambda_28F4():
        OP_8C(0x10F, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_28F4)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #62
        0x10F,
        (
            "#1443F#2P刚才这前面\x01",
            "还立着奇怪的障壁。\x02\x03",

            "现在却消失了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x107,
        (
            "#063F#6P是这样吗……\x02\x03",

            "嗯……\x01",
            "是什么原因呢？\x02",
        )
    )

    Jump("loc_299E")

    label("loc_299E")

    CloseMessageWindow()

    ChrTalk(    #64
        0x109,
        (
            "#1065F#5P唔，勉强要说的话……\x02\x03",

            "#1063F可能是因为\x01",
            "把提妲从那个\x01",
            "『封印石』里解放出来了吧。\x02\x03",

            "除此以外，\x01",
            "我们也没有做其它事情了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x107,
        (
            "#064F#6P原、原来如此……\x02\x03",

            "#561F……不过确实\x01",
            "有这个可能呢。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        "#1064F#5P咦……为什么？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x107,
        (
            "#062F#6P把封印我的石头\x01",
            "放在这附近，\x01",
            "应该也有什么原因吧。\x02\x03",

            "怎么说呢……\x01",
            "就像是基于某种规则一样。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x109,
        "#1063F#5P规则……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x10F,
        (
            "#1447F#2P……原来如此。\x01",
            "我大概明白了。\x02\x03",

            "#1448F也就是，在这种情况下\x01",
            "不解放你就无法继续前进的\x01",
            "这样一种规则吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x107,
        (
            "#560F#6P是、是的……\x01",
            "虽然只是我的猜测。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x109,
        (
            "#1060F#5P不……\x01",
            "说不定正好切中关键点啊。\x02\x03",

            "#1065F虽然不知道是谁干的，\x01",
            "但这种情况肯定是人为造成的。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x10F,
        (
            "#1443F#2P……看来我们也要\x01",
            "对这些情况多加注意。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x260E)
    OP_28(0x29, 0x1, 0x4)
    OP_28(0x29, 0x1, 0x8)
    OP_28(0x29, 0x1, 0x10)
    Sleep(500)
    EventEnd(0x0)
    Return()

    # Function_11_2744 end

    def Function_12_2CBA(): pass

    label("Function_12_2CBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 7)), scpexpr(EXPR_END)), "loc_2CC2")
    Return()

    label("loc_2CC2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D18")
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #73
        0x109,
        "#1079F#12P哎……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DBC")

    label("loc_2D18")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D6C")
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #74
        0x10F,
        "#1444F#12P啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DBC")

    label("loc_2D6C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DBC")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #75
        0x107,
        "#064F#12P咦……\x02",
    )

    CloseMessageWindow()

    label("loc_2DBC")

    Sleep(300)

    def lambda_2DC7():
        OP_6D(-47880, -52000, -80330, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DC7)

    def lambda_2DDF():
        OP_67(0, 5600, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2DDF)

    def lambda_2DF7():
        OP_6B(3500, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2DF7)

    def lambda_2E07():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2E07)

    def lambda_2E17():
        OP_6E(255, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_2E17)

    def lambda_2E27():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_2E27)
    OP_8C(0x2, 270, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_2E46():
        OP_6D(-46610, -52000, -80360, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E46)

    def lambda_2E5E():
        OP_67(0, 5000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E5E)

    def lambda_2E76():
        OP_6B(3550, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_2E76)
    SetChrPos(0x109, -36110, -52000, -82630, 270)
    SetChrPos(0x10F, -35600, -52000, -81580, 270)
    SetChrPos(0x107, -34670, -52000, -82170, 270)

    def lambda_2EB9():
        OP_8E(0xFE, 0xFFFF539E, 0xFFFF34E0, 0xFFFEBC04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EB9)
    Sleep(300)

    def lambda_2ED9():
        OP_8E(0xFE, 0xFFFF5416, 0xFFFF34E0, 0xFFFEC12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_2ED9)
    Sleep(400)

    def lambda_2EF9():
        OP_8E(0xFE, 0xFFFF59C0, 0xFFFF34E0, 0xFFFEBE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2EF9)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #76
        0x109,
        "#1063F……这是什么呀？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x10F,
        "#1444F#2P画着月亮的门……？\x02",
    )

    CloseMessageWindow()
    OP_22(0x222, 0x0, 0x64)
    OP_82(0x86, 0x2)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(500)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #78
        "\x07\x05#2S#40W终于来了……\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 90, -1, -1)

    AnonymousTalk(    #79
        (
            "\x07\x05#40W　汝须将擅长导力技术之少女\x01",
            "　　   引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #80
        0x107,
        (
            "#065F#12P哇、哇啊……\x01",
            "脑子里直接传来了声音……！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x109,
        (
            "#1063F和之前一样，\x01",
            "这扇门也拥有意识吗……\x02\x03",

            "#1065F看来我们也该\x01",
            "有必要习惯这种异常的发展了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x10F,
        (
            "#1802F#2P不过……\x01",
            "『擅长导力技术之少女』吗。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_31DF():
        OP_8C(0x109, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_31DF)
    Sleep(100)
    OP_8C(0x10F, 135, 400)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #83
        0x107,
        (
            "#065F#12P哎……\x01",
            "是、是说我吗！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x10F,
        "#1446F#5P……恐怕是了。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x109,
        (
            "#1068F#5P无论怎么想\x01",
            "都是在说提妲吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)

    ChrTalk(    #86
        0x109,
        "#1063F喂，这孩子可以吗？\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #87
        (
            "\x07\x05#2S#40W         然也……\x01",
            "这位少女正是吾所求之人。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)
    Sleep(500)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 90, -1, -1)

    AnonymousTalk(    #88
        (
            "\x07\x05#40W可入此门者仅有这位少女……\x01",
            "#500W\x01",
            "#40W   若不畏惧吾之试炼\x01",
            "    就请通过此门。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #89
        0x107,
        (
            "#065F#12P哇哇……\x01",
            "试、试炼是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x109,
        (
            "#1063F看来好像会\x01",
            "测试一下你的本事吧……\x02\x03",

            "而且这扇门似乎\x01",
            "只有提妲能进去。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x10F,
        (
            "#1443F#2P……真不讲理呢。\x02\x03",

            "#1446F#2P我想没必要理它吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x107,
        (
            "#561F#12P………………………………\x02\x03",

            "#062F请、请等一下！\x02\x03",

            "我要进去看看！\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_35ED():
        OP_8C(0x109, 90, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_35ED)
    Sleep(100)
    OP_8C(0x10F, 135, 500)

    ChrTalk(    #93
        0x10F,
        "#1444F#5P咦……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x109,
        (
            "#1069F#5P等一下！\x01",
            "这实在是……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x107,
        (
            "#062F#12P这个，\x01",
            "可能也是刚才说过的『规则』。\x02\x03",

            "而且现在也需要\x01",
            "尽可能多的线索……\x02\x03",

            "如果有危险\x01",
            "我就马上回来！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x10F,
        "#1802F#5P提妲……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x109,
        (
            "#1065F#5P………………………………\x02\x03",

            "#1063F明白了，拜托你了。\x02\x03",

            "只不过，\x01",
            "如果有危险一定要马上回来哦？\x02",
        )
    )

    Jump("loc_3773")

    label("loc_3773")

    CloseMessageWindow()

    ChrTalk(    #98
        0x10F,
        "#1448F#5P……可不能勉强自己。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x107,
        "#560F#12P是……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_37C7():
        OP_6D(-47050, -52000, -80660, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_37C7)
    OP_43(0x109, 0x0, 0x0, 0xD)
    OP_43(0x10F, 0x0, 0x0, 0xE)
    Sleep(300)

    def lambda_37F2():
        OP_8E(0xFE, 0xFFFF50E2, 0xFFFF34E0, 0xFFFEBDDA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_37F2)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x3)
    OP_8C(0x109, 270, 400)
    OP_8C(0x10F, 270, 400)
    WaitChrThread(0x109, 0x1)
    Sleep(1000)

    def lambda_383C():
        OP_8E(0xFE, 0xFFFF4912, 0xFFFF34E0, 0xFFFEBFBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_383C)

    def lambda_3857():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3857)
    Sleep(1300)
    OP_22(0x99, 0x0, 0x64)

    def lambda_3871():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3871)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_44(0x109, 0x2)
    OP_44(0x107, 0x0)
    OP_44(0x107, 0x1)
    OP_C4(0x0, 0x10)
    OP_6D(-11520, -100000, -123160, 0)
    FadeToBright(3000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    OP_28(0x1, 0x4, 0x2)
    OP_E3(0x0, 0x19, 0, 0x0)
    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_12_2CBA end

    def Function_13_38E4(): pass

    label("Function_13_38E4")


    def lambda_38EA():

        label("loc_38EA")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_38EA")

    QueueWorkItem2(0x109, 3, lambda_38EA)
    Sleep(50)
    OP_8F(0x109, 0xFFFF565A, 0xFFFF34E0, 0xFFFEB92A, 0x3E8, 0x0)
    Return()

    # Function_13_38E4 end

    def Function_14_390F(): pass

    label("Function_14_390F")


    def lambda_3915():

        label("loc_3915")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_3915")

    QueueWorkItem2(0x10F, 3, lambda_3915)
    Sleep(150)
    OP_8F(0x10F, 0xFFFF5628, 0xFFFF34E0, 0xFFFEC1E0, 0x3E8, 0x0)
    Return()

    # Function_14_390F end

    def Function_15_393A(): pass

    label("Function_15_393A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x78)
    SetChrPos(0x109, -42540, -52000, -82980, 270)
    SetChrPos(0x10F, -42570, -52000, -81570, 270)
    SetChrPos(0x107, -46960, -52000, -82210, 90)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-47380, -52000, -80280, 0)
    OP_67(0, 5050, -10000, 0)
    OP_6B(3020, 0)
    OP_6C(315000, 0)
    OP_6E(286, 0)
    Sleep(2000)
    OP_1D(0xDC)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_3A1C():
        OP_6D(-45030, -52000, -80710, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A1C)

    def lambda_3A34():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3A34)
    OP_22(0x99, 0x0, 0x64)

    def lambda_3A49():
        OP_8E(0xFE, 0xFFFF52F4, 0xFFFF34E0, 0xFFFEBF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3A49)

    def lambda_3A64():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3A64)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x107, 0x1)
    WaitChrThread(0x109, 0x0)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    OP_82(0x85, 0x2)
    Sleep(1000)

    ChrTalk(    #100
        0x109,
        (
            "#1840F提妲……\x01",
            "你没事吗。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x10F,
        (
            "#1802F#12P……没问题吗？\x01",
            "看起来好像有点疲劳。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x107,
        (
            "#563F#5P嘿嘿……\x01",
            "不用担心。\x02\x03",

            "#066F虽然遇到了战斗，\x01",
            "不过总算是赢了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x109,
        (
            "#1075F是吗……\x02\x03",

            "#1063F……那么，\x01",
            "到底发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x107,
        "#062F#5P嗯，其实是……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #105
        "\x07\x05提妲将门中发生的事情说了一遍。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #106
        0x10F,
        "#1444F#12P这种事……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x109,
        (
            "#1067F原来如此。\x01",
            "确实是『规则』啊。\x02\x03",

            "#1065F要打开『门』，\x01",
            "就需要某种条件……\x02\x03",

            "进去之后\x01",
            "会有名为『试炼』\x01",
            "的战斗在等待……\x02\x03",

            "如果胜利了，\x01",
            "就能看到『记忆之碎片』什么的，\x01",
            "并且还会获得米拉……\x02\x03",

            "#1060F──总结起来就是这样的地方啊。\x02",
        )
    )

    Jump("loc_3D41")

    label("loc_3D41")

    CloseMessageWindow()

    ChrTalk(    #108
        0x107,
        (
            "#560F#5P嗯……\x01",
            "我想就是这样的。\x02\x03",

            "而且我所见到的『记忆之碎片』\x01",
            "好像还有后续的感觉……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1065F唔……\x02\x03",

            "既然如此，\x01",
            "或许有几种模式吧。\x02\x03",

            "#1060F如果再碰到类似的门，\x01",
            "还是记录到手册上比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x10F,
        "#1448F#12P……就这样办吧。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #111
        "\x07\x05关于『记忆之门』\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    AnonymousTalk(    #112
        (
            "\x07\x05放置于各地的\x01",
            "可以观看插曲情节的『记忆之门』\x01",
            "分为以下三种模式。\x02\x03",

            "【月之门】　　长篇故事\x01",
            "【星之门】　　短篇故事\x01",
            "【太阳之门】　小游戏相关\x02\x03",

            "要打开这些门\x01",
            "必须完成\x01",
            "门上给出的条件。\x02\x03",

            "根据门的不同，可能会限制入室者，\x01",
            "在其中也可能会遭遇到战斗。\x02\x03",

            "第一次看完某段故事\x01",
            "可以获得米拉，\x01",
            "此外根据选择和行动\x01",
            "可能还会获得道具之类的奖励。\x02\x03",

            "而且，这些相关情报\x01",
            "会各自记录在『星杯手册』中，\x01",
            "用于确认现在的状况。\x02\x03",

            "此外，发现过一次的门\x01",
            "也可以作为『方石』的\x01",
            "传送目的地进行选择。\x02",
        )
    )

    Jump("loc_406A")

    label("loc_406A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(-43980, -52000, -82140, 0)
    OP_67(0, 8500, -10000, 0)
    OP_6B(4200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -43980, -52000, -82140, 90)
    SetChrPos(0x1, -43980, -52000, -82140, 90)
    SetChrPos(0x2, -43980, -52000, -82140, 90)
    OP_69(0x0, 0x0)
    OP_A2(0x260F)
    OP_28(0x29, 0x1, 0x20)
    OP_28(0x29, 0x1, 0x40)
    OP_28(0x29, 0x1, 0x80)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_15_393A end

    def Function_16_411E(): pass

    label("Function_16_411E")

    EventBegin(0x0)
    OP_22(0x222, 0x0, 0x64)
    Fade(500)
    SetChrPos(0x0, -44060, -52000, -81130, 270)
    SetChrPos(0x1, -44010, -52000, -83140, 270)
    SetChrPos(0x2, -41890, -52000, -81300, 270)
    SetChrPos(0x3, -41920, -52000, -83220, 270)
    OP_6D(-44050, -52000, -82290, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(5180, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_28(0x1, 0x4, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C1")
    OP_28(0x2, 0x4, 0x2)

    label("loc_41C1")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #113
        (
            "\x07\x05#40W　汝须将擅长导力技术之少女，\x01",
            "　　  与猛烈之焰一同\x01",
            "　　  引领至吾面前。\x01",
            "#500W\x01",
            "#40W   如此，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4294")
    Call(0, 17)
    Jump("loc_42A9")

    label("loc_4294")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42A9")
    Call(0, 17)
    Jump("loc_42A9")

    label("loc_42A9")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_16_411E end

    def Function_17_42B5(): pass

    label("Function_17_42B5")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #114
        "\x07\x05打开『门』吗？\x18\x02",
    )


    label("loc_42D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4428")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "【打开门观看前篇】\x01",      # 0
            "【打开门观看后篇】\x01",      # 1
            "【     取消    】\x01",       # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4358"),
        (1, "loc_4362"),
        (2, "loc_440B"),
        (SWITCH_DEFAULT, "loc_4418"),
    )


    label("loc_4358")

    OP_A3(0x0)
    Call(0, 18)
    Jump("loc_4425")

    label("loc_4362")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4385")
    OP_A2(0x0)
    Call(0, 18)
    Jump("loc_4408")

    label("loc_4385")

    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #115
        (
            "\x07\x05#40W 如果达到必要之条件，\x01",
            "  就请到吾面前来。\x01",
            "#500W\x01",
            "#40W如是，则『门』将开启……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4408")

    Jump("loc_4425")

    label("loc_440B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4425")

    label("loc_4418")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4425")

    label("loc_4425")

    Jump("loc_42D6")

    label("loc_4428")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_42B5 end

    def Function_18_4433(): pass

    label("Function_18_4433")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)

    def lambda_449C():
        OP_6B(4460, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_449C)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_44E9")
    OP_E3(0x0, 0x1A, 0, 0x0)
    Jump("loc_44F1")

    label("loc_44E9")

    OP_E3(0x0, 0x19, 0, 0x0)

    label("loc_44F1")

    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_4433 end

    def Function_19_44FB(): pass

    label("Function_19_44FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x0, -44060, -52000, -81130, 270)
    SetChrPos(0x1, -44010, -52000, -83140, 270)
    SetChrPos(0x2, -41890, -52000, -81300, 270)
    SetChrPos(0x3, -41920, -52000, -83220, 270)
    OP_6D(-44050, -52000, -82290, 0)
    OP_67(0, 6180, -10000, 0)
    OP_6B(5180, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    EventEnd(0x0)
    Return()

    # Function_19_44FB end

    def Function_20_45A6(): pass

    label("Function_20_45A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_45B7")
    Call(0, 2)
    Return()

    label("loc_45B7")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 81830, -8000, -24200, 270)
    SetChrPos(0x1, 82880, -8000, -23390, 270)
    SetChrPos(0x2, 83060, -8000, -25130, 270)
    SetChrPos(0x3, 83760, -8000, -24230, 270)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp204_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 82870, -8000, -24100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 28)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_20_45A6 end

    def Function_21_4695(): pass

    label("Function_21_4695")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, -9030, -28000, -58220, 90)
    SetChrPos(0x1, -10030, -28000, -59000, 90)
    SetChrPos(0x2, -10240, -28000, -57360, 90)
    SetChrPos(0x3, -11170, -28000, -58090, 90)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -9760, -28000, -58190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 28)
    EventEnd(0x0)
    Return()

    # Function_21_4695 end

    def Function_22_4748(): pass

    label("Function_22_4748")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 16180, -44000, -58840, 180)
    SetChrPos(0x1, 15140, -44000, -57850, 180)
    SetChrPos(0x2, 17040, -44000, -57890, 180)
    SetChrPos(0x3, 16040, -44000, -56770, 180)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 16050, -44000, -58090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 28)
    EventEnd(0x0)
    Return()

    # Function_22_4748 end

    def Function_23_47FB(): pass

    label("Function_23_47FB")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x0, 23970, -80000, -137070, 0)
    SetChrPos(0x1, 24950, -80000, -138170, 0)
    SetChrPos(0x2, 23010, -80000, -137980, 0)
    SetChrPos(0x3, 24050, -80000, -139020, 0)
    OP_69(0x0, 0x0)
    LoadEffect(0x0, "map\\mp200_02.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 24010, -80000, -138080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 28)
    EventEnd(0x0)
    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x14B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C0(0x16, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_23_47FB end

    def Function_24_48D9(): pass

    label("Function_24_48D9")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 81830, -8000, -24200, 90)
    SetChrPos(0x2, 82880, -8000, -23390, 90)
    SetChrPos(0x1, 83060, -8000, -25130, 90)
    SetChrPos(0x0, 83760, -8000, -24230, 90)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp204_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 82870, -8000, -24100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 29)
    NewScene("ED6_DT21/U7000   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_24_48D9 end

    def Function_25_4995(): pass

    label("Function_25_4995")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, -8630, -28000, -58220, 270)
    SetChrPos(0x2, -9630, -28000, -59000, 270)
    SetChrPos(0x1, -9840, -28000, -57360, 270)
    SetChrPos(0x0, -10770, -28000, -58090, 270)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, -9760, -28000, -58190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 29)
    NewScene("ED6_DT21/M7001   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4995 end

    def Function_26_4A51(): pass

    label("Function_26_4A51")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 16180, -44000, -59240, 0)
    SetChrPos(0x2, 15140, -44000, -58250, 0)
    SetChrPos(0x1, 17040, -44000, -58290, 0)
    SetChrPos(0x0, 16040, -44000, -57170, 0)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 16050, -44000, -58090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 29)
    NewScene("ED6_DT21/M7001   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_26_4A51 end

    def Function_27_4B0D(): pass

    label("Function_27_4B0D")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    SetChrPos(0x3, 23970, -80000, -137070, 180)
    SetChrPos(0x2, 24950, -80000, -138170, 180)
    SetChrPos(0x1, 23010, -80000, -137980, 180)
    SetChrPos(0x0, 24050, -80000, -139020, 180)
    OP_69(0x0, 0x0)
    OP_0D()
    LoadEffect(0x0, "map\\mp200_01.eff")
    PlayEffect(0x0, 0xFF, 0xFF, 24010, -80000, -138080, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    Call(0, 29)
    NewScene("ED6_DT21/M7002   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_27_4B0D end

    def Function_28_4BC9(): pass

    label("Function_28_4BC9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BF2")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4BE6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4BE6)

    label("loc_4BF2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C1B")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4C0F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4C0F)

    label("loc_4C1B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C44")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4C38():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4C38)

    label("loc_4C44")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C6D")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_4C61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4C61)

    label("loc_4C6D")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C99")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4C99")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CB0")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4CB0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CC7")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4CC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CDE")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_4CDE")

    Return()

    # Function_28_4BC9 end

    def Function_29_4CDF(): pass

    label("Function_29_4CDF")


    def lambda_4CE5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4CE5)

    def lambda_4CF7():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4CF7)

    def lambda_4D09():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4D09)

    def lambda_4D1B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4D1B)
    Sleep(1000)
    Return()

    # Function_29_4CDF end

    def Function_30_4D2D(): pass

    label("Function_30_4D2D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E12")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x291, 1)"), scpexpr(EXPR_END)), "loc_4DA1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #116
        "\x07\x00得到了\x1F\x91\x02\x07\x00。\x02",
    )

    Jump("loc_4D86")

    label("loc_4D86")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2681)
    Jump("loc_4E0F")

    label("loc_4DA1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #117
        (
            "宝箱里装有\x1F\x91\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x91\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4DF0")

    label("loc_4DF0")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_4E0F")

    Jump("loc_4E45")

    label("loc_4E12")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #118
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4E45")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_30_4D2D end

    def Function_31_4E53(): pass

    label("Function_31_4E53")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F38")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_4EC7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #119
        "\x07\x00得到了\x1F\xF5\x01\x07\x00。\x02",
    )

    Jump("loc_4EAC")

    label("loc_4EAC")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2682)
    Jump("loc_4F35")

    label("loc_4EC7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #120
        (
            "宝箱里装有\x1F\xF5\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF5\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4F16")

    label("loc_4F16")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4F35")

    Jump("loc_4F6B")

    label("loc_4F38")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #121
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4F6B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_31_4E53 end

    def Function_32_4F79(): pass

    label("Function_32_4F79")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FE9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(300)

    AnonymousTalk(    #122
        "\x07\x00得到了\x07\x02３００米拉\x07\x00。\x02",
    )

    Jump("loc_4FD7")

    label("loc_4FD7")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2683)
    Jump("loc_5005")

    label("loc_4FE9")


    AnonymousTalk(    #123
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5005")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_32_4F79 end

    SaveToFile()

Try(main)
