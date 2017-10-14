from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1600   ._SN',
        MapName             = 'Bose',
        Location            = 'C1600.x',
        MapIndex            = 60,
        MapDefaultBGM       = "ed60125",
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
        'Silver-Haired Youth',                  # 9
        'Weissmann',                            # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT29/CH12450 ._CH',             # 00
        'ED6_DT29/CH12451 ._CH',             # 01
        'ED6_DT09/CH10840 ._CH',             # 02
        'ED6_DT09/CH10841 ._CH',             # 03
        'ED6_DT29/CH12460 ._CH',             # 04
        'ED6_DT29/CH12461 ._CH',             # 05
        'ED6_DT09/CH10550 ._CH',             # 06
        'ED6_DT09/CH10551 ._CH',             # 07
        'ED6_DT29/CH12500 ._CH',             # 08
        'ED6_DT29/CH12501 ._CH',             # 09
        'ED6_DT29/CH12560 ._CH',             # 0A
        'ED6_DT29/CH12561 ._CH',             # 0B
        'ED6_DT07/CH02040 ._CH',             # 0C
        'ED6_DT27/CH03550 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT29/CH12450P._CP',             # 00
        'ED6_DT29/CH12451P._CP',             # 01
        'ED6_DT09/CH10840P._CP',             # 02
        'ED6_DT09/CH10841P._CP',             # 03
        'ED6_DT29/CH12460P._CP',             # 04
        'ED6_DT29/CH12461P._CP',             # 05
        'ED6_DT09/CH10550P._CP',             # 06
        'ED6_DT09/CH10551P._CP',             # 07
        'ED6_DT29/CH12500P._CP',             # 08
        'ED6_DT29/CH12501P._CP',             # 09
        'ED6_DT29/CH12560P._CP',             # 0A
        'ED6_DT29/CH12561P._CP',             # 0B
        'ED6_DT07/CH02040P._CP',             # 0C
        'ED6_DT27/CH03550P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -5230,
        Z                   = 4000,
        Y                   = -12590,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 28010,
        Z                   = 6000,
        Y                   = -9400,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 21830,
        Z                   = 6560,
        Y                   = -1430,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -35520,
        Z                   = 16000,
        Y                   = 14970,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 8390,
        Z                   = 16000,
        Y                   = -3360,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 25620,
        Z                   = 22000,
        Y                   = 15270,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x3C4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_269",          # 01, 1
        "Function_2_286",          # 02, 2
        "Function_3_398",          # 03, 3
        "Function_4_3E2",          # 04, 4
        "Function_5_42C",          # 05, 5
        "Function_6_43B",          # 06, 6
    )


    def Function_0_202(): pass

    label("Function_0_202")

    OP_11(0xFF, 0xFF, 0xFF, 0xAFC8, 0x11170, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_233")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    OP_B5(0x0)
    Event(0, 2)
    Jump("loc_268")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_249")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_268")

    label("loc_249")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (102, "loc_255"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x345, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_265")
    Event(0, 5)

    label("loc_265")

    Jump("loc_268")

    label("loc_268")

    Return()

    # Function_0_202 end

    def Function_1_269(): pass

    label("Function_1_269")

    OP_C4(0x0, 0x4)
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_269 end

    def Function_2_286(): pass

    label("Function_2_286")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-860, 4000, -2200, 0)
    OP_67(0, 11370, -10000, 0)
    OP_6B(3300, 0)
    OP_6C(10000, 0)
    OP_6E(545, 0)
    SetMapFlags(0x10)
    OP_11(0xC8, 0xC8, 0xC8, 0x7530, 0xAFC8, 0x0)
    FadeToBright(2000, 0)

    def lambda_2FE():
        OP_6D(-4920, 22000, 20420, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FE)

    def lambda_316():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_316)

    def lambda_326():
        OP_67(0, 7350, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_326)
    Sleep(2000)
    OP_43(0x9, 0x0, 0x0, 0x3)
    Sleep(500)
    OP_43(0x8, 0x0, 0x0, 0x4)
    WaitChrThread(0x101, 0x1)

    def lambda_35B():
        OP_6B(3800, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35B)

    def lambda_36B():
        OP_6E(262, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36B)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1603   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_286 end

    def Function_3_398(): pass

    label("Function_3_398")

    SetChrPos(0xFE, -920, 22000, 11580, 315)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFEA84, 0x55F0, 0x36C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEA84, 0x55F0, 0x5BCC, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_3_398 end

    def Function_4_3E2(): pass

    label("Function_4_3E2")

    SetChrPos(0xFE, 640, 22000, 11430, 315)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF038, 0x55F0, 0x3606, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFEF2A, 0x55F0, 0x5BCC, 0x7D0, 0x0)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_4_3E2 end

    def Function_5_42C(): pass

    label("Function_5_42C")

    EventBegin(0x0)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_42C end

    def Function_6_43B(): pass

    label("Function_6_43B")

    EventBegin(0x0)
    OP_6D(-5920, 10000, 180, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3800, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -5920, 10000, 180, 180)
    SetChrPos(0x106, -5920, 10000, 180, 180)
    SetChrPos(0x107, -5920, 10000, 180, 180)
    SetChrPos(0xF9, -5920, 10000, 180, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_A2(0x1A29)
    EventEnd(0x0)
    Return()

    # Function_6_43B end

    SaveToFile()

Try(main)
