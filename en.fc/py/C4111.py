from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4111   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4111.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60089",
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
        'Sister Ellen',                         # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Monster',                              # 14
        'Monster',                              # 15
        'Monster',                              # 16
        'Monster',                              # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Carna',                                # 20
        'Anelace',                              # 21
        'Grant',                                # 22
        'Kurt',                                 # 23
        '1st Lieutenant Schwarz',               # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Royal Guardsman',                      # 32
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
        'ED6_DT07/CH01410 ._CH',             # 00
        'ED6_DT09/CH10820 ._CH',             # 01
        'ED6_DT09/CH10821 ._CH',             # 02
        'ED6_DT07/CH00100 ._CH',             # 03
        'ED6_DT07/CH00101 ._CH',             # 04
        'ED6_DT07/CH00110 ._CH',             # 05
        'ED6_DT07/CH00111 ._CH',             # 06
        'ED6_DT07/CH00170 ._CH',             # 07
        'ED6_DT07/CH00172 ._CH',             # 08
        'ED6_DT07/CH01330 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
        'ED6_DT07/CH00112 ._CH',             # 0B
        'ED6_DT07/CH01240 ._CH',             # 0C
        'ED6_DT07/CH01630 ._CH',             # 0D
        'ED6_DT07/CH01260 ._CH',             # 0E
        'ED6_DT07/CH01620 ._CH',             # 0F
        'ED6_DT07/CH02090 ._CH',             # 10
        'ED6_DT07/CH01320 ._CH',             # 11
        'ED6_DT06/CH20116 ._CH',             # 12
        'ED6_DT06/CH20117 ._CH',             # 13
    )

    AddCharChipPat(
        'ED6_DT07/CH01410P._CP',             # 00
        'ED6_DT09/CH10820P._CP',             # 01
        'ED6_DT09/CH10821P._CP',             # 02
        'ED6_DT07/CH00100P._CP',             # 03
        'ED6_DT07/CH00101P._CP',             # 04
        'ED6_DT07/CH00110P._CP',             # 05
        'ED6_DT07/CH00111P._CP',             # 06
        'ED6_DT07/CH00170P._CP',             # 07
        'ED6_DT07/CH00172P._CP',             # 08
        'ED6_DT07/CH01330P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
        'ED6_DT07/CH00112P._CP',             # 0B
        'ED6_DT07/CH01240P._CP',             # 0C
        'ED6_DT07/CH01630P._CP',             # 0D
        'ED6_DT07/CH01260P._CP',             # 0E
        'ED6_DT07/CH01620P._CP',             # 0F
        'ED6_DT07/CH02090P._CP',             # 10
        'ED6_DT07/CH01320P._CP',             # 11
        'ED6_DT06/CH20116P._CP',             # 12
        'ED6_DT06/CH20117P._CP',             # 13
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

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 32110,
        Y                   = -1000,
        Z                   = -45500,
        Range               = 35850,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFF84AE,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )

    DeclEvent(
        X                   = -88800,
        Y                   = -1000,
        Z                   = -3040,
        Range               = -85900,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFB7EE,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 70260,
        Y                   = -1000,
        Z                   = 32570,
        Range               = 56300,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x7602,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    DeclActor(
        TriggerX            = -18470,
        TriggerZ            = 0,
        TriggerY            = -5070,
        TriggerRange        = 1500,
        ActorX              = -18470,
        ActorZ              = 1700,
        ActorY              = -5070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4CE",          # 00, 0
        "Function_1_4F4",          # 01, 1
        "Function_2_507",          # 02, 2
        "Function_3_266B",         # 03, 3
        "Function_4_30F0",         # 04, 4
        "Function_5_3405",         # 05, 5
        "Function_6_3580",         # 06, 6
        "Function_7_36FC",         # 07, 7
    )


    def Function_0_4CE(): pass

    label("Function_0_4CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_4E5")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_4E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_4F3")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_4F3")

    Return()

    # Function_0_4CE end

    def Function_1_4F4(): pass

    label("Function_1_4F4")

    OP_16(0x2, 0xFA0, 0xFFFDDD20, 0xFFFDDD20, 0x30064)
    Return()

    # Function_1_4F4 end

    def Function_2_507(): pass

    label("Function_2_507")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266A")
    EventBegin(0x0)
    SetChrPos(0x8, 14740, 0, -49400, 225)
    SetChrPos(0x9, 12040, 0, -49370, 90)
    SetChrPos(0xA, 12070, 0, -51990, 45)
    SetChrPos(0xB, 14800, 0, -52250, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    OP_A2(0x616)

    ChrTalk(    #0
        0x8,
        "Noooo!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #1
        0x101,
        "#000FYou heard that, right?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#010FIt came from over there!\x01",
            "Let's go!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(13190, 0, -50600, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 20850, 0, -44670, 0)
    SetChrPos(0x102, 19400, 0, -43210, 0)

    ChrTalk(    #3
        0x8,
        "AIIIEEEEEEE!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Help meeee!\x01",
            "Someone, please help me!!\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 2)

    def lambda_6BD():
        OP_92(0xFE, 0x8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6BD)
    Sleep(50)
    SetChrChipByIndex(0xA, 2)

    def lambda_6DC():
        OP_92(0xFE, 0x8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_6DC)
    Sleep(100)
    SetChrChipByIndex(0xB, 2)

    def lambda_6FB():
        OP_92(0xFE, 0x8, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_6FB)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)

    def lambda_71A():
        OP_8E(0xFE, 0x3B7E, 0x0, 0xFFFF3B8E, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_71A)

    def lambda_735():
        OP_8E(0xFE, 0x35DE, 0x0, 0xFFFF414C, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_735)
    Sleep(600)
    SetChrChipByIndex(0x101, 10)
    SetChrChipByIndex(0x102, 11)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x102, 0x1000)

    def lambda_769():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_769)

    def lambda_779():
        OP_99(0xFE, 0x0, 0xB, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_779)
    WaitChrThread(0x102, 0x1)
    SetChrChipByIndex(0x9, 1)

    def lambda_793():
        OP_95(0xFE, 0xFFFFF830, 0x0, 0x0, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_793)
    SetChrChipByIndex(0xB, 1)

    def lambda_7B6():
        OP_95(0xFE, 0x0, 0x0, 0xFFFFF830, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_7B6)
    TurnDirection(0x101, 0xB, 0)
    TurnDirection(0x102, 0x9, 0)

    def lambda_7E2():
        OP_8F(0xFE, 0x38AE, 0x0, 0xFFFF3B16, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7E2)

    def lambda_7FD():
        OP_8F(0xFE, 0x35D4, 0x0, 0xFFFF3DF0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7FD)
    Sleep(150)
    SetChrChipByIndex(0xA, 1)

    def lambda_822():
        OP_95(0xFE, 0xFFFFFD44, 0x0, 0xFFFFFD44, 0x3E8, 0x1770)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_822)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #5
        0x8,
        "Eh...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#000FSister! It'll be all right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FStay back!\x01",
            "It's too dangerous!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A0():
        OP_92(0xFE, 0x8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8A0)

    def lambda_8B5():
        OP_92(0xFE, 0x8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_8B5)

    def lambda_8CA():
        OP_92(0xFE, 0x8, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_8CA)
    Sleep(500)
    Battle(0x3A3, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_8F7"),
        (SWITCH_DEFAULT, "loc_8FA"),
    )


    label("loc_8F7")

    OP_B4(0x0)
    Return()

    label("loc_8FA")

    AddParty(0x7, 0xFF)
    SetChrPos(0x108, 22520, 0, -37100, 0)
    SetChrFlags(0x108, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrPos(0x101, 14390, 0, -50980, 225)
    SetChrPos(0x102, 12920, 0, -49800, 225)
    SetChrPos(0x8, 14740, 0, -49400, 225)
    OP_6D(13730, 0, -50080, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(282000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    EventBegin(0x0)

    ChrTalk(    #8
        0x101,
        (
            "#000FWhew...\x01",
            "That was pretty tough.\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #9
        0x101,
        "#000FAre you okay, Sister?\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x102, 65535)

    def lambda_9FE():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FE)

    ChrTalk(    #10
        0x8,
        "Y-Yes... Thank you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "Umm... Who are you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FWe're with the Bracer Guild.\x02\x03",

            "We heard you scream while\x01",
            "we were looking for someone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        "I... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#000FAre you okay?\x01",
            "You don't look okay...\x02\x03",

            "Did you get hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "No...\x01",
            "Thanks to you, I'm fine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "I'm Sister Ellen. I perform my\x01",
            "duties at Grancel Cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "Thank you so much for your help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#000FHa ha...\x01",
            "You don't need to thank us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        (
            "#010FI must ask, though, what is a\x01",
            "clergywoman doing so far from\x01",
            "Grancel without escort?\x02\x03",

            "Did no one accompany you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "No... Shameful though it is to\x01",
            "admit it, I did come alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "Actually, we ran out of\x01",
            "medicinal herbs for mixing\x01",
            "at the cathedral...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "The shop was also out of stock,\x01",
            "so I came here to pick some.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#000FThat was seriously risky. There\x01",
            "are monsters everywhere.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "It was not always so... There\x01",
            "used to be none to speak of.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x8,
        (
            "It seems their numbers have\x01",
            "greatly increased in recent days.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    SetChrChipByIndex(0x101, 3)
    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x101, 0x1000)
    ClearChrFlags(0x102, 0x1000)
    Sleep(500)

    def lambda_E13():
        OP_8E(0xFE, 0x3CD2, 0x0, 0xFFFF3EB8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E13)
    Sleep(100)

    def lambda_E33():
        OP_8E(0xFE, 0x37C8, 0x0, 0xFFFF4282, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_E33)
    OP_8C(0x8, 45, 400)

    ChrTalk(    #27
        0x8,
        "Ah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_E77():
        OP_8F(0xFE, 0x3782, 0x0, 0xFFFF3C24, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_E77)
    SetChrPos(0x9, 19840, 0, -40400, 0)
    SetChrPos(0xA, 21100, 0, -41220, 0)
    SetChrPos(0xB, 21440, 0, -39410, 0)
    SetChrPos(0xC, 21420, 0, -38390, 0)
    SetChrPos(0xD, 23130, 0, -39910, 0)
    SetChrPos(0xE, 21460, 0, -36780, 0)
    SetChrPos(0xF, 23510, 0, -37150, 0)
    SetChrPos(0x10, 24560, 0, -39000, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)

    def lambda_F42():
        OP_8E(0xFE, 0x3BB0, 0x0, 0xFFFF4E44, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F42)

    def lambda_F5D():
        OP_8E(0xFE, 0x43DA, 0x0, 0xFFFF4BA6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F5D)

    def lambda_F78():
        OP_8E(0xFE, 0x40E2, 0x0, 0xFFFF5060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F78)

    def lambda_F93():
        OP_8E(0xFE, 0x3FAC, 0x0, 0xFFFF56B4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_F93)

    def lambda_FAE():
        OP_8E(0xFE, 0x4A1A, 0x0, 0xFFFF5132, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FAE)

    def lambda_FC9():
        OP_8E(0xFE, 0x433A, 0x0, 0xFFFF5A74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FC9)

    def lambda_FE4():
        OP_8E(0xFE, 0x4AF6, 0x0, 0xFFFF5ACE, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_FE4)

    def lambda_FFF():
        OP_8E(0xFE, 0x4A74, 0x0, 0xFFFF55F6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_FFF)
    Sleep(300)

    def lambda_101F():
        OP_6D(19250, 0, -43570, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_101F)

    def lambda_1037():
        OP_6C(0, 4500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1037)
    Sleep(1500)

    def lambda_104C():
        OP_6D(17110, 0, -45970, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104C)
    Sleep(3000)

    ChrTalk(    #28
        0x101,
        (
            "#000FWh-What the heck are\x01",
            "these things...?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x102,
        (
            "#010FThey must have been attracted\x01",
            "by the noise...\x02\x03",

            "Dealing with this many\x01",
            "might be a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#000FYeah, we need to at least\x01",
            "get the sister to safety.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x108, 0x80)
    OP_8E(0x108, 0x528A, 0x0, 0xFFFF61B8, 0x2EE0, 0x0)

    def lambda_1155():
        OP_6D(17970, 0, -45090, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1155)
    SetChrChipByIndex(0x108, 8)
    SetChrFlags(0x108, 0x20)
    SetChrFlags(0x108, 0x1000)

    def lambda_117C():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_117C)
    OP_8E(0x108, 0x4CD6, 0x0, 0xFFFF5C36, 0x2EE0, 0x0)
    PlayEffect(0x8, 0xFF, 0xFF, 19660, 0, -41900, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)

    def lambda_11D5():
        OP_8F(0xFE, 0x43DA, 0x0, 0xFFFF542A, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_11D5)

    def lambda_11F0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11F0)

    def lambda_1202():
        OP_99(0xFE, 0x4, 0x7, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_1202)
    OP_96(0x108, 0x4F9C, 0x0, 0xFFFF5EDE, 0x3E8, 0x1770)

    ChrTalk(    #31
        0x108,
        "Yo! Need a hand?\x02",
    )

    CloseMessageWindow()

    def lambda_123F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_123F)

    def lambda_124D():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_124D)

    def lambda_125B():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_125B)

    def lambda_1269():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1269)

    def lambda_1277():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1277)

    ChrTalk(    #32
        0x101,
        "#000FZin?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        "#010FThank Aidios you're here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x108,
        (
            "#070FHeh heh... I was wondering who\x01",
            "it was, and here it turns out\x01",
            "to be you guys!\x02\x03",

            "But why don't we save the\x01",
            "chit-chat until we've dealt\x01",
            "with the guests?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#000FRight!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#010FRoger that!\x02",
    )

    CloseMessageWindow()

    def lambda_137F():
        OP_99(0xFE, 0x0, 0x4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_137F)

    def lambda_138F():
        OP_8E(0xFE, 0x416E, 0x0, 0xFFFF4868, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_138F)

    def lambda_13AA():
        OP_8E(0xFE, 0x3A0C, 0x0, 0xFFFF494E, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_13AA)
    OP_8E(0x108, 0x492A, 0x0, 0xFFFF5952, 0x1388, 0x0)
    Battle(0x3A4, 0x0, 0x0, 0x0, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_13EC"),
        (SWITCH_DEFAULT, "loc_13EF"),
    )


    label("loc_13EC")

    OP_B4(0x0)
    Return()

    label("loc_13EF")

    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    EventBegin(0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrPos(0x101, 16770, 0, -47500, 45)
    SetChrPos(0x102, 15050, 0, -45990, 45)
    SetChrPos(0x108, 17690, 0, -44440, 225)
    SetChrPos(0x8, 14650, 0, -48360, 45)
    OP_6D(15920, 0, -45970, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    ClearChrFlags(0x108, 0x1000)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x108, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 65535)
    SetChrChipByIndex(0x102, 65535)
    SetChrChipByIndex(0x108, 65535)
    ClearChrFlags(0x108, 0x20)
    ClearChrFlags(0x108, 0x1000)

    ChrTalk(    #37
        0x108,
        (
            "#070FMan, oh, man... Worked up\x01",
            "quite a sweat on that one!\x02\x03",

            "But honestly, I wasn't expecting\x01",
            "to see you guys here.\x02\x03",

            "Didn't you have business\x01",
            "in Zeiss?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        "#000FOh, we handled that ages ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x102,
        (
            "#010FActually, we transferred from\x01",
            "the Zeiss branch to Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x108,
        (
            "#070FAhh, I see.\x02\x03",

            "Which would mean that you managed\x01",
            "to solve that kidnapping case.\x01",
            "Well done!\x02\x03",

            "How's the redhead who got\x01",
            "poisoned?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#000FOh, he's fine now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x8,
        "Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x108,
        (
            "#070FOh, pardon my rudeness...\x02\x03",

            "...Whoa.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16F2():

        label("loc_16F2")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_16F2")

    QueueWorkItem2(0x108, 1, lambda_16F2)
    OP_8F(0x108, 0x3D72, 0x0, 0xFFFF4DAE, 0x7D0, 0x0)

    ChrTalk(    #44
        0x108,
        (
            "#070F(Hey... Who's the pretty lady?)\x02\x03",

            "(She with you? ...She single?)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x108, 400)

    ChrTalk(    #45
        0x102,
        (
            "#010F(Uh, what? I-I don't know.\x01",
            "We only just met her...)\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #46
        0x101,
        (
            "#000FYour MOUTHS are open, guys...\x02\x03",

            "Do you want me to tell\x01",
            "Kilika about this?\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x108, 0xFF)
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #47
        0x108,
        (
            "#070FI'm...uh...just making an objective\x01",
            "observation...\x02\x03",

            "#072F...And what does Kilika have to do with\x01",
            "this, anyway?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3B92, 0x0, 0xFFFF4674, 0x7D0, 0x0)

    ChrTalk(    #48
        0x8,
        (
            "Umm... I truly appreciate you \x01",
            "all coming to my assistance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x8,
        "You've saved my life.\x02",
    )

    CloseMessageWindow()

    def lambda_18F4():

        label("loc_18F4")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_18F4")

    QueueWorkItem2(0x108, 1, lambda_18F4)

    def lambda_1905():

        label("loc_1905")

        TurnDirection(0xFE, 0x108, 0)
        OP_48()
        Jump("loc_1905")

    QueueWorkItem2(0x102, 1, lambda_1905)
    OP_8F(0x108, 0x3DC2, 0x0, 0xFFFF491C, 0x7D0, 0x0)

    ChrTalk(    #50
        0x108,
        (
            "#070FNo, no!\x01",
            "Please, think nothing of it!\x02\x03",

            "Just doing what comes naturally\x01",
            "for a chivalrous man!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x8,
        "Oh, my...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#000F(Oh, PLEASE...)\x02\x03",

            "(He's a total sucker for \x01",
            "a pretty face, isn't he?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#010F(Ha ha... So it appears.)\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 22440, 0, -38100, 0)
    SetChrPos(0x12, 21240, 0, -37930, 0)

    ChrTalk(    #54
        0x11,
        (
            "You there!\x01",
            "What are you doing?!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1A63():

        label("loc_1A63")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A63")

    QueueWorkItem2(0x108, 2, lambda_1A63)

    def lambda_1A74():

        label("loc_1A74")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A74")

    QueueWorkItem2(0x101, 2, lambda_1A74)

    def lambda_1A85():

        label("loc_1A85")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A85")

    QueueWorkItem2(0x102, 2, lambda_1A85)

    def lambda_1A96():

        label("loc_1A96")

        TurnDirection(0xFE, 0x11, 0)
        OP_48()
        Jump("loc_1A96")

    QueueWorkItem2(0x8, 2, lambda_1A96)

    def lambda_1AA7():
        OP_8E(0xFE, 0x48DA, 0x0, 0xFFFF540C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1AA7)

    def lambda_1AC2():
        OP_8E(0xFE, 0x4434, 0x0, 0xFFFF55EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1AC2)
    OP_6D(17010, 0, -44670, 3000)

    ChrTalk(    #55
        0x101,
        "#000FWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        "#010F...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #57
        0x11,
        (
            "You're four people in an otherwise-deserted area,\x01",
            "discussing what appears to be a confidential topic.\x01",
            "HIGHLY suspicious behavior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x12,
        "I think you're terrorists.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x4182, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    ChrTalk(    #59 op#A op#5
        0x101,
        (
            "#10A#000FWha... Who are you calling a\x01",
            "terrorist?! If anyone's acting\x01",
            "suspicious here...\x05\x02",
        )
    )

    Sleep(1000)
    OP_8E(0x102, 0x3F2A, 0x0, 0xFFFF4BF6, 0xFA0, 0x0)

    def lambda_1C45():
        OP_8E(0xFE, 0x42FE, 0x0, 0xFFFF49D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C45)
    OP_8F(0x102, 0x4182, 0x0, 0xFFFF4BF6, 0x7D0, 0x0)

    ChrTalk(    #60
        0x102,
        (
            "#010FWe're with the Bracer Guild,\x01",
            "Grancel branch.\x02\x03",

            "We came to the aid of the\x01",
            "sister here, who was under\x01",
            "attack by some monsters.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x11,
        "What...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x12,
        "Bracers?!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x8, 0x3A84, 0x0, 0xFFFF4B60, 0x7D0, 0x0)

    ChrTalk(    #63
        0x8,
        (
            "Umm... This gentleman speaks\x01",
            "the truth.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        (
            "I came here to gather herbs,\x01",
            "when those creatures attacked me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x108,
        (
            "#070FAnd on a related note,\x01",
            "I'm also a bracer.\x02\x03",

            "I'll be facing your buddies\x01",
            "in the ring later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x11,
        (
            "Calvardian martial arts... Ah, you're\x01",
            "that guy in the Martial Arts\x01",
            "Competition that fights solo, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x12,
        (
            "Hmph... You've definitely got\x01",
            "the muscles of a prize fighter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "I'll leave you be,\x01",
            "just this once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        (
            "But the Erbe Royal Villa is close\x01",
            "by. Wanderers and sightseers\x01",
            "are NOT welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x12,
        "Also, Sister...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x12,
        (
            "I think we should escort you\x01",
            "back to Grancel NOW.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x12,
        (
            "You've already been enough trouble\x01",
            "as it is, from what I can see.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "Oh...but I...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #74
        0x101,
        (
            "#000FOh, for the love of...\x02\x03",

            "You've been nothing but\x01",
            "obnoxious from the moment\x01",
            "you started talki--\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #75
        0x102,
        "#010FEstelle. Shush.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x11, 400)

    ChrTalk(    #76
        0x102,
        (
            "#010FWe'll take care to avoid the Royal\x01",
            "Villa, sirs. You have our apologies\x01",
            "for any inconvenience we've caused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x11,
        "Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x11,
        (
            "In the future, however, I would advise\x01",
            "you to know your place. Mouthing off\x01",
            "to the wrong people can be...hazardous.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x12,
        "Come on, Sister. Let's go.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x8,
        "A-All right...\x02",
    )

    CloseMessageWindow()
    OP_44(0x8, 0xFF)
    OP_8E(0x8, 0x4268, 0x0, 0xFFFF515A, 0xBB8, 0x0)
    TurnDirection(0x8, 0x108, 400)

    ChrTalk(    #81
        0x8,
        (
            "Thank you again for\x01",
            "your help...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21FB():
        OP_8E(0xFE, 0x5CB2, 0x0, 0xFFFF70F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21FB)
    Sleep(100)

    def lambda_221B():
        OP_8E(0xFE, 0x5CB2, 0x0, 0xFFFF70F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_221B)
    Sleep(200)

    def lambda_223B():
        OP_8E(0xFE, 0x5CB2, 0x0, 0xFFFF70F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_223B)
    Sleep(2000)
    OP_62(0x101, 0x0, 1900, 0x2C, 0x2F, 0x96, 0x1)
    OP_22(0x2F, 0x0, 0x64)
    OP_6D(17150, 0, -46640, 1000)
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x108, 0xFF)
    OP_44(0x102, 0xFF)

    ChrTalk(    #82
        0x101,
        (
            "#000FWha... Who... How...\x02\x03",

            "Who the HELL do they\x01",
            "think they are?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x108,
        (
            "#070FThey're Special Ops soldiers,\x01",
            "affiliated with the Royal Army's\x01",
            "Intelligence Division.\x02\x03",

            "Skillful, to be sure, but\x01",
            "their strongest suit is\x01",
            "their sneakiness.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_237F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_237F)
    TurnDirection(0x101, 0x108, 400)

    ChrTalk(    #84
        0x101,
        (
            "#000FTheir ONLY suit,\x01",
            "if you ask me!\x02\x03",

            "Err...\x02\x03",

            "Wait a second. How do\x01",
            "you know them, Zin?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #85
        0x108,
        (
            "#070FI ran into their team at the\x01",
            "Martial Arts Competition.\x02\x03",

            "I was introduced to them then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#000F(They're actually fighting...?!)\x02\x03",

            "(What would some spy types be doing\x01",
            "participating in something as public\x01",
            "as a tournament?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#010F(I guess they didn't feel it necessary\x01",
            "to conceal their identities...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x108,
        (
            "#070FWell, we should get back to\x01",
            "the city before they decide\x01",
            "that they'd rather fight.\x02\x03",

            "...Oh, right. What brings\x01",
            "you two here, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x101,
        (
            "#000FOh, yeah. Duh.\x02\x03",

            "Actually, we were looking for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x108,
        "#070FWhy's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#010FWe had a favor we needed to ask.\x02\x03",

            "About that Martial Arts Competition...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/T4130   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_266A")

    Return()

    # Function_2_507 end

    def Function_3_266B(): pass

    label("Function_3_266B")

    EventBegin(0x0)
    SetChrPos(0x101, 11690, 0, -52560, 225)
    SetChrPos(0x102, 11000, 0, -51680, 225)
    SetChrPos(0x108, 10930, 0, -50240, 196)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x13, 14410, 0, -53900, 257)
    SetChrPos(0x14, 14820, 0, -52280, 244)
    SetChrPos(0x15, 13050, 0, -51640, 207)
    SetChrPos(0x16, 13090, 0, -50260, 213)
    OP_6D(11570, 250, -53400, 0)
    OP_67(0, 7270, -10000, 0)
    OP_6B(2710, 0)
    OP_6C(225000, 0)
    OP_6E(395, 0)
    FadeToBright(3000, 0)

    def lambda_2744():
        OP_6C(249000, 5000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2744)
    OP_6E(309, 5000)

    ChrTalk(    #92
        0x101,
        (
            "#006FSo...are we going to\x01",
            "meet back here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010FWell, this is the Amberl Monument rest area,\x01",
            "so this should be the place.\x02\x03",

            "#013FThe only real issue is whether\x01",
            "or not Lt. Schwarz and her men\x01",
            "can get here undetected.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x17, 17080, 0, -45130, 225)
    SetChrPos(0x18, 17100, 0, -43830, 225)
    SetChrPos(0x19, 18380, 0, -45010, 225)
    SetChrPos(0x1A, 17740, 0, -42700, 225)
    SetChrPos(0x1B, 18600, 0, -43670, 225)
    SetChrPos(0x1C, 19480, 0, -44620, 225)
    SetChrPos(0x1D, 18580, 0, -41840, 225)
    SetChrPos(0x1E, 19520, 0, -42690, 225)
    SetChrPos(0x1F, 20400, 0, -43690, 225)

    def lambda_2903():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2903)

    def lambda_291E():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_291E)

    def lambda_2939():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2939)

    def lambda_2954():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2954)

    def lambda_296F():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_296F)

    def lambda_298A():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_298A)

    def lambda_29A5():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_29A5)

    def lambda_29C0():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_29C0)

    def lambda_29DB():
        OP_90(0xFE, 0x7D0, 0x0, 0xFA0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_29DB)

    ChrTalk(    #94
        0x17,
        "#1PNo need to worry about that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2A4E():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A4E)

    def lambda_2A5C():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A5C)

    def lambda_2A6A():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2A6A)

    def lambda_2A78():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2A78)

    def lambda_2A86():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2A86)

    def lambda_2A94():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2A94)

    def lambda_2AA2():
        TurnDirection(0xFE, 0x17, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2AA2)

    def lambda_2AB0():
        OP_6C(335000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_2AB0)

    def lambda_2AC0():
        OP_6E(332, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2AC0)

    def lambda_2AD0():
        OP_6D(13880, 0, -49890, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2AD0)

    def lambda_2AE8():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_2AE8)
    Sleep(100)

    def lambda_2B08():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_2B08)

    def lambda_2B23():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2B23)
    Sleep(100)

    def lambda_2B43():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_2B43)

    def lambda_2B5E():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_2B5E)

    def lambda_2B79():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_2B79)
    Sleep(100)

    def lambda_2B99():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_2B99)

    def lambda_2BB4():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_2BB4)

    def lambda_2BCF():
        OP_90(0xFE, 0xFFFFF060, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_2BCF)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x17, 0x1)

    ChrTalk(    #95
        0x101,
        (
            "#004FWhoa!\x01",
            "When did you get here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x108,
        (
            "#071FHa ha... Nice work staying\x01",
            "hidden in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x17,
        (
            "#176FWe have quite a few sympathizers\x01",
            "among the citizens.\x02\x03",

            "#170FWe've finished our preparations.\x01",
            "We can begin whenever you're ready.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x16,
        "#843FAll right...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x101, 400)

    ChrTalk(    #99
        0x16,
        (
            "#840F#4PWe're waiting on your\x01",
            "order, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2D2E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D2E)

    def lambda_2D3C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2D3C)

    def lambda_2D4A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2D4A)

    def lambda_2D58():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2D58)

    def lambda_2D66():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_2D66)

    def lambda_2D74():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_2D74)

    ChrTalk(    #100
        0x101,
        (
            "#580FHuh...?\x02\x03",

            "MY order?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x16,
        (
            "#840F#4PYou were the ones who originally\x01",
            "received Her Majesty's request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x15,
        (
            "#820F#4PSo, we're waiting on your\x01",
            "command before we begin.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x101,
        "#506FB-But...I... I'm just a rookie...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x13,
        (
            "#831F#2PHa ha... That really doesn't\x01",
            "matter. I don't think you'll\x01",
            "have a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x14,
        "#811F#2PJust do it without shouting, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x17,
        (
            "#171FWe'll be there to help.\x01",
            "We have no objections.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x101,
        "#503FI...uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x102,
        "#010F#6PHave a little faith in yourself.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x108,
        (
            "#071F#6PDon't worry about the trivial details.\x02\x03",

            "Just deal with things as\x01",
            "they come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#008FRight...\x02\x03",

            "#006F...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 225, 400)

    def lambda_2FD9():

        label("loc_2FD9")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FD9")

    QueueWorkItem2(0x102, 1, lambda_2FD9)

    def lambda_2FEA():

        label("loc_2FEA")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FEA")

    QueueWorkItem2(0x108, 1, lambda_2FEA)

    def lambda_2FFB():

        label("loc_2FFB")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_2FFB")

    QueueWorkItem2(0x13, 1, lambda_2FFB)

    def lambda_300C():

        label("loc_300C")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_300C")

    QueueWorkItem2(0x14, 1, lambda_300C)

    def lambda_301D():

        label("loc_301D")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_301D")

    QueueWorkItem2(0x15, 1, lambda_301D)

    def lambda_302E():

        label("loc_302E")

        TurnDirection(0xFE, 0x101, 0)
        OP_48()
        Jump("loc_302E")

    QueueWorkItem2(0x16, 1, lambda_302E)

    def lambda_303F():
        OP_6C(0, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_303F)
    OP_8E(0x101, 0x2972, 0x1E0, 0xFFFF2F40, 0x5DC, 0x0)
    OP_20(0x7D0)
    OP_8C(0x101, 45, 400)
    WaitChrThread(0x101, 0x3)
    OP_21()

    ChrTalk(    #111
        0x101,
        "#006F#5POkay, then, here goes...\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #112
        0x101,
        (
            "#005F#5PEveryone...let's get those\x01",
            "hostages rescued!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    SetMapFlags(0x2000000)
    OP_A2(0x3FA)
    NewScene("ED6_DT01/C4113   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_266B end

    def Function_4_30F0(): pass

    label("Function_4_30F0")

    EventBegin(0x0)
    OP_6D(-26280, 0, -4400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(234, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x18, 19)
    SetChrChipByIndex(0x19, 19)
    SetChrChipByIndex(0x1A, 19)
    SetChrChipByIndex(0x1B, 19)
    SetChrSubChip(0x18, 2)
    SetChrSubChip(0x19, 2)
    SetChrSubChip(0x1A, 2)
    SetChrSubChip(0x1B, 2)
    SetChrPos(0x18, -25890, 0, -4510, 180)
    SetChrPos(0x19, -27370, 0, -4510, 180)
    SetChrPos(0x1A, -27240, 0, -2700, 180)
    SetChrPos(0x1B, -25950, 0, -2920, 180)
    SetChrPos(0x108, -26570, 0, -6220, 0)
    SetChrPos(0x102, -28030, 0, -6250, 45)
    SetChrPos(0x101, -25360, 0, -6190, 315)
    Sleep(1000)

    ChrTalk(    #113
        0x108,
        "#4P#072FThe ambush party's on the move.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x18,
        (
            "#3PWe'll go ahead and lure \x01",
            "the remaining forces into\x01",
            "the front gardens!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x18,
        (
            "#3PYou can break into the villa\x01",
            "while they're distracted!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x101,
        "#006FSounds good!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        "#2P#012FAidios be with all of you!\x02",
    )

    CloseMessageWindow()

    def lambda_32E6():

        label("loc_32E6")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_32E6")

    QueueWorkItem2(0x101, 1, lambda_32E6)

    def lambda_32F7():

        label("loc_32F7")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_32F7")

    QueueWorkItem2(0x102, 1, lambda_32F7)

    def lambda_3308():

        label("loc_3308")

        TurnDirection(0xFE, 0x18, 0)
        OP_48()
        Jump("loc_3308")

    QueueWorkItem2(0x108, 1, lambda_3308)
    SetChrChipByIndex(0x1B, 18)

    def lambda_331E():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_331E)

    def lambda_332C():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_332C)
    Sleep(200)
    SetChrChipByIndex(0x1A, 18)

    def lambda_3351():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_3351)

    def lambda_335F():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_335F)
    Sleep(200)
    SetChrChipByIndex(0x18, 18)

    def lambda_3384():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3384)

    def lambda_3392():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3392)
    Sleep(200)
    SetChrChipByIndex(0x19, 18)

    def lambda_33B7():
        OP_8C(0xFE, 0, 800)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_33B7)

    def lambda_33C5():
        OP_8E(0xFE, 0xFFFF9B60, 0x0, 0x76B6, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_33C5)
    Sleep(2000)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x108, 0xFF)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    OP_A2(0x651)
    EventEnd(0x0)
    Return()

    # Function_4_30F0 end

    def Function_5_3405(): pass

    label("Function_5_3405")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_357F")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_347D")

    ChrTalk(    #118
        0x101,
        (
            "#002FWe can't miss our chance\x01",
            "to get in.\x02\x03",

            "We have to get to the Erbe\x01",
            "Royal Villa NOW!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3564")

    label("loc_347D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34EF")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #119
        0x102,
        (
            "#012FWe're not going to get\x01",
            "another chance at this.\x02\x03",

            "Let's go to the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3564")

    label("loc_34EF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3564")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(    #120
        0x108,
        (
            "#072FWe've only got one chance\x01",
            "to do this.\x02\x03",

            "...Come on. Let's hurry to\x01",
            "the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3564")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_357F")

    Return()

    # Function_5_3405 end

    def Function_6_3580(): pass

    label("Function_6_3580")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36FB")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F8")

    ChrTalk(    #121
        0x101,
        (
            "#002FWe can't miss our chance\x01",
            "to get in.\x02\x03",

            "We have to get to the Erbe\x01",
            "Royal Villa NOW!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_35F8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_366B")
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #122
        0x102,
        (
            "#012FWe're not going to get\x01",
            "another chance for this.\x02\x03",

            "Let's go to the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36E0")

    label("loc_366B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E0")
    TurnDirection(0x108, 0x1, 400)

    ChrTalk(    #123
        0x108,
        (
            "#072FWe've only got one chance\x01",
            "to do this.\x02\x03",

            "...Come on. Let's hurry to\x01",
            "the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36E0")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_36FB")

    Return()

    # Function_6_3580 end

    def Function_7_36FC(): pass

    label("Function_7_36FC")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #124
        (
            "\x07\x05North:   Erbe Royal Villa\x01",
            "West:    Sanktheim Gate          224 selge\x01",
            "East:    Gurune Gate             256 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_7_36FC end

    SaveToFile()

Try(main)
