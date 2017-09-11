from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4302   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4302.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60017",
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
        'Sergeant',                             # 9
        'Special Ops Soldier',                  # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Special Ops Soldier',                  # 16
        'Special Ops Soldier',                  # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Military K-9',                         # 20
        'Military K-9',                         # 21
        'Military K-9',                         # 22
        'Military K-9',                         # 23
        'Military K-9',                         # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Kloe',                                 # 29
        'Scherazard',                           # 30
        'Olivier',                              # 31
        'Nial',                                 # 32
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
        'ED6_DT07/CH01330 ._CH',             # 00
        'ED6_DT07/CH01610 ._CH',             # 01
        'ED6_DT09/CH10060 ._CH',             # 02
        'ED6_DT07/CH01320 ._CH',             # 03
        'ED6_DT07/CH00100 ._CH',             # 04
        'ED6_DT07/CH00101 ._CH',             # 05
        'ED6_DT07/CH00110 ._CH',             # 06
        'ED6_DT07/CH00111 ._CH',             # 07
        'ED6_DT07/CH00170 ._CH',             # 08
        'ED6_DT07/CH00171 ._CH',             # 09
        'ED6_DT07/CH00340 ._CH',             # 0A
        'ED6_DT07/CH00341 ._CH',             # 0B
        'ED6_DT07/CH00342 ._CH',             # 0C
        'ED6_DT07/CH00040 ._CH',             # 0D
        'ED6_DT07/CH00020 ._CH',             # 0E
        'ED6_DT07/CH00030 ._CH',             # 0F
        'ED6_DT07/CH02060 ._CH',             # 10
        'ED6_DT06/CH20116 ._CH',             # 11
        'ED6_DT06/CH20117 ._CH',             # 12
    )

    AddCharChipPat(
        'ED6_DT07/CH01330P._CP',             # 00
        'ED6_DT07/CH01610P._CP',             # 01
        'ED6_DT09/CH10060P._CP',             # 02
        'ED6_DT07/CH01320P._CP',             # 03
        'ED6_DT07/CH00100P._CP',             # 04
        'ED6_DT07/CH00101P._CP',             # 05
        'ED6_DT07/CH00110P._CP',             # 06
        'ED6_DT07/CH00111P._CP',             # 07
        'ED6_DT07/CH00170P._CP',             # 08
        'ED6_DT07/CH00171P._CP',             # 09
        'ED6_DT07/CH00340P._CP',             # 0A
        'ED6_DT07/CH00341P._CP',             # 0B
        'ED6_DT07/CH00342P._CP',             # 0C
        'ED6_DT07/CH00040P._CP',             # 0D
        'ED6_DT07/CH00020P._CP',             # 0E
        'ED6_DT07/CH00030P._CP',             # 0F
        'ED6_DT07/CH02060P._CP',             # 10
        'ED6_DT06/CH20116P._CP',             # 11
        'ED6_DT06/CH20117P._CP',             # 12
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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


    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 1000,
        TriggerY            = 20390,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = 20390,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_466",          # 00, 0
        "Function_1_4E4",          # 01, 1
        "Function_2_4F7",          # 02, 2
        "Function_3_79C",          # 03, 3
        "Function_4_1128",         # 04, 4
        "Function_5_1163",         # 05, 5
        "Function_6_1244",         # 06, 6
        "Function_7_133E",         # 07, 7
        "Function_8_1ACA",         # 08, 8
    )


    def Function_0_466(): pass

    label("Function_0_466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_477")
    OP_A3(0x3FA)
    Event(0, 2)
    Jump("loc_4E3")

    label("loc_477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_488")
    OP_A3(0x3FB)
    Event(0, 5)
    Jump("loc_4E3")

    label("loc_488")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_4A2")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 6)
    Jump("loc_4E3")

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 5)), scpexpr(EXPR_END)), "loc_4C1")
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FD)
    Event(0, 7)
    Jump("loc_4E3")

    label("loc_4C1")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_4CD"),
        (SWITCH_DEFAULT, "loc_4E3"),
    )


    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E0")
    OP_A2(0x652)
    Event(0, 3)

    label("loc_4E0")

    Jump("loc_4E3")

    label("loc_4E3")

    Return()

    # Function_0_466 end

    def Function_1_4E4(): pass

    label("Function_1_4E4")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8900, 0x30061)
    Return()

    # Function_1_4E4 end

    def Function_2_4F7(): pass

    label("Function_2_4F7")

    EventBegin(0x0)
    OP_6D(-70, 0, 20900, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(0, 0)
    OP_6E(408, 0)

    def lambda_53C():
        OP_6D(-700, 0, 46980, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_53C)

    def lambda_554():
        OP_6C(314000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_554)

    def lambda_564():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_564)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x8, -70, 1000, 50380, 180)
    SetChrPos(0x9, 730, 0, 46530, 0)
    SetChrPos(0xA, 2350, 0, 46770, 315)
    SetChrPos(0xB, 2090, 0, 45430, 332)
    SetChrPos(0xC, 1380, 0, 44350, 351)
    SetChrPos(0xD, 470, 0, 43290, 7)
    SetChrPos(0xE, -920, 0, 43360, 353)
    SetChrPos(0xF, -2230, 0, 44390, 7)
    SetChrPos(0x10, -1210, 0, 45310, 16)
    SetChrPos(0x11, -2029, 0, 46530, 25)
    SetChrPos(0x12, -690, 0, 46650, 7)
    SetChrPos(0x13, -3190, 0, 43920, 33)
    SetChrPos(0x14, -3130, 250, 47070, 62)
    SetChrPos(0x15, 3260, 0, 45110, 307)
    SetChrPos(0x16, 80, 0, 44910, 349)
    SetChrPos(0x17, 1250, 0, 42490, 5)
    Sleep(5000)

    ChrTalk(    #0
        0x8,
        (
            "Listen up! We have word from\x01",
            "the I.D. ship!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "We apparently have a lock on\x01",
            "the Royal Guardsman!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "If we get there quickly, this will\x01",
            "be our chance to wipe them out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        "Roger!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4103   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_4F7 end

    def Function_3_79C(): pass

    label("Function_3_79C")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0x9, 12)
    SetChrChipByIndex(0xA, 10)
    SetChrChipByIndex(0xB, 10)
    SetChrChipByIndex(0xC, 10)
    SetChrChipByIndex(0xD, 10)
    SetChrChipByIndex(0xE, 10)
    SetChrChipByIndex(0x101, 4)
    SetChrChipByIndex(0x102, 6)
    SetChrChipByIndex(0x108, 8)
    SetChrPos(0x108, 70, 0, 26850, 356)
    SetChrPos(0x101, -640, 0, 26250, 315)
    SetChrPos(0x102, 1000, 0, 26220, 45)
    SetChrPos(0x18, 9480, 250, 32070, 180)
    SetChrPos(0x9, 9490, 250, 31050, 0)
    SetChrPos(0x19, 8250, 130, 44870, 46)
    SetChrPos(0xA, 7080, 0, 41450, 14)
    SetChrPos(0xB, 17790, 0, 47220, 260)
    SetChrPos(0x1A, -18980, 0, 51590, 180)
    SetChrPos(0xC, -19080, 0, 48030, 0)
    SetChrPos(0x1B, -9790, 210, 47380, 56)
    SetChrPos(0xD, -19320, 0, 41420, 44)
    SetChrPos(0xE, -17850, 20, 41630, 80)
    FadeToBright(2000, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(278000, 0)
    OP_6E(288, 0)
    Fade(1000)
    OP_6D(9140, 250, 31570, 0)

    def lambda_92B():
        OP_6C(314000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_92B)
    SetChrFlags(0x9, 0x20)
    OP_51(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_94B():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_94B)

    def lambda_965():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_965)
    Sleep(1000)

    def lambda_984():
        OP_99(0x9, 0x2, 0x7, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_984)
    Sleep(100)
    OP_96(0x18, 0x2512, 0xFA, 0x80DE, 0x3E8, 0x1F40)
    OP_8E(0x18, 0x24FE, 0xFA, 0x7CC4, 0x1B58, 0x0)
    OP_96(0x9, 0x24F4, 0xFA, 0x74EA, 0x3E8, 0x1F40)

    def lambda_9DB():
        OP_99(0x9, 0x0, 0x2, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9DB)
    OP_8E(0x9, 0x24FE, 0xFA, 0x799A, 0x1B58, 0x0)

    def lambda_9FF():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_9FF)

    def lambda_A19():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A19)
    Sleep(500)
    Fade(1000)
    OP_6D(7760, 0, 43410, 0)
    OP_6E(330, 0)

    def lambda_A57():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_A57)

    def lambda_A67():
        OP_6D(11360, 0, 49140, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_A67)

    def lambda_A7F():

        label("loc_A7F")

        TurnDirection(0xFE, 0x19, 0)
        OP_48()
        Jump("loc_A7F")

    QueueWorkItem2(0xA, 2, lambda_A7F)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrChipByIndex(0xA, 11)
    SetChrChipByIndex(0xB, 11)

    def lambda_AA9():
        OP_8E(0xFE, 0x3BE2, 0xFA, 0xB8BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_AA9)

    def lambda_AC4():
        OP_8E(0xFE, 0x22BA, 0xE6, 0xB50E, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_AC4)

    def lambda_ADF():
        OP_8E(0xFE, 0x2724, 0xFA, 0xB8F6, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_ADF)
    WaitChrThread(0x19, 0x1)

    def lambda_AFF():
        OP_8E(0xFE, 0x2C60, 0x0, 0xC116, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_AFF)
    WaitChrThread(0x19, 0x1)
    TurnDirection(0x19, 0xA, 800)
    Sleep(200)

    def lambda_B2B():
        OP_92(0xFE, 0x19, 0x3E8, 0x190, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B2B)

    def lambda_B40():
        OP_92(0xFE, 0x19, 0x3E8, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_B40)
    Sleep(300)
    TurnDirection(0x19, 0xB, 800)
    SetChrFlags(0xB, 0x20)
    OP_51(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_99(0xB, 0x0, 0x2, 0x7D0)

    def lambda_B7A():
        OP_99(0xFE, 0x3, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_B7A)

    def lambda_B8A():
        OP_8E(0xFE, 0x2FD0, 0x0, 0xBD6A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B8A)
    Sleep(100)

    def lambda_BAA():
        OP_8E(0xFE, 0x2832, 0x28, 0xBB3A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_BAA)
    Sleep(200)
    SetChrFlags(0x19, 0x4)

    def lambda_BCF():
        OP_97(0xFE, 0x2ED6, 0xC06C, 0x38270, 0x24B8, 0x1)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_BCF)
    Sleep(250)

    def lambda_BF0():
        OP_8F(0xFE, 0x2B0C, 0xFA, 0xB752, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BF0)
    Sleep(100)

    def lambda_C10():
        OP_96(0xFE, 0x23F0, 0x0, 0xBA86, 0x258, 0x1B58)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C10)
    ClearChrFlags(0x19, 0x4)

    def lambda_C33():
        OP_8E(0xFE, 0x5000, 0x0, 0xB464, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_C33)
    Sleep(500)

    def lambda_C53():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C53)
    Sleep(500)

    def lambda_C6D():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_C6D)
    Sleep(100)
    ClearChrFlags(0xB, 0x20)
    OP_8E(0xB, 0x2B7A, 0x0, 0xBC7A, 0x1388, 0x0)

    def lambda_CA0():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_CA0)

    def lambda_CB5():
        OP_92(0xFE, 0x19, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_CB5)
    Sleep(500)
    Fade(1000)
    OP_6D(-19190, 0, 50360, 0)
    SetChrChipByIndex(0xC, 11)

    def lambda_CEA():
        OP_6D(-19700, 0, 53190, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CEA)
    OP_92(0xC, 0x1A, 0x258, 0x1770, 0x0)

    def lambda_D10():
        OP_91(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D10)
    OP_91(0x1A, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)

    def lambda_D3F():
        OP_9E(0xFE, 0x1E, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_D3F)

    def lambda_D59():
        OP_9E(0xFE, 0x1E, 0x0, 0x2BC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_D59)
    Sleep(700)

    def lambda_D78():

        label("loc_D78")

        TurnDirection(0xFE, 0xC, 0)
        OP_48()
        Jump("loc_D78")

    QueueWorkItem2(0x1A, 1, lambda_D78)

    def lambda_D89():
        OP_8F(0xFE, 0xFFFFB3C0, 0x0, 0xD192, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_D89)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x40)
    OP_91(0xC, 0x0, 0x0, 0x190, 0x1388, 0x0)
    OP_97(0xC, 0xFFFFB3C0, 0xD192, 0xFFFE7960, 0x2328, 0x2)
    OP_96(0xC, 0xFFFFAE3E, 0xFFFFF060, 0xDCD2, 0xC8, 0x2710)
    OP_44(0x1A, 0xFF)
    SetChrChipByIndex(0xD, 11)

    def lambda_DF7():
        OP_8E(0xFE, 0xFFFFB348, 0x0, 0xBE46, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_DF7)
    Sleep(500)

    def lambda_E17():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_E17)

    def lambda_E25():
        OP_6D(-19190, 0, 50360, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E25)

    def lambda_E3D():
        OP_6E(305, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E3D)
    SetChrChipByIndex(0xE, 11)

    def lambda_E52():
        OP_8E(0xFE, 0xFFFFB8FC, 0x0, 0xBDF6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E52)
    Sleep(1500)

    def lambda_E72():

        label("loc_E72")

        TurnDirection(0xFE, 0xE, 0)
        OP_48()
        Jump("loc_E72")

    QueueWorkItem2(0x1A, 1, lambda_E72)

    def lambda_E83():
        OP_91(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E83)
    Sleep(200)

    def lambda_EA3():
        OP_91(0xFE, 0x0, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_EA3)
    Sleep(300)

    def lambda_EC3():
        OP_8E(0xFE, 0xFFFFBB9A, 0x0, 0xBE3C, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_EC3)
    Sleep(500)

    def lambda_EE3():
        TurnDirection(0xFE, 0x1B, 800)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_EE3)

    def lambda_EF1():
        TurnDirection(0xFE, 0x1B, 800)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_EF1)
    Sleep(400)
    OP_96(0xE, 0xFFFFB64A, 0x0, 0xB928, 0x3E8, 0x1770)
    Sleep(100)

    def lambda_F20():
        OP_8F(0xFE, 0xFFFFB384, 0x0, 0xB6E4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_F20)

    def lambda_F3B():
        OP_8F(0xFE, 0xFFFFB0E6, 0x0, 0xC1D4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_F3B)
    SetChrFlags(0x1A, 0x4)
    OP_8F(0x1A, 0xFFFFB7A8, 0x0, 0xC8F0, 0xFA0, 0x0)
    OP_96(0x1A, 0xFFFFBFE6, 0x0, 0xBFE0, 0x3E8, 0x1B58)
    OP_8F(0x1A, 0xFFFFBD02, 0x0, 0xBA40, 0x7D0, 0x0)
    Fade(1000)
    OP_6D(110, 0, 26870, 0)
    OP_6C(326000, 0)

    ChrTalk(    #4
        0x108,
        (
            "#070FAll right...\x01",
            "Looks like they went for it.\x02\x03",

            "Now's our chance to sneak in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#000FOkay!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#010FRoger that.\x02",
    )

    CloseMessageWindow()

    def lambda_1032():
        OP_6D(-60, 1000, 57500, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1032)

    def lambda_104A():
        OP_67(0, 5710, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_104A)

    def lambda_1062():
        OP_6B(1780, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1062)

    def lambda_1072():
        OP_6C(44000, 6000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1072)

    def lambda_1082():
        OP_6E(545, 3000)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1082)

    def lambda_1092():
        OP_8E(0xFE, 0xFFFFFFA6, 0x3E8, 0xE06A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_1092)
    Sleep(300)

    def lambda_10B2():
        OP_8E(0xFE, 0xFFFFFDBC, 0x3E8, 0xDB60, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_10B2)
    Sleep(100)

    def lambda_10D2():
        OP_8E(0xFE, 0x320, 0x3E8, 0xDA2A, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_10D2)
    WaitChrThread(0x108, 0x1)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_43(0x108, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0x4)
    Sleep(400)
    OP_43(0x102, 0x1, 0x0, 0x4)
    OP_28(0x4C, 0x1, 0x1)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4310   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_79C end

    def Function_4_1128(): pass

    label("Function_4_1128")

    OP_8E(0xFE, 0xFFFFFFA6, 0x3E8, 0xE06A, 0x1194, 0x0)

    def lambda_1142():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_1142)
    OP_8E(0xFE, 0xFFFFFFCE, 0x3E8, 0xE948, 0x1194, 0x0)
    Return()

    # Function_4_1128 end

    def Function_5_1163(): pass

    label("Function_5_1163")

    EventBegin(0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, -1440, 1000, 57280, 180)
    SetChrPos(0x19, 1590, 1000, 57280, 180)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x18, 2)
    SetChrSubChip(0x19, 2)
    OP_6D(-110, 1000, 51060, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(538, 0)

    def lambda_11E8():
        OP_6D(80, 1000, 58940, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11E8)

    def lambda_1200():
        OP_6C(0, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1200)

    def lambda_1210():
        OP_6E(346, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1210)

    def lambda_1220():
        OP_67(0, 6150, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1220)
    Sleep(9000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4313   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1163 end

    def Function_6_1244(): pass

    label("Function_6_1244")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, -1440, 1000, 57280, 180)
    SetChrPos(0x19, 1590, 1000, 57280, 180)
    SetChrChipByIndex(0x18, 18)
    SetChrChipByIndex(0x19, 18)
    SetChrSubChip(0x18, 2)
    SetChrSubChip(0x19, 2)
    OP_6D(750, 0, 24130, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(480, 0)

    def lambda_12D8():
        OP_6C(333000, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_12D8)
    Sleep(1000)

    def lambda_12ED():
        OP_6D(-440, 0, 54170, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12ED)

    def lambda_1305():
        OP_67(0, 4770, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1305)

    def lambda_131D():
        OP_6E(480, 9000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_131D)
    Sleep(9000)
    SetMapFlags(0x2000000)
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4312   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1244 end

    def Function_7_133E(): pass

    label("Function_7_133E")

    ClearMapFlags(0x10000000)
    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(260, 1000, 50040, 0)
    OP_67(0, 6530, -10000, 0)
    OP_6B(1570, 0)
    OP_6C(44000, 0)
    OP_6E(510, 0)
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x101, 130, 1000, 50320, 180)
    SetChrPos(0x102, 170, 750, 49180, 337)
    SetChrPos(0x101, 130, 1000, 50320, 180)
    SetChrPos(0x1C, 1300, 1000, 50640, 233)
    SetChrPos(0x1D, -1050, 1000, 51180, 189)
    SetChrPos(0x1F, -2540, 1000, 50100, 137)
    SetChrPos(0x1E, -1560, 500, 48490, 27)
    SetChrPos(0x108, 1400, 250, 47380, 6)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #7
        0x101,
        (
            "#505F#6PJoshua, please be careful...\x02\x03",

            "Don't go taking any unnecessary risks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#010FI'll be fine.\x02\x03",

            "And you try to be on\x01",
            "your best behavior.\x02\x03",

            "Don't overestimate your own\x01",
            "strength, and make sure you\x01",
            "watch Schera's back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        (
            "#006FI understand.\x02\x03",

            "Whatever happens,\x01",
            "remember our promise!\x02\x03",

            "#001FWe see each other again, safe\x01",
            "and sound, in Grancel Castle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        "#019FCount on it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x1C,
        (
            "#040FJoshua...\x02\x03",

            "There's no telling what kinds of\x01",
            "creatures inhabit the sewers.\x02\x03",

            "Please, take the utmost care.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #12
        0x102,
        "#010FI know. And I will.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #13
        0x1D,
        (
            "#021FAnd don't worry about Estelle.\x02\x03",

            "You've grown so much during\x01",
            "this trip of yours.\x02\x03",

            "#027FNot just in your skills and bracer\x01",
            "qualifications, but in your hearts...\x01",
            "or so it seems to me.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x101, 0x1D, 400)

    ChrTalk(    #14
        0x101,
        "#4P#503FSch-Schera...\x02",
    )

    CloseMessageWindow()

    def lambda_1769():

        label("loc_1769")

        TurnDirection(0xFE, 0x102, 0)
        OP_48()
        Jump("loc_1769")

    QueueWorkItem2(0x1F, 1, lambda_1769)

    ChrTalk(    #15
        0x102,
        (
            "#014F???\x02\x03",

            "What does that mean?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #16
        0x101,
        "#008FI-It's nothing! Save it for later!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x1F,
        (
            "#141FHeh... Even in times of crisis,\x01",
            "you can always count on these\x01",
            "two brats.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x108,
        (
            "#071FHa ha... Quite so.\x02\x03",

            "#070FNow...I think we'll be heading out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x1E,
        "#031FMay we meet again, my lovelies.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#010FAidios be with you!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x108, 180, 400)

    def lambda_18BB():
        OP_6D(260, 1000, 49040, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18BB)

    def lambda_18D3():
        OP_8E(0xFE, 0x8C, 0x0, 0x5618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_18D3)
    OP_8C(0x1E, 180, 400)

    def lambda_18F5():
        OP_8E(0xFE, 0x8C, 0x0, 0x5618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_18F5)
    OP_8C(0x102, 180, 400)

    def lambda_1917():
        OP_8E(0xFE, 0x8C, 0x0, 0x5618, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1917)
    Sleep(500)
    OP_8E(0x101, 0xAA, 0x2EE, 0xC01C, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #21
        0x101,
        "#000F#6PJoshua...\x02",
    )

    CloseMessageWindow()
    OP_62(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_63(0x1D)
    OP_8F(0x1D, 0x2BC, 0x3E8, 0xC792, 0x7D0, 0x0)

    ChrTalk(    #22
        0x1D,
        (
            "#027F(Hey, Princess...)\x02\x03",

            "(Do you ever wonder if those\x01",
            "two have some kind of destiny\x01",
            "in store for them...?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x1C,
        (
            "#045F#6P(Ha ha... Yes, the thought\x01",
            "has crossed my mind.)\x02\x03",

            "(They always have a smile\x01",
            "for each other...)\x02\x03",

            "#542F(...I have to admit, I'm even\x01",
            "the tiniest bit envious.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x65A)
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4100   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_133E end

    def Function_8_1ACA(): pass

    label("Function_8_1ACA")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #24
        "\x07\x05It's locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_1ACA end

    SaveToFile()

Try(main)
