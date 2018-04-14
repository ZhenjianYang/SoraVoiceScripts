from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0137   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0137.x',
        MapIndex            = 10,
        MapDefaultBGM       = "ed60084",
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
        '鸽子',                                 # 9
        '鸽子',                                 # 10
        '鸽子',                                 # 11
        '鸽子',                                 # 12
        '鸽子',                                 # 13
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
        'ED6_DT07/CH01730 ._CH',             # 00
        'ED6_DT07/CH01731 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01730P._CP',             # 00
        'ED6_DT07/CH01731P._CP',             # 01
    )

    DeclNpc(
        X                   = 54080,
        Z                   = 11330,
        Y                   = 43400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 54640,
        Z                   = 11330,
        Y                   = 43420,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55240,
        Z                   = 11330,
        Y                   = 43310,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55740,
        Z                   = 10630,
        Y                   = 43210,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 55640,
        Z                   = 11330,
        Y                   = 43400,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -300,
        TriggerZ            = 0,
        TriggerY            = 4140,
        TriggerRange        = 800,
        ActorX              = -300,
        ActorZ              = 1000,
        ActorY              = 4140,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 53450,
        TriggerZ            = 10300,
        TriggerY            = 47970,
        TriggerRange        = 800,
        ActorX              = 53450,
        ActorZ              = 10000,
        ActorY              = 47970,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1A3",          # 01, 1
        "Function_2_1E2",          # 02, 2
        "Function_3_389",          # 03, 3
        "Function_4_39F",          # 04, 4
        "Function_5_3A9",          # 05, 5
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Return()

    # Function_0_1A2 end

    def Function_1_1A3(): pass

    label("Function_1_1A3")

    OP_82(0x86, 0x2)
    OP_82(0x87, 0x2)
    OP_82(0x88, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D9")
    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xEA60, 0x0)

    label("loc_1D9")

    Jump("loc_1E1")

    label("loc_1DC")

    ClearMapFlags(0x10)

    label("loc_1E1")

    Return()

    # Function_1_1A3 end

    def Function_2_1E2(): pass

    label("Function_2_1E2")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_224")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_IMOD), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_231")

    label("loc_224")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_IMOD), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_231")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_388")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_345")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BF")
    Sleep(50)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BF")
    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2BF")
    Sleep(100)

    label("loc_2BF")

    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)

    def lambda_2D0():
        OP_94(0x0, 0xFE, 0xB4, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D0)
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xFE, 0x2, 0x0, 0x3)
    SetChrChipByIndex(0xFE, 0)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_339")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_331")
    Jump("loc_339")

    label("loc_331")

    Sleep(15)
    Jump("loc_30C")

    label("loc_339")

    OP_44(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_385")

    label("loc_345")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_369")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_385")

    label("loc_369")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_385")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_385")

    Jump("loc_231")

    label("loc_388")

    Return()

    # Function_2_1E2 end

    def Function_3_389(): pass

    label("Function_3_389")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_39E")
    OP_99(0xFE, 0x0, 0x7, 0x1770)
    Jump("Function_3_389")

    label("loc_39E")

    Return()

    # Function_3_389 end

    def Function_4_39F(): pass

    label("Function_4_39F")

    NewScene("ED6_DT21/T0137   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_4_39F end

    def Function_5_3A9(): pass

    label("Function_5_3A9")

    NewScene("ED6_DT21/T0137   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_3A9 end

    SaveToFile()

Try(main)
