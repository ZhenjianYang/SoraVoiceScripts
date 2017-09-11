from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4113   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4113.x',
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
        'Special Ops Soldier',                  # 9
        'Special Ops Soldier',                  # 10
        'Carna',                                # 11
        'Anelace',                              # 12
        'Grant',                                # 13
        'Kurt',                                 # 14
        '1st Lieutenant Schwarz',               # 15
        'Royal Guardsman',                      # 16
        'Royal Guardsman',                      # 17
        'Royal Guardsman',                      # 18
        'Royal Guardsman',                      # 19
        'Royal Guardsman',                      # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Chief Warrant Officer',                # 24
        'Special Ops Soldier',                  # 25
        'Special Ops Soldier',                  # 26
        'Special Ops Soldier',                  # 27
        'Special Ops Soldier',                  # 28
        'Special Ops Soldier',                  # 29
        'Special Ops Soldier',                  # 30
        'Special Ops Soldier',                  # 31
        'Special Ops Soldier',                  # 32
        'Special Ops Soldier',                  # 33
        'Special Ops Soldier',                  # 34
        'Military K-9',                         # 35
        'Military K-9',                         # 36
        'Military K-9',                         # 37
        'Military K-9',                         # 38
        'Military K-9',                         # 39
        'Mechanic Payton',                      # 40
        ' ',                                    # 41
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
        'ED6_DT07/CH01610 ._CH',             # 00
        'ED6_DT07/CH00400 ._CH',             # 01
        'ED6_DT07/CH00420 ._CH',             # 02
        'ED6_DT07/CH00390 ._CH',             # 03
        'ED6_DT07/CH00410 ._CH',             # 04
        'ED6_DT07/CH02090 ._CH',             # 05
        'ED6_DT07/CH01320 ._CH',             # 06
        'ED6_DT07/CH01610 ._CH',             # 07
        'ED6_DT07/CH00340 ._CH',             # 08
        'ED6_DT07/CH00341 ._CH',             # 09
        'ED6_DT09/CH10060 ._CH',             # 0A
        'ED6_DT09/CH10061 ._CH',             # 0B
        'ED6_DT06/CH20042 ._CH',             # 0C
        'ED6_DT07/CH01450 ._CH',             # 0D
        'ED6_DT06/CH20114 ._CH',             # 0E
        'ED6_DT06/CH20115 ._CH',             # 0F
        'ED6_DT06/CH20116 ._CH',             # 10
        'ED6_DT06/CH20117 ._CH',             # 11
        'ED6_DT07/CH00344 ._CH',             # 12
        'ED6_DT07/CH00440 ._CH',             # 13
        'ED6_DT07/CH00441 ._CH',             # 14
        'ED6_DT07/CH01790 ._CH',             # 15
        'ED6_DT07/CH00502 ._CH',             # 16
        'ED6_DT07/CH00510 ._CH',             # 17
        'ED6_DT07/CH00511 ._CH',             # 18
        'ED6_DT07/CH00442 ._CH',             # 19
    )

    AddCharChipPat(
        'ED6_DT07/CH01610P._CP',             # 00
        'ED6_DT07/CH00400P._CP',             # 01
        'ED6_DT07/CH00420P._CP',             # 02
        'ED6_DT07/CH00390P._CP',             # 03
        'ED6_DT07/CH00410P._CP',             # 04
        'ED6_DT07/CH02090P._CP',             # 05
        'ED6_DT07/CH01320P._CP',             # 06
        'ED6_DT07/CH01610P._CP',             # 07
        'ED6_DT07/CH00340P._CP',             # 08
        'ED6_DT07/CH00341P._CP',             # 09
        'ED6_DT09/CH10060P._CP',             # 0A
        'ED6_DT09/CH10061P._CP',             # 0B
        'ED6_DT06/CH20042P._CP',             # 0C
        'ED6_DT07/CH01450P._CP',             # 0D
        'ED6_DT06/CH20114P._CP',             # 0E
        'ED6_DT06/CH20115P._CP',             # 0F
        'ED6_DT06/CH20116P._CP',             # 10
        'ED6_DT06/CH20117P._CP',             # 11
        'ED6_DT07/CH00344P._CP',             # 12
        'ED6_DT07/CH00440P._CP',             # 13
        'ED6_DT07/CH00441P._CP',             # 14
        'ED6_DT07/CH01790P._CP',             # 15
        'ED6_DT07/CH00502P._CP',             # 16
        'ED6_DT07/CH00510P._CP',             # 17
        'ED6_DT07/CH00511P._CP',             # 18
        'ED6_DT07/CH00442P._CP',             # 19
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 131087,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 131089,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 21,
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


    DeclEvent(
        X                   = 14350,
        Y                   = -1000,
        Z                   = -8640,
        Range               = 11930,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0x19F0,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 44270,
        Y                   = 1000,
        Z                   = 940,
        Range               = 48410,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0xFFFFFF10,
        Unknown_18          = 0x0,
        Unknown_1C          = 21,
    )

    DeclEvent(
        X                   = 45450,
        Y                   = 1000,
        Z                   = 6140,
        Range               = 47430,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x1144,
        Unknown_18          = 0x0,
        Unknown_1C          = 22,
    )


    ScpFunction(
        "Function_0_5FA",          # 00, 0
        "Function_1_62E",          # 01, 1
        "Function_2_646",          # 02, 2
        "Function_3_B08",          # 03, 3
        "Function_4_174F",         # 04, 4
        "Function_5_1782",         # 05, 5
        "Function_6_17C8",         # 06, 6
        "Function_7_180E",         # 07, 7
        "Function_8_1854",         # 08, 8
        "Function_9_1886",         # 09, 9
        "Function_10_18B8",        # 0A, 10
        "Function_11_18EB",        # 0B, 11
        "Function_12_191E",        # 0C, 12
        "Function_13_1951",        # 0D, 13
        "Function_14_1970",        # 0E, 14
        "Function_15_19A3",        # 0F, 15
        "Function_16_19D6",        # 10, 16
        "Function_17_1A09",        # 11, 17
        "Function_18_1A3C",        # 12, 18
        "Function_19_1A6F",        # 13, 19
        "Function_20_1AA2",        # 14, 20
        "Function_21_2297",        # 15, 21
        "Function_22_23FD",        # 16, 22
        "Function_23_26CF",        # 17, 23
    )


    def Function_0_5FA(): pass

    label("Function_0_5FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_611")
    OP_A3(0x3FA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_611")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_61F")
    OP_A3(0x3FB)
    Event(0, 3)

    label("loc_61F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_62D")
    OP_A3(0x3FC)
    Event(0, 20)

    label("loc_62D")

    Return()

    # Function_0_5FA end

    def Function_1_62E(): pass

    label("Function_1_62E")

    OP_16(0x2, 0xFA0, 0xFFFEA070, 0xFFFE4698, 0x30066)
    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_62E end

    def Function_2_646(): pass

    label("Function_2_646")

    ClearMapFlags(0x2000000)
    EventBegin(0x0)
    OP_6D(45860, 0, 7990, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(69000, 0)
    OP_6E(325, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 26320, 0, 2029, 270)
    SetChrPos(0x9, 26350, 0, -100, 270)
    FadeToBright(2000, 0)

    def lambda_6C5():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_6C5)
    Sleep(2000)

    def lambda_6DA():
        OP_6E(228, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DA)
    OP_6D(26290, 0, 960, 5000)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)

    ChrTalk(    #0
        0x8,
        (
            "#6P*sigh*...\x01",
            "I am so freakin' hungry...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #1
        0x8,
        "#3PIsn't it time to change shifts yet?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #2
        0x9,
        "Come on, stay focused.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "There's no telling when the Royal Guardsmen\x01",
            "might finally show themselves.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "#3PThere weren't more than\x01",
            "ten escapees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#3PIf the colonel really put his mind to it, we\x01",
            "could hunt the lot of them down in no time.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, 16180, 0, 1410, 90)
    SetChrPos(0xF, 15420, 0, 630, 90)
    SetChrPos(0x10, 15520, 0, 2230, 90)
    SetChrPos(0x11, 14270, 0, 550, 90)
    SetChrPos(0x12, 14270, 0, 2230, 90)
    SetChrSubChip(0xE, 1)
    SetChrSubChip(0xF, 2)
    SetChrSubChip(0x10, 2)
    SetChrSubChip(0x11, 2)
    SetChrSubChip(0x12, 2)
    OP_20(0x5DC)

    ChrTalk(    #6
        0xE,
        (
            "#2PIf you think it's so easy,\x01",
            "then go ahead and try.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_960():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_960)

    def lambda_96E():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_96E)

    def lambda_97C():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_97C)

    def lambda_98C():
        OP_6D(20430, 0, 1370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_98C)

    def lambda_9A4():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9A4)
    Sleep(500)
    OP_1D(0x59)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1000)
    OP_62(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    ChrTalk(    #7
        0x8,
        "#2PWha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "#2PLieutenant Schwarz!\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 25)
    SetChrChipByIndex(0x9, 25)
    SetChrSubChip(0x8, 0)
    SetChrSubChip(0x9, 0)
    SetChrFlags(0xE, 0x1000)
    SetChrFlags(0xF, 0x1000)
    SetChrFlags(0x10, 0x1000)
    SetChrFlags(0x11, 0x1000)
    SetChrFlags(0x12, 0x1000)
    SetChrChipByIndex(0xE, 14)

    def lambda_A4C():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A4C)

    def lambda_A62():
        OP_6D(24930, 0, 1380, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A62)
    Sleep(200)
    SetChrChipByIndex(0xF, 16)
    SetChrChipByIndex(0x10, 16)
    SetChrChipByIndex(0x11, 16)
    SetChrChipByIndex(0x12, 16)

    def lambda_A93():
        OP_92(0xFE, 0x9, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_A93)
    Sleep(50)

    def lambda_AAD():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_AAD)
    Sleep(50)

    def lambda_AC7():
        OP_92(0xFE, 0x9, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_AC7)
    Sleep(50)

    def lambda_AE1():
        OP_92(0xFE, 0x8, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_AE1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_646 end

    def Function_3_B08(): pass

    label("Function_3_B08")

    EventBegin(0x0)
    OP_6D(30000, 0, 630, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(233000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x108, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0xE, 28310, 0, 210, 90)
    SetChrPos(0xF, 29950, 0, -1020, 47)
    SetChrPos(0x10, 29140, 0, 2290, 127)
    SetChrPos(0x11, 31010, 0, 1560, 131)
    SetChrPos(0x12, 31530, 0, -1200, 11)
    SetChrChipByIndex(0x8, 12)
    SetChrChipByIndex(0x9, 12)
    SetChrFlags(0x8, 0x800)
    SetChrFlags(0x9, 0x800)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x8, 33200, 0, 2800, 26)
    SetChrPos(0x9, 32790, 0, 420, 142)
    SetChrFlags(0x17, 0x40)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    SetChrFlags(0x21, 0x40)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x17, 11630, 0, -2640, 90)
    SetChrPos(0x18, 9800, 0, -3930, 90)
    SetChrPos(0x19, 9800, 0, -3930, 90)
    SetChrPos(0x1A, 9800, 0, -3930, 90)
    SetChrPos(0x1B, 9800, 0, -3930, 90)
    SetChrPos(0x1C, 9800, 0, -3930, 90)
    SetChrPos(0x1D, 9890, 0, -2180, 90)
    SetChrPos(0x1E, 9890, 0, -2180, 90)
    SetChrPos(0x1F, 9890, 0, -2180, 90)
    SetChrPos(0x20, 9890, 0, -2180, 90)
    SetChrPos(0x21, 9890, 0, -2180, 90)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x22, 0x40)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x25, 0x40)
    SetChrFlags(0x26, 0x40)
    SetChrPos(0x22, 12030, 0, -4240, 90)
    SetChrPos(0x23, 13140, 0, -2490, 72)
    SetChrPos(0x24, 11810, 0, -930, 90)
    SetChrPos(0x25, 8510, 0, -4850, 90)
    SetChrPos(0x26, 8510, 0, -1080, 90)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #9
        0xE,
        (
            "#176F#4PThat settles that...\x02\x03",

            "#173FHmph.\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xE, 1)
    SetChrSubChip(0xF, 1)
    SetChrSubChip(0x10, 1)
    SetChrSubChip(0x11, 1)
    SetChrSubChip(0x12, 1)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0x10, 0x20)
    SetChrFlags(0x11, 0x20)
    SetChrFlags(0x12, 0x20)

    def lambda_E24():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_E24)

    def lambda_E32():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_E32)

    def lambda_E40():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_E40)

    def lambda_E4E():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_E4E)

    def lambda_E5C():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E5C)
    Sleep(100)

    def lambda_E6F():
        OP_6D(19050, 0, 1190, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E6F)

    def lambda_E87():
        OP_6C(315000, 2300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E87)
    Sleep(400)
    OP_43(0x22, 0x1, 0x0, 0x5)
    OP_43(0x23, 0x1, 0x0, 0x6)
    OP_43(0x24, 0x1, 0x0, 0x7)
    OP_43(0x17, 0x1, 0x0, 0x4)
    OP_43(0x18, 0x1, 0x0, 0xA)
    OP_43(0x1D, 0x1, 0x0, 0xF)
    Sleep(600)

    def lambda_ECB():
        OP_6D(25500, 0, 390, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ECB)

    def lambda_EE3():
        OP_67(0, 6710, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_EE3)
    OP_43(0x19, 0x1, 0x0, 0xB)
    OP_43(0x1E, 0x1, 0x0, 0x10)
    Sleep(400)
    OP_43(0x1A, 0x1, 0x0, 0xC)
    OP_43(0x1F, 0x1, 0x0, 0x11)
    Sleep(400)
    OP_43(0x1B, 0x1, 0x0, 0xD)
    OP_43(0x20, 0x1, 0x0, 0x12)
    Sleep(400)
    OP_43(0x1C, 0x1, 0x0, 0xE)
    OP_43(0x21, 0x1, 0x0, 0x13)
    Sleep(400)
    OP_43(0x25, 0x1, 0x0, 0x8)
    OP_43(0x26, 0x1, 0x0, 0x9)
    Sleep(2500)

    ChrTalk(    #10
        0x17,
        "Idiots...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x17,
        (
            "The airship's locked down.\x01",
            "You'll never be able to use it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xE,
        "#178F#2P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x17,
        (
            "If you'd just done as the colonel said,\x01",
            "we would've spared your lives...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x17,
        (
            "But now you're going to die, and you've only\x01",
            "got your own stubbornness to blame!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x17,
        "Take this!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xA, 12560, 0, -2110, 70)
    SetChrPos(0xD, 13660, 0, -70, 90)
    SetChrPos(0xC, 13730, 0, -1250, 75)
    SetChrPos(0xB, 12340, 0, 1110, 95)

    def lambda_10B2():
        OP_6D(28050, 0, 980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_10B2)
    LoadEffect(0x2, "map\\\\mp019_00.eff")
    LoadEffect(0x0, "craft\\\\cr201_02.eff")
    SetChrPos(0x28, 19080, 0, 510, 0)
    PlayEffect(0x2, 0xFF, 0xC, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x28, 0, 0, 0, 0)
    Sleep(200)
    SetChrChipByIndex(0x22, 11)
    SetChrChipByIndex(0x23, 11)
    SetChrChipByIndex(0x24, 11)

    def lambda_114E():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_114E)

    def lambda_1169():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1169)

    def lambda_1184():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1184)
    Sleep(100)
    SetChrChipByIndex(0x18, 20)
    SetChrChipByIndex(0x1C, 9)

    def lambda_11AE():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_11AE)

    def lambda_11C9():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_11C9)
    Sleep(100)
    SetChrChipByIndex(0x19, 9)
    SetChrChipByIndex(0x1D, 9)

    def lambda_11F3():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_11F3)

    def lambda_120E():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_120E)
    OP_22(0x1FA, 0x0, 0x64)
    Sleep(100)
    Sleep(200)
    OP_44(0x1B, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)
    Sleep(100)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    SetChrChipByIndex(0x17, 23)
    SetChrChipByIndex(0x18, 19)
    SetChrChipByIndex(0x19, 8)
    SetChrChipByIndex(0x1A, 19)
    SetChrChipByIndex(0x1C, 19)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 19)
    SetChrChipByIndex(0x1F, 8)
    SetChrChipByIndex(0x20, 19)
    SetChrChipByIndex(0x21, 8)
    SetChrChipByIndex(0x22, 10)
    SetChrChipByIndex(0x23, 10)
    SetChrChipByIndex(0x24, 10)
    SetChrChipByIndex(0x25, 10)
    SetChrChipByIndex(0x26, 10)

    def lambda_12C8():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_12C8)

    def lambda_12D6():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_12D6)

    def lambda_12E4():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_12E4)

    def lambda_12F2():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_12F2)

    def lambda_1300():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1300)

    def lambda_130E():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_130E)

    def lambda_131C():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_131C)

    def lambda_132A():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_132A)

    def lambda_1338():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1338)

    def lambda_1346():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1346)

    def lambda_1354():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1354)

    def lambda_1362():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1362)

    def lambda_1370():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1370)

    def lambda_137E():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_137E)

    def lambda_138C():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_138C)

    def lambda_139A():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_139A)

    def lambda_13A8():

        label("loc_13A8")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13A8")

    QueueWorkItem2(0x22, 0, lambda_13A8)

    def lambda_13BB():

        label("loc_13BB")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13BB")

    QueueWorkItem2(0x23, 0, lambda_13BB)

    def lambda_13CE():

        label("loc_13CE")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13CE")

    QueueWorkItem2(0x24, 0, lambda_13CE)

    def lambda_13E1():
        OP_67(0, 4650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_13E1)

    def lambda_13F9():
        OP_6C(291000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13F9)

    def lambda_1409():
        OP_6D(16070, 0, 1210, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1409)
    Sleep(350)
    PlayEffect(0x0, 0xFF, 0x1B, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x1F, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0x20, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_44(0x1B, 0xFF)
    OP_44(0x1F, 0xFF)
    OP_44(0x20, 0xFF)

    def lambda_14D1():
        OP_8F(0x1B, 0x4BB4, 0x0, 0xFFFFF880, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_14D1)

    def lambda_14EC():
        OP_8F(0x1F, 0x50D2, 0x0, 0x46A, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_14EC)

    def lambda_1507():
        OP_8F(0x20, 0x4934, 0x0, 0xA28, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_1507)
    TurnDirection(0x1B, 0x28, 0)
    TurnDirection(0x1F, 0x28, 0)
    TurnDirection(0x20, 0x28, 0)
    SetChrChipByIndex(0x1B, 18)
    SetChrChipByIndex(0x1F, 18)
    SetChrChipByIndex(0x20, 18)
    SetChrFlags(0x1B, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)

    def lambda_1555():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1555)

    def lambda_1565():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1565)

    def lambda_1575():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1575)
    Sleep(30)

    def lambda_158A():
        OP_8F(0x1B, 0x4BB4, 0x0, 0xFFFFF880, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_158A)

    def lambda_15A5():
        OP_8F(0x1F, 0x50D2, 0x0, 0x46A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_15A5)

    def lambda_15C0():
        OP_8F(0x20, 0x4934, 0x0, 0xA28, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_15C0)
    Sleep(30)

    def lambda_15E0():
        OP_8F(0x1B, 0x4BB4, 0x0, 0xFFFFF880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_15E0)

    def lambda_15FB():
        OP_8F(0x1F, 0x50D2, 0x0, 0x46A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_15FB)

    def lambda_1616():
        OP_8F(0x20, 0x4934, 0x0, 0xA28, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_1616)
    Sleep(30)
    OP_44(0x1B, 0x2)
    OP_44(0x1F, 0x2)
    OP_44(0x20, 0x2)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #16
        0x17,
        "#2PB-Bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x17,
        (
            "#2PYou can't be serious...\x01",
            "You're not actually going to try\x01",
            "standing against the Royal Army!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        (
            "#843F#6PSorry to disappoint you...\x01",
            "but you've already been\x01",
            "marked as criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        (
            "#832FBy order of the queen,\x01",
            "you will let us pass!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4111   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_B08 end

    def Function_4_174F(): pass

    label("Function_4_174F")

    SetChrChipByIndex(0xFE, 24)
    OP_8E(0xFE, 0x44E8, 0x0, 0xFFFFFE98, 0x1770, 0x0)
    OP_8E(0xFE, 0x5438, 0x0, 0x0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 23)
    Return()

    # Function_4_174F end

    def Function_5_1782(): pass

    label("Function_5_1782")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x47FE, 0xA, 0xFFFFF718, 0x1770, 0x0)
    OP_8E(0xFE, 0x5794, 0x0, 0xFFFFF754, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_17BA():

        label("loc_17BA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_17BA")

    QueueWorkItem2(0xFE, 0, lambda_17BA)
    Return()

    # Function_5_1782 end

    def Function_6_17C8(): pass

    label("Function_6_17C8")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4C0E, 0x0, 0xFFFFFF92, 0x1770, 0x0)
    OP_8E(0xFE, 0x5AC8, 0x0, 0xFFFFFFCE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1800():

        label("loc_1800")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1800")

    QueueWorkItem2(0xFE, 0, lambda_1800)
    Return()

    # Function_6_17C8 end

    def Function_7_180E(): pass

    label("Function_7_180E")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4574, 0x0, 0x41A, 0x1770, 0x0)
    OP_8E(0xFE, 0x5744, 0x0, 0x780, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1846():

        label("loc_1846")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1846")

    QueueWorkItem2(0xFE, 0, lambda_1846)
    Return()

    # Function_7_180E end

    def Function_8_1854(): pass

    label("Function_8_1854")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4466, 0x0, 0xFFFFF7D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1878():

        label("loc_1878")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1878")

    QueueWorkItem2(0xFE, 0, lambda_1878)
    Return()

    # Function_8_1854 end

    def Function_9_1886(): pass

    label("Function_9_1886")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x434E, 0x0, 0x938, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_18AA():

        label("loc_18AA")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_18AA")

    QueueWorkItem2(0xFE, 0, lambda_18AA)
    Return()

    # Function_9_1886 end

    def Function_10_18B8(): pass

    label("Function_10_18B8")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x55B4, 0x64, 0xFFFFF2D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_10_18B8 end

    def Function_11_18EB(): pass

    label("Function_11_18EB")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4F92, 0x14, 0xFFFFF718, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_11_18EB end

    def Function_12_191E(): pass

    label("Function_12_191E")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FEC, 0x0, 0xFFFFFD12, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_12_191E end

    def Function_13_1951(): pass

    label("Function_13_1951")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4826, 0x0, 0xFFFFFD4E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_13_1951 end

    def Function_14_1970(): pass

    label("Function_14_1970")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4B00, 0x1E, 0xFFFFF3EE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_14_1970 end

    def Function_15_19A3(): pass

    label("Function_15_19A3")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x54A6, 0x0, 0xC26, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_15_19A3 end

    def Function_16_19D6(): pass

    label("Function_16_19D6")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FBA, 0x0, 0x712, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_16_19D6 end

    def Function_17_1A09(): pass

    label("Function_17_1A09")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4CFE, 0x0, 0x21C, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_17_1A09 end

    def Function_18_1A3C(): pass

    label("Function_18_1A3C")

    SetChrChipByIndex(0xFE, 20)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x472C, 0x0, 0x5F0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 19)
    Return()

    # Function_18_1A3C end

    def Function_19_1A6F(): pass

    label("Function_19_1A6F")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4C54, 0x0, 0xDF2, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_19_1A6F end

    def Function_20_1AA2(): pass

    label("Function_20_1AA2")

    EventBegin(0x0)
    OP_6D(46220, -50, 11920, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x7, 0xFF)
    AddParty(0x0, 0xFF)
    AddParty(0x2, 0xFF)
    AddParty(0x4, 0xFF)
    OP_B5(0x2, 0x0)
    OP_B5(0x2, 0x1)
    OP_B5(0x2, 0x2)
    OP_B5(0x2, 0x3)
    OP_B5(0x2, 0x4)
    OP_B5(0x2, 0x5)
    OP_41(0x2, 0x40)
    OP_41(0x2, 0xF5)
    OP_41(0x2, 0x113)
    OP_41(0x2, 0x26E, 0x0)
    OP_41(0x2, 0x26B, 0x1)
    OP_41(0x2, 0x25F, 0x2)
    OP_41(0x2, 0x262, 0x3)
    OP_41(0x2, 0x268, 0x4)
    OP_41(0x2, 0x271, 0x5)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_36(0x2, 0xF0)
    OP_B5(0x4, 0x0)
    OP_B5(0x4, 0x5)
    OP_B5(0x4, 0x4)
    OP_B5(0x4, 0x3)
    OP_B5(0x4, 0x2)
    OP_B5(0x4, 0x1)
    OP_41(0x4, 0x7C)
    OP_41(0x4, 0xF5)
    OP_41(0x4, 0x113)
    OP_41(0x4, 0x259, 0x0)
    OP_41(0x4, 0x261, 0x5)
    OP_41(0x4, 0x2C8, 0x4)
    OP_41(0x4, 0x264, 0x3)
    OP_41(0x4, 0x25F, 0x2)
    OP_41(0x4, 0x27E, 0x1)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_36(0x4, 0xFA)
    SetChrPos(0x101, 46320, -10, -1800, 0)
    SetChrPos(0x103, 47360, 0, -2280, 0)
    SetChrPos(0x105, 45230, 0, -2280, 0)

    def lambda_1BC8():
        OP_6D(46300, -40, -1440, 7000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BC8)

    def lambda_1BE0():
        OP_6E(262, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BE0)
    Sleep(7000)

    ChrTalk(    #20
        0x101,
        (
            "#000FWho'd have thought we'd actually end up\x01",
            "piloting the Intelligence Division's airship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x103,
        (
            "#020FCreepy looking thing, isn't it?\x02\x03",

            "I'm not sure which I like less--this or\x01",
            "the sky bandits' ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x105,
        (
            "#040FYou must admit, though, its\x01",
            "specs are impressive.\x02\x03",

            "But how did the Intelligence Division\x01",
            "manage to get their hands on a ship\x01",
            "like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#000FThere sure is a lot we don't know...\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x27, 46370, 200, 5440, 180)
    ClearChrFlags(0x27, 0x80)

    def lambda_1D9B():
        OP_8E(0xFE, 0xB522, 0xC8, 0x442, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1D9B)
    Sleep(500)

    def lambda_1DBB():
        OP_6D(46270, 200, 430, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1DBB)
    WaitChrThread(0x27, 0x1)

    ChrTalk(    #24
        0x27,
        (
            "Hello, Your Highness.\x01",
            "Sorry for the wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x105,
        (
            "#040FHello, Payton.\x01",
            "It's been some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#000FUmm...who's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x105,
        (
            "#040FPayton works on the maintenance team for the\x01",
            "Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x27,
        (
            "Though I'm just a lowly technician sent from\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x27,
        (
            "We're still conducting test flights of the\x01",
            "Arseille, so there's quite a lot of data\x01",
            "that needs to be collected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#000FOhh, okay.\x02\x03",

            "It seemed to be flying just fine when we saw\x01",
            "it in Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x27,
        "Oh, normal flight is already stable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x27,
        (
            "But the development of the new orbal engines\x01",
            "is behind schedule, so we're just using an\x01",
            "older, less powerful one for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x27,
        (
            "Since the Intelligence Division\x01",
            "took her away, all test flights\x01",
            "were halted indefinitely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x27,
        (
            "I was wondering what to do with myself when\x01",
            "Julia made contact with me in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        "#000FGot'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#020FHa ha... We appreciate whatever\x01",
            "you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x27,
        "Y-You can count on me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x27,
        (
            "I've removed the lock, so you should be\x01",
            "able to fly without any problems.\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x27, 0xADFC, 0xC8, 0x3FC, 0x7D0, 0x0)
    TurnDirection(0x27, 0x105, 400)

    def lambda_21D0():

        label("loc_21D0")

        TurnDirection(0xFE, 0x105, 0)
        OP_48()
        Jump("loc_21D0")

    QueueWorkItem2(0x27, 3, lambda_21D0)

    ChrTalk(    #39
        0x27,
        (
            "She's an extremely maneuverable girl once\x01",
            "she gets up and running, so bear that in\x01",
            "mind when you're flying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x105,
        "#040FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#000FWell, let's go ahead\x01",
            "and get started!\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_20_1AA2 end

    def Function_21_2297(): pass

    label("Function_21_2297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_22A4")
    Return()

    label("loc_22A4")

    EventBegin(0x0)

    ChrTalk(    #42
        0x27,
        "Oh, right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x27,
        (
            "I brought along my tools to\x01",
            "tune up everyone's orbments,\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x27,
        (
            "I can also make a few tools \x01",
            "and pieces of equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#000FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x103,
        "#020FThat was thoughtful of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x105,
        (
            "#040FThat should be useful.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x27,
        "I-It's really no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x27,
        (
            "If I can help out,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x65F)
    EventEnd(0x1)
    Return()

    # Function_21_2297 end

    def Function_22_23FD(): pass

    label("Function_22_23FD")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 46310, 200, 4320, 176)
    SetChrPos(0x103, 46840, 200, 3150, 0)
    SetChrPos(0x101, 45710, 200, 3160, 0)
    TurnDirection(0x27, 0x105, 0)
    OP_6D(46390, 250, 4580, 1000)

    ChrTalk(    #50
        0x105,
        (
            "#040FIt's already almost noon.\x02\x03",

            "Shall we start the launch?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Board]\x01",                  # 0
            "[Prepare Equipment]\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_24FC"),
        (1, "loc_2517"),
        (SWITCH_DEFAULT, "loc_2585"),
    )


    label("loc_24FC")


    ChrTalk(    #51
        0x105,
        "#040FI understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2585")

    label("loc_2517")


    ChrTalk(    #52
        0x105,
        "#040FI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020FIf we're going to mess\x01",
            "with our gear, we should\x01",
            "talk to the mechanic.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    label("loc_2585")

    OP_A2(0x660)
    OP_28(0x4D, 0x1, 0x20)
    TurnDirection(0x105, 0x27, 400)

    ChrTalk(    #54
        0x105,
        "#040FPayton, could you help us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x27,
        "Roger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x27,
        (
            "I'll handle the engine.\x01",
            "You can just focus on\x01",
            "flying, Your Highness!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #57
        0x101,
        "#000FIt's finally time, Schera...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #58
        0x103,
        (
            "#020FYes...\x02\x03",

            "It'll be a difficult mission,\x01",
            "but the fundamentals are as\x01",
            "important as ever.\x02\x03",

            "Speed...and steadiness.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3F0)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_22_23FD end

    def Function_23_26CF(): pass

    label("Function_23_26CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_286E")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2766")
    TurnDirection(0x105, 0x0, 400)

    ChrTalk(    #59
        0x105,
        (
            "#042FUmm...\x01",
            "It's already almost noon.\x02\x03",

            "If everyone's ready, we\x01",
            "should board the ship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #60
        0x101,
        "#002FRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2853")

    label("loc_2766")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27F8")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #61
        0x103,
        (
            "#026FThere's no time before the\x01",
            "plan is put into action.\x02\x03",

            "#027FIf the equipment is ready, then\x01",
            "we should get on-board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2853")

    label("loc_27F8")

    TurnDirection(0x105, 0x1, 400)

    ChrTalk(    #62
        0x105,
        (
            "#042FIt's already almost noon.\x02\x03",

            "If everyone's ready, we\x01",
            "should board the ship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2853")

    OP_90(0x0, 0x5DC, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_286E")

    Return()

    # Function_23_26CF end

    SaveToFile()

Try(main)
