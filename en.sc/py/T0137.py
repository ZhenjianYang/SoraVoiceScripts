from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        'Blueberry Muffin',                     # 9
        'Jam',                                  # 10
        'Bacon',                                # 11
        'Orange Juice',                         # 12
        'Milk',                                 # 13
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
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
        TalkFunctionIndex   = 9,
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
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1A3",          # 01, 1
        "Function_2_1EC",          # 02, 2
        "Function_3_3D5",          # 03, 3
        "Function_4_3EB",          # 04, 4
        "Function_5_440",          # 05, 5
        "Function_6_47D",          # 06, 6
        "Function_7_4C3",          # 07, 7
        "Function_8_504",          # 08, 8
        "Function_9_551",          # 09, 9
        "Function_10_55B",         # 0A, 10
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DE")
    SetMapFlags(0x10)
    OP_11(0x4B, 0x4B, 0x96, 0x0, 0xEA60, 0x0)
    OP_E8(0xD0, 0x7, 0x0, 0x0)

    label("loc_1DE")

    Jump("loc_1EB")

    label("loc_1E1")

    ClearMapFlags(0x10)
    OP_E8(0xE8, 0x3, 0x0, 0x0)

    label("loc_1EB")

    Return()

    # Function_1_1A3 end

    def Function_2_1EC(): pass

    label("Function_2_1EC")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x40)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22E")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_IMOD), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_23B")

    label("loc_22E")

    OP_51(0xFE, 0x4, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_IMOD), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_23B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3D4")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x1), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x3), scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_SUB), scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x3), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_391")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B")
    Sleep(250)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B")
    Sleep(500)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30B")
    Sleep(500)

    label("loc_30B")

    OP_44(0xFE, 0x1)
    TurnDirection(0xFE, 0x0, 0)

    def lambda_31C():
        OP_94(0x0, 0xFE, 0xB4, 0x7530, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31C)
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0xFE, 0x2, 0x0, 0x3)
    SetChrChipByIndex(0xFE, 0)
    ClearChrFlags(0xFE, 0x400)
    SetChrFlags(0xFE, 0x4)
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_358")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_385")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_37D")
    Jump("loc_385")

    label("loc_37D")

    Sleep(15)
    Jump("loc_358")

    label("loc_385")

    OP_44(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Jump("loc_3D1")

    label("loc_391")

    Sleep(100)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B5")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_3D1")

    label("loc_3B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3D1")
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_3D1")

    Jump("loc_23B")

    label("loc_3D4")

    Return()

    # Function_2_1EC end

    def Function_3_3D5(): pass

    label("Function_3_3D5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EA")
    OP_99(0xFE, 0x0, 0x7, 0x1770)
    Jump("Function_3_3D5")

    label("loc_3EA")

    Return()

    # Function_3_3D5 end

    def Function_4_3EB(): pass

    label("Function_4_3EB")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #0
        0xFE,
        "*chirp chirp chirp chirp chirp...*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_4_3EB end

    def Function_5_440(): pass

    label("Function_5_440")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #1
        0xFE,
        "*chirr...*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_5_440 end

    def Function_6_47D(): pass

    label("Function_6_47D")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)
    OP_EA(0x0, 0x1, 0x0, 0x0)

    ChrTalk(    #2
        0xFE,
        "*chirp chirp!*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_6_47D end

    def Function_7_4C3(): pass

    label("Function_7_4C3")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #3
        0xFE,
        "*CHIRP!!*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_7_4C3 end

    def Function_8_504(): pass

    label("Function_8_504")

    OP_4A(0xFE, 255)
    TalkBegin(0xFE)
    OP_62(0xFE, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(1000)

    ChrTalk(    #4
        0xFE,
        "*chirp chirp chirrrr*\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    OP_4B(0xFE, 255)
    Return()

    # Function_8_504 end

    def Function_9_551(): pass

    label("Function_9_551")

    NewScene("ED6_DT21/T0137   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_9_551 end

    def Function_10_55B(): pass

    label("Function_10_55B")

    NewScene("ED6_DT21/T0137   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_10_55B end

    SaveToFile()

Try(main)
