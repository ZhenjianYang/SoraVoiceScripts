from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Bone Warrior',                         # 9
        'Bone Warrior',                         # 10
        'Bone Shooter',                         # 11
        'Sealing Stone 1',                      # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
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
        "Function_3_D27",          # 03, 3
        "Function_4_1B26",         # 04, 4
        "Function_5_1B82",         # 05, 5
        "Function_6_1BE3",         # 06, 6
        "Function_7_1C44",         # 07, 7
        "Function_8_2C7C",         # 08, 8
        "Function_9_2CE3",         # 09, 9
        "Function_10_2E74",        # 0A, 10
        "Function_11_2F16",        # 0B, 11
        "Function_12_35F4",        # 0C, 12
        "Function_13_4362",        # 0D, 13
        "Function_14_438D",        # 0E, 14
        "Function_15_43B8",        # 0F, 15
        "Function_16_4D92",        # 10, 16
        "Function_17_4F30",        # 11, 17
        "Function_18_50A8",        # 12, 18
        "Function_19_5170",        # 13, 19
        "Function_20_521B",        # 14, 20
        "Function_21_530A",        # 15, 21
        "Function_22_53BD",        # 16, 22
        "Function_23_5470",        # 17, 23
        "Function_24_554E",        # 18, 24
        "Function_25_560A",        # 19, 25
        "Function_26_56C6",        # 1A, 26
        "Function_27_5782",        # 1B, 27
        "Function_28_583E",        # 1C, 28
        "Function_29_5954",        # 1D, 29
        "Function_30_59A2",        # 1E, 30
        "Function_31_5B7C",        # 1F, 31
        "Function_32_5CAE",        # 20, 32
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
        "#1079F#5PCheck this out...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x10F,
        (
            "#1443FIt looks like that really was an 'entrance'\x01",
            "of sorts.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_1D(0xDC)

    def lambda_7BE():
        OP_6D(57610, -7450, -24140, 5000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7BE)

    def lambda_7D6():
        OP_67(0, 5640, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7D6)

    def lambda_7EE():
        OP_6B(7160, 7000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7EE)

    def lambda_7FE():
        OP_6C(292000, 5000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_7FE)

    def lambda_80E():
        OP_6E(537, 5000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_80E)
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
            "#1063F#5PWe still seem to be in the same bizarre\x01",
            "enclosed space as before.\x02\x03",

            "We've got quite a long road ahead of us,\x01",
            "don't we?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10F,
        "#1802FWe sure do...\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #4
        0x10F,
        "#1441FKevin!\x02",
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

    def lambda_A45():
        OP_6D(74350, -8000, -23480, 1600)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A45)

    def lambda_A5D():
        OP_67(0, 5530, -10000, 1600)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A5D)

    def lambda_A75():
        OP_6B(3800, 1600)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A75)

    def lambda_A85():
        OP_6C(315000, 1600)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A85)

    def lambda_A95():
        OP_6E(229, 1600)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_A95)
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

    def lambda_B12():

        label("loc_B12")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B12")

    QueueWorkItem2(0x10, 3, lambda_B12)
    Sleep(30)

    def lambda_B2A():

        label("loc_B2A")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B2A")

    QueueWorkItem2(0x11, 3, lambda_B2A)
    Sleep(30)

    def lambda_B42():

        label("loc_B42")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_B42")

    QueueWorkItem2(0x12, 3, lambda_B42)

    def lambda_B55():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_B55)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x0, 0x2)
    Sleep(100)

    def lambda_B74():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_B74)
    OP_22(0x99, 0x0, 0x64)
    OP_82(0x1, 0x2)
    Sleep(100)

    def lambda_B93():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_B93)
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
        "#1069FM-Monsters?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10F,
        (
            "#1802F#6PHow did they just appear out\x01",
            "of nowhere?\x02",
        )
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

    def lambda_C56():
        OP_6D(76160, -8000, -23500, 300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C56)

    def lambda_C6E():
        OP_67(0, 6030, -10000, 300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C6E)

    def lambda_C86():
        OP_6B(3250, 300)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_C86)
    SetChrChipByIndex(0x10, 4)

    def lambda_C9B():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_C9B)
    Sleep(30)
    SetChrChipByIndex(0x11, 4)

    def lambda_CC0():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_CC0)
    Sleep(30)
    SetChrChipByIndex(0x12, 6)

    def lambda_CE5():
        OP_91(0xFE, 0x1388, 0x0, 0x0, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_CE5)
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

    def Function_3_D27(): pass

    label("Function_3_D27")

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

    def lambda_E7D():
        OP_6D(76870, -8000, -23160, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E7D)

    def lambda_E95():
        OP_67(0, 4860, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_E95)

    def lambda_EAD():
        OP_6B(3840, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_EAD)
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
        "#1063F#5P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 0, 500)

    ChrTalk(    #8
        0x10F,
        "#1441F#6PHow can this be...?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x109, 180, 400)
    Sleep(300)

    ChrTalk(    #9
        0x109,
        (
            "#1065F#2PI know exactly what you mean.\x02\x03",

            "#1067FThere are a whole lot of monster types in our\x01",
            "world, but that's my first time seeing any like\x01",
            "THAT.\x02\x03",

            "This is like being in a totally different realm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10F,
        (
            "#1445F#6P...\x02\x03",

            "#1446FAnd the monsters weren't even\x01",
            "the strangest part.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x109,
        (
            "#1063F#2PTell me about it. The elements against them\x01",
            "weren't your usual affair, either.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10F,
        (
            "#1443F#6PExactly.\x02\x03",

            "The three elements of space, mirage, and time\x01",
            "were in effect during that battle, too.\x02\x03",

            "Not just the traditional four elements.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x109,
        (
            "#1065F#2PVery observant, rookie. Didn't think you'd notice\x01",
            "to that extent.\x02\x03",

            "#1060FThis points to yet another clue that we're a long\x01",
            "ways from home.\x02\x03",

            "I mean, you'll find a boatload of monsters that're\x01",
            "weak to fire in Zemuria, but you're not going to\x01",
            "find any that are weak to mirage.\x02\x03",

            "You know how it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10F,
        (
            "#1446F#6PIndeed, I do. Spiritually, the world in which we\x01",
            "live is in a relatively low plane of existence. \x02\x03",

            "To quote the Testaments:\x02\x03",

            "#1440F'Our world and the world of the Goddess will\x01",
            "forever be separate; She simply drops pebbles\x01",
            "from above, known as miracles...'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x109,
        (
            "#1060F#2PQuoting word for word? Though, hey,\x01",
            "I guess those ARE the basic principles.\x02\x03",

            "#1065FWe just keep running into surprises.\x01",
            "Space, time, AND mirage? All here?\x02\x03",

            "#1067FIt should be impossible...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10F,
        (
            "#1445F#6P...\x02\x03",

            "#1802FWhat about those monsters themselves?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x109,
        (
            "#1065F#2PHonestly, they were less 'monsters' and more \x01",
            "'fiends.'\x02\x03",

            "#1063FCreatures that shouldn't even be allowed to\x01",
            "exist in our world, and yet they somehow do\x01",
            "without any problems here.\x02\x03",

            "And I doubt that those are the only ones.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10F,
        (
            "#1802F#6P...\x02\x03",

            "#1445FAre we going to be all right in here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x109,
        (
            "#1065F#2PHopefully. They were tough, but not so tough we\x01",
            "can't handle them if we're together.\x02\x03",

            "#1060FIt's not like there's anything else for us to do back\x01",
            "in that base area. Let's keep walkin' and see what\x01",
            "we find, I say.\x02\x03",

            "It might be worth going back briefly to check our\x01",
            "orbment setups, though, seeing as we've got more\x01",
            "elements to account for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10F,
        (
            "#1443F#6P...True.\x02\x03",

            "#1446FOh, Kevin.\x01",
            "Let me give you this.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #21
        "\x07\x05Ries handed Kevin the \x1F\x0F\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x20F, 1)

    ChrTalk(    #22
        0x109,
        "#1079F#4PHmm? What's this for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10F,
        (
            "#1448F#6PIt's called a Monster Guide.\x01",
            "It was designed to record data on monsters.\x01",
            "Their habits, their weaknesses, and the like.\x02\x03",

            "I think it would be wise for us to note anything\x01",
            "and everything we come across here.\x02\x03",

            "#1447FAlthough, I suppose 'Fiend Guide' would be\x01",
            "more appropriate here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1840F#4PHaha. You're tellin' me.\x02\x03",

            "#1841FYou sure I can't just store all this info up in the\x01",
            "ol' noggin, though? I'm already putting enough stuff in\x01",
            "the Gralsritter notebook as it is! My hands're gonna\x01",
            "go numb at this rate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10F,
        (
            "#1801F#6P...You complain way too much, Kevin.\x02\x03",

            "#1446FYou're a knight. Do your job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x109,
        (
            "#1068F#4PUgh... Yes, ma'am.\x02\x03",

            "#1066FNo time like the present, I guess.\x02\x03",

            "#1075F*scribble* *scribble*\x02\x03",

            "#1060FThere. Happy?\x02",
        )
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

    # Function_3_D27 end

    def Function_4_1B26(): pass

    label("Function_4_1B26")

    PlayEffect(0x0, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1B61():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1B61)
    OP_22(0x214, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x10, 0x1)
    SetChrFlags(0x10, 0x80)
    Return()

    # Function_4_1B26 end

    def Function_5_1B82(): pass

    label("Function_5_1B82")

    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1BC2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1BC2)
    OP_22(0x214, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x11, 0x1)
    SetChrFlags(0x11, 0x80)
    Return()

    # Function_5_1B82 end

    def Function_6_1BE3(): pass

    label("Function_6_1BE3")

    Sleep(400)
    PlayEffect(0x0, 0xFF, 0xFE, 0, 300, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_1C23():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1C23)
    OP_22(0x214, 0x0, 0x64)
    OP_22(0x99, 0x0, 0x64)
    WaitChrThread(0x12, 0x1)
    SetChrFlags(0x12, 0x80)
    Return()

    # Function_6_1BE3 end

    def Function_7_1C44(): pass

    label("Function_7_1C44")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    ChrTalk(    #27
        0x109,
        "#1079F#5PHuh? What's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10F,
        (
            "#1442F#5PIt's really pretty...\x02\x03",

            "It looks kind of like a cube of septium,\x01",
            "but I don't think that's what it is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x109,
        (
            "#1060F#5PYeah. Maybe we should touch it and see\x01",
            "what happens.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1E3E():
        OP_6D(59080, -60000, -70580, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1E3E)
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

    AnonymousTalk(    #30
        "\x07\x05Found \x1F\x52\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x352, 1)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #31
        0x10F,
        "#1443F#2PDoes it seem harmful?\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #32
        0x109,
        (
            "#1075F#6PNope. Seems safe to me.\x02\x03",

            "#1060FWish I knew what it was, though. The light coming\x01",
            "off it's so...warm.\x02\x03",

            "The kind of slow, rhythmic glowing from it reminds\x01",
            "me of a beating heart in a way.\x02",
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

    ChrTalk(    #33
        0x10F,
        "#1444F#2PWas that...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1063F#5PThere's our cube again.\x02",
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

    AnonymousTalk(    #35
        "\x07\x0C\x18#2S#80WVisitor from afar...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #36
        "\x07\x0C\x18#2S#80WYou who possess the cube...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(300)

    ChrTalk(    #37
        0x10F,
        "#1802F#5PIt's that voice from earlier...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        (
            "#1069F#5PJust who are you?!\x02\x03",

            "Where are you talking to us from?!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #39
        (
            "\x07\x0C\x18#2S#80WRaise that sealing stone before the monument\x01",
            "in the garden...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #40
        "\x07\x0C\x18#2S#80W...then the barrier...and the imprisoned...shall...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)

    ChrTalk(    #41
        0x109,
        (
            "#1063F#5PArgh... I can barely work out what it's trying to\x01",
            "say...\x02\x03",

            "#1069FAll I could get is that we need to take this thing\x01",
            "to the monument.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #42
        "\x07\x0C\x18#2S#80W...I will unlock another power...cube...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #43
        "\x07\x0C\x18#2S#80W...Make use of...it...\x02",
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

    AnonymousTalk(    #44
        "\x07\x05The cube's warp functionality is now available.\x02",
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

    AnonymousTalk(    #45
        (
            "\x07\x05To use it, click the icon at the top-right corner of the\x01",
            "screen, then select the location you wish to warp to.\x02",
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

    ChrTalk(    #46
        0x109,
        "#1079F#5PWh-What the...?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #47
        "\x07\x0C\x18#2S#80WBeware the...malevolent one...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #48
        "\x07\x0C\x18#2S#80WGather strength...or you too will be forever...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, 80, -1, -1)

    AnonymousTalk(    #49
        "\x07\x0C\x18#2S#80W...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)

    def lambda_267C():
        OP_6D(58430, -60000, -70120, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_267C)
    OP_62(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x109)
    OP_63(0x10F)
    Sleep(300)
    WaitChrThread(0xEE, 0x0)
    OP_8C(0x10F, 180, 400)
    Sleep(300)

    ChrTalk(    #50
        0x10F,
        "#1443F#2PUmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x109,
        (
            "#1068F#5PDon't even ask...\x02\x03",

            "I feel like I'm in some kinda weird dream\x01",
            "that just gets freakier by the minute.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(500)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    OP_8C(0x109, 0, 400)
    Sleep(300)

    ChrTalk(    #52
        0x109,
        (
            "#1060F#6PI don't sense anything bad coming from the voice,\x01",
            "at least. More like it's trying to guide us forward.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x10F,
        (
            "#1446F#2PTrue. It does...\x02\x03",

            "#1443FYou don't think the cube has a will of its own\x01",
            "and that it's the thing talking to us, do you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        (
            "#1065F#6PI doubt it. It kept talking about the cube as\x01",
            "if it were a separate object. \x02\x03",

            "My hunch is that the source of the voice is \x01",
            "someone else.\x02\x03",

            "#1063FAnd then there's that 'malevolent one' it\x01",
            "was bringing up, too.\x02\x03",

            "I could see that being that man in black\x01",
            "we saw when we were thrown in here,\x01",
            "but it could very easily be someone else.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x10F,
        "#1445F#2P...All of this is starting to make my head hurt.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x109,
        (
            "#1068F#6PJoin the club...\x02\x03",

            "#1060FWell, let's try and take things one step at\x01",
            "a time, okay?\x02\x03",

            "And on that note, the best place to start is \x01",
            "probably giving the cube's new power a shot.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #57
        0x10F,
        "#1444F#2PYou're serious?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        (
            "#1075F#6PSerious as can be.\x02\x03",

            "#1062FThere aren't many artifacts that have the power\x01",
            "of teleportation, y'know.\x02\x03",

            "And in the situation we're stuck in, we need to\x01",
            "use everything we've got at our disposal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x10F,
        (
            "#1446F#2P...All right.\x02\x03",

            "#1443FBe sure you're careful when using it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        "#1060F#6PI will.\x02",
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

    # Function_7_1C44 end

    def Function_8_2C7C(): pass

    label("Function_8_2C7C")

    OP_C6(0x2, 0x3, -1, 500, 0)
    OP_C6(0x2, 0x4, 0, 0, 0)
    Sleep(500)

    label("loc_2C9F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CE2")
    Sleep(200)
    OP_C6(0x2, 0x3, 16777215, 500, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2CCB")
    Jump("loc_2CE2")

    label("loc_2CCB")

    OP_C6(0x2, 0x3, -1, 500, 0)
    Sleep(500)
    Jump("loc_2C9F")

    label("loc_2CE2")

    Return()

    # Function_8_2C7C end

    def Function_9_2CE3(): pass

    label("Function_9_2CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 5)), scpexpr(EXPR_END)), "loc_2CEE")
    Return()

    label("loc_2CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF7")
    Return()

    label("loc_2CF7")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DAA")
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #61
        0x109,
        (
            "#1078FHold on. Why don't we take this chance to try\x01",
            "using the cube?\x02\x03",

            "I want to see if it really does let us warp.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #62
        0x10F,
        "#1801F...Do we have to?\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E58")

    label("loc_2DAA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E58")
    TurnDirection(0x109, 0x10F, 400)

    ChrTalk(    #63
        0x109,
        (
            "#1078FHold on. Why don't we take this chance to try\x01",
            "using the cube?\x02\x03",

            "I want to see if it really does let us warp.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10F, 0x109, 400)

    ChrTalk(    #64
        0x10F,
        "#1801F...Do we have to?\x02",
    )

    CloseMessageWindow()

    label("loc_2E58")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_9_2CE3 end

    def Function_10_2E74(): pass

    label("Function_10_2E74")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    OP_6D(-4830, -49650, -96300, 0)
    OP_67(0, 5450, -10000, 0)
    OP_6B(4600, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    def lambda_2ECD():
        OP_6B(4200, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2ECD)
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

    # Function_10_2E74 end

    def Function_11_2F16(): pass

    label("Function_11_2F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F22")
    Return()

    label("loc_2F22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 6)), scpexpr(EXPR_END)), "loc_2F2A")
    Return()

    label("loc_2F2A")

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

    ChrTalk(    #65
        0x10F,
        (
            "#1444FHmm?\x02\x03",

            "Wasn't this path blocked before?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x109,
        "#1063FSure was... What's going on?\x02",
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1200)
    OP_8C(0x107, 315, 400)
    Sleep(300)

    ChrTalk(    #67
        0x107,
        "#064F#6PIs something wrong?\x02",
    )

    CloseMessageWindow()

    def lambda_306E():
        OP_6D(2100, -52000, -97400, 1300)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_306E)

    def lambda_3086():
        OP_67(0, 5980, -10000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3086)

    def lambda_309E():
        OP_6B(4000, 1300)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_309E)

    def lambda_30AE():
        OP_8C(0x10F, 180, 400)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_30AE)
    Sleep(100)
    OP_8C(0x109, 90, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #68
        0x10F,
        (
            "#1443F#2PThe last time we passed by here, this path was\x01",
            "blocked by some kind of barrier.\x02\x03",

            "But as you can see, it's nowhere to be seen now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x107,
        (
            "#063F#6PReally...?\x02\x03",

            "I wonder what could have caused that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x109,
        (
            "#1065F#5PWell, if we think about what's changed since\x01",
            "when we last passed here and now...\x02\x03",

            "#1063F...maybe it was releasing Tita from that stone\x01",
            "that caused it to disappear?\x02\x03",

            "I mean, we haven't done anything else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x107,
        (
            "#064F#6PO-Oh, I see...\x02\x03",

            "#561FStill, that actually could be it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        "#1064F#5PHuh? You think?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x107,
        (
            "#062F#6PThink about it. The stone with me inside was\x01",
            "near here, too, right? Maybe that was more\x01",
            "than a coincidence.\x02\x03",

            "This could be among one of the many rules\x01",
            "that govern this place that we just haven't\x01",
            "figured out yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        "#1063F#5PRules?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x10F,
        (
            "#1447F#2P...Hmm. I think I get what you're trying to say.\x02\x03",

            "#1448FSo in this case, we wouldn't have been able to\x01",
            "advance any farther if we hadn't released you\x01",
            "from that stone?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x107,
        (
            "#560F#6PThat's right. I can't be sure, but I do have\x01",
            "a good feeling about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x109,
        (
            "#1060F#5PAnd a good feeling is good enough for me right\x01",
            "now.\x02\x03",

            "#1065FWe still don't have a clue who's responsible\x01",
            "for the situation we're in, but it all feels very\x01",
            "deliberately set up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x10F,
        (
            "#1443F#2PWhich is all the reason we'll need to be careful,\x01",
            "I suppose.\x02",
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

    # Function_11_2F16 end

    def Function_12_35F4(): pass

    label("Function_12_35F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 7)), scpexpr(EXPR_END)), "loc_35FC")
    Return()

    label("loc_35FC")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3649")
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #79
        0x109,
        "#1079F#12PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DB")

    label("loc_3649")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3694")
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x10F, 270, 400)
    Sleep(300)

    ChrTalk(    #80
        0x10F,
        "#1444F#12PHuh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_36DB")

    label("loc_3694")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36DB")
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x107, 270, 400)
    Sleep(300)

    ChrTalk(    #81
        0x107,
        "#064F#12PHuh?\x02",
    )

    CloseMessageWindow()

    label("loc_36DB")

    Sleep(300)

    def lambda_36E6():
        OP_6D(-47880, -52000, -80330, 3500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_36E6)

    def lambda_36FE():
        OP_67(0, 5600, -10000, 3500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_36FE)

    def lambda_3716():
        OP_6B(3500, 3500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3716)

    def lambda_3726():
        OP_6C(315000, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_3726)

    def lambda_3736():
        OP_6E(255, 3500)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_3736)

    def lambda_3746():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_3746)
    OP_8C(0x2, 270, 400)
    WaitChrThread(0x109, 0x0)
    Sleep(1000)

    def lambda_3765():
        OP_6D(-46610, -52000, -80360, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3765)

    def lambda_377D():
        OP_67(0, 5000, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_377D)

    def lambda_3795():
        OP_6B(3550, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_3795)
    SetChrPos(0x109, -36110, -52000, -82630, 270)
    SetChrPos(0x10F, -35600, -52000, -81580, 270)
    SetChrPos(0x107, -34670, -52000, -82170, 270)

    def lambda_37D8():
        OP_8E(0xFE, 0xFFFF539E, 0xFFFF34E0, 0xFFFEBC04, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_37D8)
    Sleep(300)

    def lambda_37F8():
        OP_8E(0xFE, 0xFFFF5416, 0xFFFF34E0, 0xFFFEC12C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10F, 0, lambda_37F8)
    Sleep(400)

    def lambda_3818():
        OP_8E(0xFE, 0xFFFF59C0, 0xFFFF34E0, 0xFFFEBE5C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3818)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #82
        0x109,
        "#1063FWhat's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x10F,
        "#1444F#2PA shining door with a moon on it..?\x02",
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

    AnonymousTalk(    #84
        "\x07\x05#2S#40WWelcome...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 90, -1, -1)

    AnonymousTalk(    #85
        (
            "\x07\x05#40WBring to me the girl skilled in orbal engineering.\x01\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)
    OP_62(0x107, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    ChrTalk(    #86
        0x107,
        (
            "#065F#12PWh-Whoa! I could hear a voice talking right\x01",
            "into my mind!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        (
            "#1063FIt looks like this door's got a will of its own\x01",
            "like the tree, spring, and monument back in\x01",
            "the garden.\x02\x03",

            "#1065FThere'll come a day when I get used to all\x01",
            "these funky talking objects, I'm sure...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10F,
        (
            "#1802F#2PI can only think of one person who\x01",
            "might fit the door's description...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3B7B():
        OP_8C(0x109, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3B7B)
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

    ChrTalk(    #89
        0x107,
        "#065F#12PY-You think it means me?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10F,
        "#1446F#5PMost likely.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x109,
        (
            "#1068F#5PIt's a pretty terrible riddle.\x01",
            "It's sure not me or Ries.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x109, 270, 400)

    ChrTalk(    #92
        0x109,
        "#1063FHey, door. It's her you mean, right?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10F, 270, 400)
    Sleep(150)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)

    AnonymousTalk(    #93
        "\x07\x05#2S#40WIndeed... She is the one I seek.\x02",
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

    AnonymousTalk(    #94
        (
            "\x07\x05#40WOnly she may enter...\x01",
            "#500W \x01",
            "#40WIf she fears not the trial within,\x01",
            "she should step forth through the door.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #95
        0x107,
        "#065F#12PT-T-Trial?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x109,
        (
            "#1063FMaybe it wants to test your strength to see\x01",
            "if you're worthy of...something.\x02\x03",

            "And apparently, we can't even go inside to\x01",
            "back you up in it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x10F,
        (
            "#1443F#2PThat's ludicrous.\x02\x03",

            "#1446F#2PI propose we disregard this door and move on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x107,
        (
            "#561F#12P...\x02\x03",

            "#062FW-Wait!\x02\x03",

            "I'm going to go inside!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3FB1():
        OP_8C(0x109, 90, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3FB1)
    Sleep(100)
    OP_8C(0x10F, 135, 500)

    ChrTalk(    #99
        0x10F,
        "#1444F#5PBut, Tita...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x109,
        "#1069F#5PHold on just a sec! There's no way...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x107,
        (
            "#062F#12PI feel like this might be another of the 'rules'\x01",
            "I was talking about earlier.\x02\x03",

            "And besides, we've got so little to work with as\x01",
            "we try to get out of here. We need all the clues\x01",
            "and help we can get.\x02\x03",

            "If it seems like it'll be too dangerous, I'll come\x01",
            "right back out. I promise!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x10F,
        "#1802F#5PWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x109,
        (
            "#1065F#5P...\x02\x03",

            "#1063FAll right. We're counting on you.\x02\x03",

            "But like you said, if it seems too dangerous,\x01",
            "come right back out. Don't expose yourself\x01",
            "to any more danger than you need to.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x10F,
        "#1448F#5PDo be careful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x107,
        "#560F#12PI will!\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_4245():
        OP_6D(-47050, -52000, -80660, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4245)
    OP_43(0x109, 0x0, 0x0, 0xD)
    OP_43(0x10F, 0x0, 0x0, 0xE)
    Sleep(300)

    def lambda_4270():
        OP_8E(0xFE, 0xFFFF50E2, 0xFFFF34E0, 0xFFFEBDDA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_4270)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10F, 0x3)
    OP_8C(0x109, 270, 400)
    OP_8C(0x10F, 270, 400)
    WaitChrThread(0x109, 0x1)
    Sleep(1000)

    def lambda_42BA():
        OP_8E(0xFE, 0xFFFF4912, 0xFFFF34E0, 0xFFFEBFBA, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_42BA)

    def lambda_42D5():
        OP_6B(2900, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_42D5)
    Sleep(1300)
    OP_22(0x99, 0x0, 0x64)

    def lambda_42EF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x258)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_42EF)
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

    # Function_12_35F4 end

    def Function_13_4362(): pass

    label("Function_13_4362")


    def lambda_4368():

        label("loc_4368")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4368")

    QueueWorkItem2(0x109, 3, lambda_4368)
    Sleep(50)
    OP_8F(0x109, 0xFFFF565A, 0xFFFF34E0, 0xFFFEB92A, 0x3E8, 0x0)
    Return()

    # Function_13_4362 end

    def Function_14_438D(): pass

    label("Function_14_438D")


    def lambda_4393():

        label("loc_4393")

        TurnDirection(0xFE, 0x107, 400)
        OP_48()
        Jump("loc_4393")

    QueueWorkItem2(0x10F, 3, lambda_4393)
    Sleep(150)
    OP_8F(0x10F, 0xFFFF5628, 0xFFFF34E0, 0xFFFEC1E0, 0x3E8, 0x0)
    Return()

    # Function_14_438D end

    def Function_15_43B8(): pass

    label("Function_15_43B8")

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

    def lambda_449A():
        OP_6D(-45030, -52000, -80710, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_449A)

    def lambda_44B2():
        OP_6B(2950, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_44B2)
    OP_22(0x99, 0x0, 0x64)

    def lambda_44C7():
        OP_8E(0xFE, 0xFFFF52F4, 0xFFFF34E0, 0xFFFEBF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_44C7)

    def lambda_44E2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_44E2)
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

    ChrTalk(    #106
        0x109,
        "#1840FThank Aidios! You're all right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x10F,
        "#1802F#12PAre you feeling okay? You look quite tired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x107,
        (
            "#563F#5PHeehee. I'm fine!\x02\x03",

            "#066FI did have to fight some scary enemies,\x01",
            "but I managed to pull through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x109,
        (
            "#1075FThat's good...\x02\x03",

            "#1063FSo what happened in there?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x107,
        "#062F#5PWell...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #111
        "\x07\x05Tita explained everything that happened on the other side of the door.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()

    ChrTalk(    #112
        0x10F,
        "#1444F#12PI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x109,
        (
            "#1067FYep. Sounds like this is another one of our rules,\x01",
            "all right.\x02\x03",

            "#1065FIn other words, first you need to meet some \x01",
            "condition or conditions to get the door to open.\x02\x03",

            "After that, you fight your way through a battle,\x01",
            "or trial...\x02\x03",

            "Win, and you get to see some kind of 'memory\x01",
            "fragment' and walk away with mira as a bonus.\x02\x03",

            "#1060FThat sum things up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x107,
        (
            "#560F#5PYeah... That's how it was for me.\x02\x03",

            "The memory fragment didn't feel like it was quite\x01",
            "finished, though. There seemed to be more that I\x01",
            "didn't get to see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x109,
        (
            "#1065FHmm...\x02\x03",

            "Maybe there's more than one pattern to these\x01",
            "doors, then.\x02\x03",

            "#1060FEither way, every time we find one, we should\x01",
            "probably note its location and conditions down.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x10F,
        "#1448F#12PIndeed.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #117
        "\x07\x05About Memory Doors\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    AnonymousTalk(    #118
        (
            "\x07\x05Memory Doors are located throughout \x01",
            "the game and allow you to see various\x01",
            "optional scenes. In all, there are three \x01",
            "types of doors.\x02\x03",

            "Moon Doors - Contain lengthy side stories.\x01",
            "Star Doors - Contain short side stories.\x01",
            "Sun Doors - Contain minigames.\x02\x03",

            "In order to open a door, you will need to\x01",
            "fulfill one or multiple conditions.\x02\x03",

            "Furthermore, some doors will require\x01",
            "certain characters to win a battle in\x01",
            "order to view the contents within.\x02\x03",

            "After viewing the contents of a door for \x01",
            "the first time, you will earn mira, and \x01",
            "depending on your choices or actions,\x01",
            "potentially even bonuses such as items.\x02\x03",

            "All of this information is automatically\x01",
            "recorded in the notebook and can be\x01",
            "viewed at any time.\x02\x03",

            "Finally, you can also warp to any door\x01",
            "you have discovered using the cube.\x02",
        )
    )

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

    # Function_15_43B8 end

    def Function_16_4D92(): pass

    label("Function_16_4D92")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E35")
    OP_28(0x2, 0x4, 0x2)

    label("loc_4E35")

    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_C4(0x0, 0x800)
    SetChrName("")
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #119
        (
            "\x07\x05#40WBring to me the girl skilled in orbal engineering,\x01",
            "accompanied by an ever-burning flame.\x01\x01",
            "Only then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F0F")
    Call(0, 17)
    Jump("loc_4F24")

    label("loc_4F0F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F24")
    Call(0, 17)
    Jump("loc_4F24")

    label("loc_4F24")

    FadeToBright(300, 0)
    EventEnd(0x0)
    Return()

    # Function_16_4D92 end

    def Function_17_4F30(): pass

    label("Function_17_4F30")

    SetMessageWindowPos(-1, 110, -1, -1)
    SetChrName("")

    AnonymousTalk(    #120
        "\x07\x05Open the Door?\x18\x02",
    )


    label("loc_4F4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_509D")
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "View Part 1\x01",      # 0
            "View Part 2\x01",      # 1
            "Quit\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    OP_56(0x0)
    Sleep(300)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4FB6"),
        (1, "loc_4FC0"),
        (2, "loc_5080"),
        (SWITCH_DEFAULT, "loc_508D"),
    )


    label("loc_4FB6")

    OP_A3(0x0)
    Call(0, 18)
    Jump("loc_509A")

    label("loc_4FC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4FE3")
    OP_A2(0x0)
    Call(0, 18)
    Jump("loc_507D")

    label("loc_4FE3")

    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #121
        (
            "\x07\x05#40WWhen you have met my conditions, return to me once\x01",
            "more.\x01",
            "#500W \x01",
            "#40WOnly then shall the door open...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_507D")

    Jump("loc_509A")

    label("loc_5080")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_509A")

    label("loc_508D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_509A")

    label("loc_509A")

    Jump("loc_4F4F")

    label("loc_509D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_4F30 end

    def Function_18_50A8(): pass

    label("Function_18_50A8")

    FadeToBright(300, 0)
    Sleep(500)
    PlayEffect(0x85, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    Sleep(300)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x3)
    Sleep(500)

    def lambda_5111():
        OP_6B(4460, 3000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_5111)
    OP_22(0x138, 0x0, 0x64)
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(2000, 16777215)
    OP_0D()
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C4(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_515E")
    OP_E3(0x0, 0x1A, 0, 0x0)
    Jump("loc_5166")

    label("loc_515E")

    OP_E3(0x0, 0x19, 0, 0x0)

    label("loc_5166")

    NewScene("ED6_DT21/P9000   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_18_50A8 end

    def Function_19_5170(): pass

    label("Function_19_5170")

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

    # Function_19_5170 end

    def Function_20_521B(): pass

    label("Function_20_521B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_522C")
    Call(0, 2)
    Return()

    label("loc_522C")

    OP_DE(0x0, 0x0, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_20_521B end

    def Function_21_530A(): pass

    label("Function_21_530A")

    OP_DE(0x0, 0x1, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_21_530A end

    def Function_22_53BD(): pass

    label("Function_22_53BD")

    OP_DE(0x0, 0x2, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_22_53BD end

    def Function_23_5470(): pass

    label("Function_23_5470")

    OP_DE(0x0, 0x3, 0x1)
    EventBegin(0x2)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_23_5470 end

    def Function_24_554E(): pass

    label("Function_24_554E")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_24_554E end

    def Function_25_560A(): pass

    label("Function_25_560A")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_25_560A end

    def Function_26_56C6(): pass

    label("Function_26_56C6")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_26_56C6 end

    def Function_27_5782(): pass

    label("Function_27_5782")

    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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

    # Function_27_5782 end

    def Function_28_583E(): pass

    label("Function_28_583E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5867")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_585B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_585B)

    label("loc_5867")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5890")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5884():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_5884)

    label("loc_5890")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58B9")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_58AD():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_58AD)

    label("loc_58B9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58E2")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_58D6():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_58D6)

    label("loc_58E2")

    Sleep(800)
    OP_44(0x0, 0x1)
    OP_44(0x1, 0x1)
    OP_44(0x2, 0x1)
    OP_44(0x3, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_590E")
    OP_9F(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_590E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5925")
    OP_9F(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5925")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_593C")
    OP_9F(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_593C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5953")
    OP_9F(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_5953")

    Return()

    # Function_28_583E end

    def Function_29_5954(): pass

    label("Function_29_5954")


    def lambda_595A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_595A)

    def lambda_596C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_596C)

    def lambda_597E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_597E)

    def lambda_5990():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_5990)
    Sleep(1000)
    Return()

    # Function_29_5954 end

    def Function_30_59A2(): pass

    label("Function_30_59A2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A7B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x291, 1)"), scpexpr(EXPR_END)), "loc_5A10")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #122
        "\x07\x05Found \x1F\x91\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2681)
    Jump("loc_5A78")

    label("loc_5A10")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #123
        (
            "\x07\x05Found \x1F\x91\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x91\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_5A78")

    Jump("loc_5B6E")

    label("loc_5A7B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #124
        (
            "\x07\x05Did you know? It's true that Zin's name was once written as 'Zane,' but\x01",
            "another name change considered was Olivier's. The original suggestion\x01",
            "was 'Oliver.' This chest is glad that request never went through.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA1, 0x0)

    label("loc_5B6E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_30_59A2 end

    def Function_31_5B7C(): pass

    label("Function_31_5B7C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C55")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_5BEA")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #125
        "\x07\x05Found \x1F\xF5\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2682)
    Jump("loc_5C52")

    label("loc_5BEA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #126
        (
            "\x07\x05Found \x1F\xF5\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF5\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_5C52")

    Jump("loc_5CA0")

    label("loc_5C55")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #127
        "\x07\x05I'm here because they ran out of jokes.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0xA2, 0x0)

    label("loc_5CA0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_31_5B7C end

    def Function_32_5CAE(): pass

    label("Function_32_5CAE")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4D0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D19")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x1E)
    OP_73(0x2)
    OP_6F(0x2, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(300)

    AnonymousTalk(    #128
        "\x07\x05Received \x07\x02300 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2683)
    Jump("loc_5D4A")

    label("loc_5D19")


    AnonymousTalk(    #129
        "\x07\x05A chest, a chest! My kingdom for a chest!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5D4A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0xA3, 0x0)
    Return()

    # Function_32_5CAE end

    SaveToFile()

Try(main)
