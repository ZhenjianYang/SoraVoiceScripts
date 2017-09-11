from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'C4103   ._SN',
        MapName             = 'Grancel',
        Location            = 'C4103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        'ED6_DT07/CH00344 ._CH',             # 0C
        'ED6_DT07/CH01450 ._CH',             # 0D
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
        'ED6_DT07/CH00344P._CP',             # 0C
        'ED6_DT07/CH01450P._CP',             # 0D
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 22,
    )


    DeclEvent(
        X                   = 23240,
        Y                   = -1000,
        Z                   = 7400,
        Range               = 17390,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE0D4,
        Unknown_18          = 0x0,
        Unknown_1C          = 25,
    )

    DeclEvent(
        X                   = 44270,
        Y                   = 1000,
        Z                   = 940,
        Range               = 48410,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 23,
    )

    DeclEvent(
        X                   = 45450,
        Y                   = 1000,
        Z                   = 6140,
        Range               = 47430,
        Unknown_10          = 0xFFFFFC18,
        Unknown_14          = 0x1144,
        Unknown_18          = 0x0,
        Unknown_1C          = 24,
    )


    ScpFunction(
        "Function_0_57A",          # 00, 0
        "Function_1_5AE",          # 01, 1
        "Function_2_5DB",          # 02, 2
        "Function_3_5F1",          # 03, 3
        "Function_4_92E",          # 04, 4
        "Function_5_12A5",         # 05, 5
        "Function_6_12EB",         # 06, 6
        "Function_7_1331",         # 07, 7
        "Function_8_1377",         # 08, 8
        "Function_9_13BD",         # 09, 9
        "Function_10_13EF",        # 0A, 10
        "Function_11_1421",        # 0B, 11
        "Function_12_1454",        # 0C, 12
        "Function_13_1487",        # 0D, 13
        "Function_14_14BA",        # 0E, 14
        "Function_15_14D9",        # 0F, 15
        "Function_16_150C",        # 10, 16
        "Function_17_153F",        # 11, 17
        "Function_18_1572",        # 12, 18
        "Function_19_15A5",        # 13, 19
        "Function_20_15D8",        # 14, 20
        "Function_21_160B",        # 15, 21
        "Function_22_1EA7",        # 16, 22
        "Function_23_2002",        # 17, 23
        "Function_24_218E",        # 18, 24
        "Function_25_249A",        # 19, 25
    )


    def Function_0_57A(): pass

    label("Function_0_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_588")
    OP_A3(0x3FA)
    Event(0, 3)

    label("loc_588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 3)), scpexpr(EXPR_END)), "loc_596")
    OP_A3(0x3FB)
    Event(0, 4)

    label("loc_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 4)), scpexpr(EXPR_END)), "loc_5AD")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FC)
    Event(0, 21)

    label("loc_5AD")

    Return()

    # Function_0_57A end

    def Function_1_5AE(): pass

    label("Function_1_5AE")

    OP_16(0x2, 0xFA0, 0xFFFEA070, 0xFFFE4698, 0x30066)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_END)), "loc_5D5")
    OP_71(0x0, 0x4)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x57), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D5")

    OP_22(0x1CC, 0x1, 0x64)
    Return()

    # Function_1_5AE end

    def Function_2_5DB(): pass

    label("Function_2_5DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F0")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5DB")

    label("loc_5F0")

    Return()

    # Function_2_5DB end

    def Function_3_5F1(): pass

    label("Function_3_5F1")

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

    def lambda_66B():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_66B)
    Sleep(2000)

    def lambda_680():
        OP_6E(228, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_680)
    OP_6D(26290, 0, 960, 5000)

    ChrTalk(    #0
        0x8,
        (
            "*sigh*...\x01",
            "I am so freakin' hungry...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #1
        0x18,
        "Isn't it time to change shifts yet?\x02",
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
            "There weren't more than\x01",
            "ten escapees.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "If the colonel really put his mind to it, we\x01",
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

    ChrTalk(    #6
        0xE,
        (
            "If you think it's so easy,\x01",
            "then go ahead and try.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_89C():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_89C)

    def lambda_8AA():
        TurnDirection(0xFE, 0xE, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_8AA)

    def lambda_8B8():
        OP_6E(262, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B8)

    def lambda_8C8():
        OP_6D(20430, 0, 1370, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8C8)

    def lambda_8E0():
        OP_6C(315000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8E0)
    Sleep(1500)

    ChrTalk(    #7
        0x8,
        "Wha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x9,
        "Lieutenant Schwarz!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T4300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5F1 end

    def Function_4_92E(): pass

    label("Function_4_92E")

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

    ChrTalk(    #9
        0xE,
        (
            "#170FThat settles that...\x02\x03",

            "Hmph.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_BF2():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BF2)

    def lambda_C00():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_C00)

    def lambda_C0E():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_C0E)

    def lambda_C1C():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_C1C)

    def lambda_C2A():
        TurnDirection(0xFE, 0x17, 800)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_C2A)
    Sleep(100)

    def lambda_C3D():
        OP_6D(19050, 0, 1190, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C3D)

    def lambda_C55():
        OP_6C(315000, 2300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_C55)
    Sleep(400)
    OP_43(0x22, 0x1, 0x0, 0x6)
    OP_43(0x23, 0x1, 0x0, 0x7)
    OP_43(0x24, 0x1, 0x0, 0x8)
    OP_43(0x17, 0x1, 0x0, 0x5)
    OP_43(0x18, 0x1, 0x0, 0xB)
    OP_43(0x1D, 0x1, 0x0, 0x10)
    Sleep(600)

    def lambda_C99():
        OP_6D(25500, 0, 390, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C99)

    def lambda_CB1():
        OP_67(0, 6710, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_CB1)
    OP_43(0x19, 0x1, 0x0, 0xC)
    OP_43(0x1E, 0x1, 0x0, 0x11)
    Sleep(400)
    OP_43(0x1A, 0x1, 0x0, 0xD)
    OP_43(0x1F, 0x1, 0x0, 0x12)
    Sleep(400)
    OP_43(0x1B, 0x1, 0x0, 0xE)
    OP_43(0x20, 0x1, 0x0, 0x13)
    Sleep(400)
    OP_43(0x1C, 0x1, 0x0, 0xF)
    OP_43(0x21, 0x1, 0x0, 0x14)
    Sleep(400)
    OP_43(0x25, 0x1, 0x0, 0x9)
    OP_43(0x26, 0x1, 0x0, 0xA)
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
        "#170F...\x02",
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
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xA, 13660, 0, -70, 90)
    SetChrPos(0xB, 12560, 0, -2110, 75)
    SetChrPos(0xC, 13730, 0, -1250, 68)
    SetChrPos(0xD, 12340, 0, 1110, 97)

    def lambda_E91():
        OP_6D(28050, 0, 980, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_E91)
    SetChrChipByIndex(0x22, 11)
    SetChrChipByIndex(0x23, 11)
    SetChrChipByIndex(0x24, 11)

    def lambda_EB8():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_EB8)

    def lambda_ED3():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_ED3)

    def lambda_EEE():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_EEE)
    Sleep(100)
    SetChrChipByIndex(0x18, 9)
    SetChrChipByIndex(0x1C, 9)

    def lambda_F18():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_F18)

    def lambda_F33():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_F33)
    Sleep(100)
    SetChrChipByIndex(0x19, 9)
    SetChrChipByIndex(0x1D, 9)

    def lambda_F5D():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_F5D)

    def lambda_F78():
        OP_8E(0xFE, 0x91AA, 0x0, 0x140, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_F78)
    Sleep(100)
    PlayEffect(0x8, 0xFF, 0xFF, 21350, 3000, 30, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_44(0x1B, 0xFF)
    PlayEffect(0x8, 0xFF, 0xFF, 17730, 1000, -580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x1B, 12)
    OP_8C(0x1B, 244, 0)

    def lambda_1017():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1017)
    Sleep(100)
    OP_44(0x22, 0xFF)
    OP_44(0x23, 0xFF)
    OP_44(0x24, 0xFF)
    OP_44(0x17, 0xFF)
    OP_44(0x18, 0xFF)
    OP_44(0x19, 0xFF)
    OP_44(0x1D, 0xFF)
    OP_44(0x1E, 0xFF)
    SetChrChipByIndex(0x17, 8)
    SetChrChipByIndex(0x18, 8)
    SetChrChipByIndex(0x19, 8)
    SetChrChipByIndex(0x1A, 8)
    SetChrChipByIndex(0x1C, 8)
    SetChrChipByIndex(0x1D, 8)
    SetChrChipByIndex(0x1E, 8)
    SetChrChipByIndex(0x1F, 8)
    SetChrChipByIndex(0x20, 8)
    SetChrChipByIndex(0x21, 8)
    SetChrChipByIndex(0x22, 10)
    SetChrChipByIndex(0x23, 10)
    SetChrChipByIndex(0x24, 10)
    SetChrChipByIndex(0x25, 10)
    SetChrChipByIndex(0x26, 10)

    def lambda_1097():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_1097)

    def lambda_10A5():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_10A5)

    def lambda_10B3():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_10B3)

    def lambda_10C1():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_10C1)

    def lambda_10CF():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_10CF)

    def lambda_10DD():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_10DD)

    def lambda_10EB():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_10EB)

    def lambda_10F9():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_10F9)

    def lambda_1107():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1107)

    def lambda_1115():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1115)

    def lambda_1123():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1123)

    def lambda_1131():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_1131)

    def lambda_113F():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_113F)

    def lambda_114D():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_114D)

    def lambda_115B():
        TurnDirection(0xFE, 0xA, 800)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_115B)

    def lambda_1169():
        OP_67(0, 4650, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1169)

    def lambda_1181():
        OP_6C(291000, 1500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1181)
    OP_6D(18070, 0, 1210, 1500)

    ChrTalk(    #16
        0x17,
        "Wha...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x17,
        "B-Bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x17,
        (
            "You can't be serious...\x01",
            "You're not actually going to try\x01",
            "standing against the Royal Army!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xD,
        (
            "Sorry to disappoint you...\x01",
            "but you've already been\x01",
            "marked as criminals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xA,
        (
            "By order of the queen,\x01",
            "you will let us pass!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3FB)
    NewScene("ED6_DT01/C4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_92E end

    def Function_5_12A5(): pass

    label("Function_5_12A5")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x44E8, 0x0, 0xFFFFFE98, 0x1770, 0x0)
    OP_8E(0xFE, 0x5438, 0x0, 0x0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)

    def lambda_12DD():

        label("loc_12DD")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_12DD")

    QueueWorkItem2(0xFE, 0, lambda_12DD)
    Return()

    # Function_5_12A5 end

    def Function_6_12EB(): pass

    label("Function_6_12EB")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x47FE, 0xA, 0xFFFFF718, 0x1770, 0x0)
    OP_8E(0xFE, 0x5794, 0x0, 0xFFFFF754, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1323():

        label("loc_1323")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1323")

    QueueWorkItem2(0xFE, 0, lambda_1323)
    Return()

    # Function_6_12EB end

    def Function_7_1331(): pass

    label("Function_7_1331")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4C0E, 0x0, 0xFFFFFF92, 0x1770, 0x0)
    OP_8E(0xFE, 0x5AC8, 0x0, 0xFFFFFFCE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1369():

        label("loc_1369")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1369")

    QueueWorkItem2(0xFE, 0, lambda_1369)
    Return()

    # Function_7_1331 end

    def Function_8_1377(): pass

    label("Function_8_1377")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4574, 0x0, 0x41A, 0x1770, 0x0)
    OP_8E(0xFE, 0x5744, 0x0, 0x780, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_13AF():

        label("loc_13AF")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13AF")

    QueueWorkItem2(0xFE, 0, lambda_13AF)
    Return()

    # Function_8_1377 end

    def Function_9_13BD(): pass

    label("Function_9_13BD")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x4466, 0x0, 0xFFFFF7D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_13E1():

        label("loc_13E1")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_13E1")

    QueueWorkItem2(0xFE, 0, lambda_13E1)
    Return()

    # Function_9_13BD end

    def Function_10_13EF(): pass

    label("Function_10_13EF")

    SetChrChipByIndex(0xFE, 11)
    OP_8E(0xFE, 0x434E, 0x0, 0x938, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 10)

    def lambda_1413():

        label("loc_1413")

        OP_99(0xFE, 0x0, 0x7, 0x5DC)
        OP_48()
        Jump("loc_1413")

    QueueWorkItem2(0xFE, 0, lambda_1413)
    Return()

    # Function_10_13EF end

    def Function_11_1421(): pass

    label("Function_11_1421")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x55B4, 0x64, 0xFFFFF2D6, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_11_1421 end

    def Function_12_1454(): pass

    label("Function_12_1454")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4F92, 0x14, 0xFFFFF718, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_12_1454 end

    def Function_13_1487(): pass

    label("Function_13_1487")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FEC, 0x0, 0xFFFFFD12, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_13_1487 end

    def Function_14_14BA(): pass

    label("Function_14_14BA")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4826, 0x0, 0xFFFFFD4E, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_14_14BA end

    def Function_15_14D9(): pass

    label("Function_15_14D9")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x4128, 0x0, 0xFFFFFA38, 0x1770, 0x0)
    OP_8E(0xFE, 0x4B00, 0x1E, 0xFFFFF3EE, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_15_14D9 end

    def Function_16_150C(): pass

    label("Function_16_150C")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x54A6, 0x0, 0xC26, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_16_150C end

    def Function_17_153F(): pass

    label("Function_17_153F")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4FBA, 0x0, 0x712, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_17_153F end

    def Function_18_1572(): pass

    label("Function_18_1572")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4CFE, 0x0, 0x21C, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_18_1572 end

    def Function_19_15A5(): pass

    label("Function_19_15A5")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x472C, 0x0, 0x5F0, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_19_15A5 end

    def Function_20_15D8(): pass

    label("Function_20_15D8")

    SetChrChipByIndex(0xFE, 9)
    OP_8E(0xFE, 0x3F7A, 0x0, 0x29E, 0x1770, 0x0)
    OP_8E(0xFE, 0x4C54, 0x0, 0xDF2, 0x1770, 0x0)
    SetChrChipByIndex(0xFE, 8)
    Return()

    # Function_20_15D8 end

    def Function_21_160B(): pass

    label("Function_21_160B")

    ClearMapFlags(0x2000000)
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
    AddParty(0x4, 0xFF)
    AddParty(0x2, 0xFF)
    OP_31(0x2, 0x0, 0x22)
    OP_B5(0x2, 0x0)
    OP_B5(0x2, 0x1)
    OP_B5(0x2, 0x5)
    OP_B5(0x2, 0x4)
    OP_B5(0x2, 0x3)
    OP_B5(0x2, 0x2)
    OP_41(0x2, 0x40)
    OP_41(0x2, 0xF6)
    OP_41(0x2, 0x114)
    OP_41(0x2, 0x26F, 0x0)
    OP_41(0x2, 0x26C, 0x1)
    OP_41(0x2, 0x260, 0x5)
    OP_41(0x2, 0x269, 0x4)
    OP_41(0x2, 0x271, 0x3)
    OP_41(0x2, 0x280, 0x2)
    OP_35(0x2, 0xAA)
    OP_35(0x2, 0xAB)
    OP_35(0x2, 0xAC)
    OP_36(0x2, 0xF0)
    OP_31(0x4, 0x0, 0x20)
    OP_B5(0x4, 0x0)
    OP_B5(0x4, 0x5)
    OP_B5(0x4, 0x4)
    OP_B5(0x4, 0x3)
    OP_B5(0x4, 0x2)
    OP_B5(0x4, 0x1)
    OP_41(0x4, 0x7C)
    OP_41(0x4, 0xF6)
    OP_41(0x4, 0x114)
    OP_41(0x4, 0x25A, 0x0)
    OP_41(0x4, 0x262, 0x5)
    OP_41(0x4, 0x2C9, 0x4)
    OP_41(0x4, 0x265, 0x3)
    OP_41(0x4, 0x25D, 0x2)
    OP_41(0x4, 0x2D4, 0x1)
    OP_35(0x4, 0xBE)
    OP_35(0x4, 0xBF)
    OP_36(0x4, 0xFA)
    SetChrPos(0x101, 46320, -10, -1800, 0)
    SetChrPos(0x103, 47360, 0, -2280, 0)
    SetChrPos(0x105, 45230, 0, -2280, 0)

    def lambda_1744():
        OP_6D(46300, -40, -1440, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1744)

    def lambda_175C():
        OP_6E(262, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_175C)
    Sleep(5000)

    ChrTalk(    #21
        0x101,
        (
            "#002FWho'd have thought we'd actually end up\x01",
            "piloting the Intelligence Division's airship...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x103,
        (
            "#025FCreepy looking thing, isn't it?\x02\x03",

            "#027FI'm not sure which I like less--this or\x01",
            "the sky bandits' ship.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x105,
        (
            "#043FYou must admit, though, its\x01",
            "specs are impressive.\x02\x03",

            "But how did the Intelligence Division\x01",
            "manage to get a ship like this...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#505FYeah...\x02\x03",

            "#007FIt's a mystery. Just like how they managed\x01",
            "to get hold of the Gospel...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x27, 46370, 200, 6000, 180)
    ClearChrFlags(0x27, 0x80)
    OP_4A(0x27, 255)

    NpcTalk(    #25
        0x27,
        "Boy's Voice",
        (
            "#4PHello, Your Highness.\x01",
            "Sorry for the wait.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1980():
        OP_6D(46270, 200, 430, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1980)

    def lambda_1998():
        OP_8E(0xFE, 0xB522, 0xC8, 0x442, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_1998)
    WaitChrThread(0x27, 0x1)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #26
        0x105,
        (
            "#041FHello, Payton.\x01",
            "It's been some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        "#501FUmm...who's that?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x105,
        (
            "#040FPayton works on the maintenance team for the\x01",
            "Arseille.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x27,
        (
            "#3PThough I'm just a lowly technician sent from\x01",
            "the central factory.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x27,
        (
            "#3PWe're still conducting test flights of the\x01",
            "Arseille, so there's quite a lot of data\x01",
            "that needs to be collected.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#004FOhh, okay.\x02\x03",

            "It seemed to be flying just fine when we saw\x01",
            "it in Ruan...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x27,
        "#3POh, normal flight is already stable.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x27,
        (
            "#3PBut the development of the new orbal engines\x01",
            "is behind schedule, so we're just using an\x01",
            "older, less powerful one for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x27,
        (
            "#3PSince the Intelligence Division\x01",
            "took her away, all test flights\x01",
            "were halted indefinitely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x27,
        (
            "#3PI was wondering what to do with myself when\x01",
            "Julia made contact with me in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#000FGot'cha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x103,
        (
            "#2P#021FHa ha... We appreciate whatever\x01",
            "you can do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x27,
        "#3PY-You can count on me!\x02",
    )

    CloseMessageWindow()

    def lambda_1D34():

        label("loc_1D34")

        TurnDirection(0xFE, 0x27, 400)
        OP_48()
        Jump("loc_1D34")

    QueueWorkItem2(0x101, 1, lambda_1D34)

    def lambda_1D45():

        label("loc_1D45")

        TurnDirection(0xFE, 0x27, 400)
        OP_48()
        Jump("loc_1D45")

    QueueWorkItem2(0x105, 1, lambda_1D45)

    def lambda_1D56():

        label("loc_1D56")

        TurnDirection(0xFE, 0x27, 400)
        OP_48()
        Jump("loc_1D56")

    QueueWorkItem2(0x103, 1, lambda_1D56)
    OP_8E(0x27, 0xBB9E, 0xC8, 0x2DA, 0x7D0, 0x0)
    TurnDirection(0x27, 0x105, 400)
    OP_44(0x101, 0xFF)
    OP_44(0x105, 0xFF)
    OP_44(0x103, 0xFF)

    ChrTalk(    #39
        0x27,
        (
            "#3PI've removed the lock, so you should be\x01",
            "able to fly without any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x27,
        (
            "#3PShe's an extremely maneuverable girl once\x01",
            "she gets up and running, so bear that in\x01",
            "mind when you're flying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        "#042F#5PI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        (
            "#006FWell, let's go ahead\x01",
            "and get started!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x27, 270, 0)
    OP_4B(0x27, 255)
    EventEnd(0x0)
    Return()

    # Function_21_160B end

    def Function_22_1EA7(): pass

    label("Function_22_1EA7")

    TalkBegin(0x27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F4C")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                 # 0
            "Modify/Exchange\x01",      # 1
            "Buy\x01",                  # 2
            "Leave\x01",                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F22")
    OP_0D()
    OP_A9(0x6C)
    OP_56(0x0)
    TalkEnd(0x27)
    Return()

    label("loc_1F22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F3B")
    OP_0D()
    OP_A9(0x6D)
    OP_56(0x0)
    TalkEnd(0x27)
    Return()

    label("loc_1F3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F4C")
    TalkEnd(0x27)
    Return()

    label("loc_1F4C")


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
        0x27,
        (
            "If I can help out,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x27)
    Return()

    # Function_22_1EA7 end

    def Function_23_2002(): pass

    label("Function_23_2002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 7)), scpexpr(EXPR_END)), "loc_200A")
    Return()

    label("loc_200A")

    EventBegin(0x0)
    OP_4A(0x27, 255)
    OP_8C(0x27, 225, 400)

    ChrTalk(    #46
        0x27,
        "Oh, right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x27, 0)
    TurnDirection(0x105, 0x27, 0)
    TurnDirection(0x103, 0x27, 0)

    ChrTalk(    #47
        0x27,
        (
            "I brought along my tools to\x01",
            "tune up everyone's orbments,\x01",
            "just in case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x27,
        (
            "I can also make a few tools \x01",
            "and pieces of equipment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        "#001FReally?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        "#027FThat was thoughtful of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x105,
        (
            "#041FThat should be useful.\x01",
            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x27,
        "I-It's really no big deal.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x27,
        (
            "If I can help out,\x01",
            "just say the word.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x65F)
    OP_8C(0x27, 270, 0)
    OP_4B(0x27, 255)
    EventEnd(0x1)
    Return()

    # Function_23_2002 end

    def Function_24_218E(): pass

    label("Function_24_218E")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x105, 46310, 200, 4320, 176)
    SetChrPos(0x103, 46840, 200, 3150, 0)
    SetChrPos(0x101, 45710, 200, 3160, 0)
    OP_6D(46390, 250, 4580, 0)
    OP_0D()

    ChrTalk(    #54
        0x105,
        (
            "#042F#3PIt's already almost noon.\x02\x03",

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
        (0, "loc_228A"),
        (1, "loc_22A8"),
        (SWITCH_DEFAULT, "loc_2319"),
    )


    label("loc_228A")


    ChrTalk(    #55
        0x105,
        "#047F#3PI understand.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2319")

    label("loc_22A8")


    ChrTalk(    #56
        0x105,
        "#040F#3PI understand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
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

    label("loc_2319")

    OP_28(0x4D, 0x1, 0x20)
    OP_4A(0x27, 255)
    TurnDirection(0x27, 0x105, 400)
    OP_6D(47340, 250, 3680, 1000)

    ChrTalk(    #58
        0x105,
        "#040F#3PPayton, could you help us?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x27,
        "#2PRoger that!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x27,
        (
            "#2PI'll handle the engine.\x01",
            "You can just focus on\x01",
            "flying, Your Highness!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #61
        0x101,
        "#1P#002FIt's finally time, Schera...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #62
        0x103,
        (
            "#026F#2PYes...\x02\x03",

            "#020FIt'll be a difficult mission,\x01",
            "but the fundamentals are as\x01",
            "important as ever.\x02\x03",

            "Speed...and steadiness.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3F0)
    NewScene("ED6_DT01/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_24_218E end

    def Function_25_249A(): pass

    label("Function_25_249A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCB, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2634")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2531")
    TurnDirection(0x105, 0x0, 400)

    ChrTalk(    #63
        0x105,
        (
            "#043FUmm...\x01",
            "It's already almost noon.\x02\x03",

            "If everyone's ready, we\x01",
            "should board the ship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #64
        0x101,
        "#006FRoger!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2619")

    label("loc_2531")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25BE")
    TurnDirection(0x103, 0x1, 400)

    ChrTalk(    #65
        0x103,
        (
            "#022FThere's no time before the\x01",
            "plan is put into action.\x02\x03",

            "If the equipment is ready, then\x01",
            "we should get on-board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2619")

    label("loc_25BE")

    TurnDirection(0x105, 0x1, 400)

    ChrTalk(    #66
        0x105,
        (
            "#042FIt's already almost noon.\x02\x03",

            "If everyone's ready, we\x01",
            "should board the ship.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2619")

    OP_90(0x0, 0x7D0, 0x0, 0x0, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)

    label("loc_2634")

    Return()

    # Function_25_249A end

    SaveToFile()

Try(main)
