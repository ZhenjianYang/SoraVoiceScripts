from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'R1203   ._SN',
        MapName             = 'Bose',
        Location            = 'R1203.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60086",
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
        '约修亚',                               # 9
        '乔丝特',                               # 10
        '多伦',                                 # 11
        '吉尔',                                 # 12
        '特务兵',                               # 13
        '特务兵',                               # 14
        '特务兵',                               # 15
        '特务兵',                               # 16
        '特务兵',                               # 17
        '特务兵',                               # 18
        ' ',                                    # 19
        '古罗尼山道方向',                       # 20
        '柏斯方向',                             # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
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
        'ED6_DT09/CH10290 ._CH',             # 00
        'ED6_DT09/CH10291 ._CH',             # 01
        'ED6_DT09/CH10310 ._CH',             # 02
        'ED6_DT09/CH10311 ._CH',             # 03
        'ED6_DT09/CH10320 ._CH',             # 04
        'ED6_DT09/CH10321 ._CH',             # 05
        'ED6_DT09/CH10330 ._CH',             # 06
        'ED6_DT09/CH10331 ._CH',             # 07
        'ED6_DT09/CH10350 ._CH',             # 08
        'ED6_DT09/CH10351 ._CH',             # 09
        'ED6_DT09/CH10540 ._CH',             # 0A
        'ED6_DT09/CH10541 ._CH',             # 0B
        'ED6_DT09/CH10550 ._CH',             # 0C
        'ED6_DT09/CH10551 ._CH',             # 0D
        'ED6_DT09/CH10870 ._CH',             # 0E
        'ED6_DT09/CH10871 ._CH',             # 0F
        'ED6_DT09/CH10900 ._CH',             # 10
        'ED6_DT09/CH10901 ._CH',             # 11
        'ED6_DT27/CH03010 ._CH',             # 12
        'ED6_DT27/CH03100 ._CH',             # 13
        'ED6_DT07/CH02110 ._CH',             # 14
        'ED6_DT07/CH02120 ._CH',             # 15
        'ED6_DT07/CH00340 ._CH',             # 16
        'ED6_DT27/CH04010 ._CH',             # 17
        'ED6_DT07/CH00310 ._CH',             # 18
        'ED6_DT07/CH00312 ._CH',             # 19
        'ED6_DT07/CH00290 ._CH',             # 1A
        'ED6_DT07/CH00292 ._CH',             # 1B
        'ED6_DT07/CH00300 ._CH',             # 1C
        'ED6_DT07/CH00305 ._CH',             # 1D
        'ED6_DT07/CH00306 ._CH',             # 1E
        'ED6_DT07/CH00341 ._CH',             # 1F
        'ED6_DT07/CH00343 ._CH',             # 20
        'ED6_DT07/CH00344 ._CH',             # 21
        'ED6_DT07/CH00440 ._CH',             # 22
        'ED6_DT07/CH00441 ._CH',             # 23
        'ED6_DT07/CH00443 ._CH',             # 24
        'ED6_DT07/CH00444 ._CH',             # 25
        'ED6_DT26/CH20299 ._CH',             # 26
        'ED6_DT07/CH00316 ._CH',             # 27
        'ED6_DT27/CH04012 ._CH',             # 28
        'ED6_DT27/CH04017 ._CH',             # 29
        'ED6_DT27/CH0401A ._CH',             # 2A
    )

    AddCharChipPat(
        'ED6_DT09/CH10290P._CP',             # 00
        'ED6_DT09/CH10291P._CP',             # 01
        'ED6_DT09/CH10310P._CP',             # 02
        'ED6_DT09/CH10311P._CP',             # 03
        'ED6_DT09/CH10320P._CP',             # 04
        'ED6_DT09/CH10321P._CP',             # 05
        'ED6_DT09/CH10330P._CP',             # 06
        'ED6_DT09/CH10331P._CP',             # 07
        'ED6_DT09/CH10350P._CP',             # 08
        'ED6_DT09/CH10351P._CP',             # 09
        'ED6_DT09/CH10540P._CP',             # 0A
        'ED6_DT09/CH10541P._CP',             # 0B
        'ED6_DT09/CH10550P._CP',             # 0C
        'ED6_DT09/CH10551P._CP',             # 0D
        'ED6_DT09/CH10870P._CP',             # 0E
        'ED6_DT09/CH10871P._CP',             # 0F
        'ED6_DT09/CH10900P._CP',             # 10
        'ED6_DT09/CH10901P._CP',             # 11
        'ED6_DT27/CH03010P._CP',             # 12
        'ED6_DT27/CH03100P._CP',             # 13
        'ED6_DT07/CH02110P._CP',             # 14
        'ED6_DT07/CH02120P._CP',             # 15
        'ED6_DT07/CH00340P._CP',             # 16
        'ED6_DT27/CH04010P._CP',             # 17
        'ED6_DT07/CH00310P._CP',             # 18
        'ED6_DT07/CH00312P._CP',             # 19
        'ED6_DT07/CH00290P._CP',             # 1A
        'ED6_DT07/CH00292P._CP',             # 1B
        'ED6_DT07/CH00300P._CP',             # 1C
        'ED6_DT07/CH00305P._CP',             # 1D
        'ED6_DT07/CH00306P._CP',             # 1E
        'ED6_DT07/CH00341P._CP',             # 1F
        'ED6_DT07/CH00343P._CP',             # 20
        'ED6_DT07/CH00344P._CP',             # 21
        'ED6_DT07/CH00440P._CP',             # 22
        'ED6_DT07/CH00441P._CP',             # 23
        'ED6_DT07/CH00443P._CP',             # 24
        'ED6_DT07/CH00444P._CP',             # 25
        'ED6_DT26/CH20299P._CP',             # 26
        'ED6_DT07/CH00316P._CP',             # 27
        'ED6_DT27/CH04012P._CP',             # 28
        'ED6_DT27/CH04017P._CP',             # 29
        'ED6_DT27/CH0401AP._CP',             # 2A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
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
        Unknown3            = 35,
        ChipIndex           = 0x23,
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
        Unknown3            = 35,
        ChipIndex           = 0x23,
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
        Unknown3            = 35,
        ChipIndex           = 0x23,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        Unknown3            = 31,
        ChipIndex           = 0x1F,
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
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -505000,
        Z                   = 10,
        Y                   = 56760,
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
        X                   = -352510,
        Z                   = 0,
        Y                   = 15930,
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


    DeclMonster(
        X                   = -391300,
        Z                   = -10,
        Y                   = 18680,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -416900,
        Z                   = 560,
        Y                   = 32439,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -468920,
        Z                   = 50,
        Y                   = 69100,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -449270,
        Z                   = -30,
        Y                   = 48370,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xF6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -454930,
        TriggerZ            = 510,
        TriggerY            = 62180,
        TriggerRange        = 1000,
        ActorX              = -454930,
        ActorZ              = 510,
        ActorY              = 62880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_436",          # 00, 0
        "Function_1_44A",          # 01, 1
        "Function_2_46B",          # 02, 2
        "Function_3_1D6D",         # 03, 3
        "Function_4_1DD4",         # 04, 4
        "Function_5_1E3B",         # 05, 5
        "Function_6_1EB6",         # 06, 6
        "Function_7_1F31",         # 07, 7
        "Function_8_1FAC",         # 08, 8
        "Function_9_2027",         # 09, 9
        "Function_10_207A",        # 0A, 10
        "Function_11_20CD",        # 0B, 11
        "Function_12_216D",        # 0C, 12
        "Function_13_220D",        # 0D, 13
        "Function_14_2284",        # 0E, 14
        "Function_15_22C2",        # 0F, 15
    )


    def Function_0_436(): pass

    label("Function_0_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_449")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)

    label("loc_449")

    Return()

    # Function_0_436 end

    def Function_1_44A(): pass

    label("Function_1_44A")

    OP_16(0x2, 0xFA0, 0xFFF77480, 0xFFFEA070, 0x23001B)
    OP_64(0x0, 0x1)
    OP_71(0x0, 0x0)
    OP_71(0x0, 0x4)
    Return()

    # Function_1_44A end

    def Function_2_46B(): pass

    label("Function_2_46B")

    EventBegin(0x0)
    ClearMapFlags(0x10)
    LoadEffect(0x0, "map\\\\mp019_00.eff")
    LoadEffect(0x1, "monster\\ms00300.eff")
    LoadEffect(0x2, "battle\\btgun00.eff")
    LoadEffect(0x3, "monster\\msc0130.eff")
    LoadEffect(0x4, "Craft\\\\cr161_00.eff")
    LoadEffect(0x5, "monster\\msc0100.eff")
    LoadEffect(0x6, "map\\mp047_00.eff")
    LoadEffect(0x7, "craft\\\\cr162_02.eff")
    OP_6D(-377740, 0, 17860, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(118000, 0)
    OP_6E(626, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrChipByIndex(0xA, 26)
    SetChrChipByIndex(0x9, 24)
    SetChrChipByIndex(0xB, 28)
    SetChrPos(0xA, -418370, 10, 17500, 90)
    SetChrPos(0xB, -405790, 1120, 27140, 270)
    SetChrPos(0x9, -404680, 1120, 10760, 180)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x11, 0x40)
    SetChrPos(0xC, -344960, 0, 16730, 270)
    SetChrPos(0xD, -345890, 0, 18630, 270)
    SetChrPos(0xE, -350960, 0, 15420, 270)
    SetChrPos(0xF, -348390, 0, 16440, 270)
    SetChrPos(0x10, -348330, 0, 17970, 270)
    SetChrPos(0x11, -350850, 0, 16990, 270)

    def lambda_675():
        OP_6E(426, 18000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_675)
    OP_C8(0x200, 0x46, "C_PLAC13._CH", 0x0, 0x3E8)
    FadeToBright(2000, 0)
    OP_43(0xC, 0x0, 0x0, 0x3)
    OP_43(0xD, 0x0, 0x0, 0x4)
    OP_43(0xE, 0x0, 0x0, 0x5)
    OP_43(0xF, 0x0, 0x0, 0x6)
    OP_43(0x10, 0x0, 0x0, 0x7)
    OP_43(0x11, 0x0, 0x0, 0x8)
    Sleep(8000)

    def lambda_6D2():
        OP_6D(-398320, 0, 19820, 10000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_6D2)

    def lambda_6EA():
        OP_67(0, 5400, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_6EA)

    def lambda_702():
        OP_6C(62000, 10000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_702)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    WaitChrThread(0x0, 0x3)
    Fade(1000)
    OP_6D(-415430, 5330, 19650, 0)
    OP_67(0, 3540, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(90000, 0)
    OP_6E(426, 0)
    SetChrPos(0xA, -423010, 5360, 19710, 90)
    OP_44(0xC, 0x0)
    SetChrPos(0xC, -394550, 0, 19140, 270)

    def lambda_78E():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_78E)
    OP_44(0xD, 0x0)
    SetChrPos(0xD, -395580, 0, 21300, 270)

    def lambda_7B9():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_7B9)
    OP_44(0xE, 0x0)
    SetChrPos(0xE, -399330, 0, 17930, 270)

    def lambda_7E4():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_7E4)
    OP_44(0xF, 0x0)
    SetChrPos(0xF, -397170, 0, 19450, 270)

    def lambda_80F():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_80F)
    OP_44(0x10, 0x0)
    SetChrPos(0x10, -397650, 0, 21940, 270)

    def lambda_83A():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_83A)
    OP_44(0x11, 0x0)
    SetChrPos(0x11, -399630, 0, 20170, 270)

    def lambda_865():
        OP_94(0x0, 0xFE, 0x0, 0x2710, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_865)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0 op#A op#5
        0xA,
        "#196F#5S#5P#20A喝啊啊啊啊！\x05\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_44(0xC, 0x0)
    SetChrSubChip(0xC, 0)
    OP_44(0xD, 0x0)
    SetChrSubChip(0xD, 0)
    OP_44(0xE, 0x0)
    SetChrSubChip(0xE, 0)
    OP_44(0xF, 0x0)
    SetChrSubChip(0xF, 0)
    OP_44(0x10, 0x0)
    SetChrSubChip(0x10, 0)
    OP_44(0x11, 0x0)
    SetChrSubChip(0x11, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_8EE():
        OP_6D(-402920, 0, 19580, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_8EE)

    def lambda_906():
        OP_67(0, 4880, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_906)

    def lambda_91E():
        OP_6C(82000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_91E)

    def lambda_92E():
        OP_96(0xFE, 0xFFF9BBDC, 0x0, 0x4858, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_92E)

    def lambda_94C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_94C)
    WaitChrThread(0xA, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_96D():
        OP_96(0xFE, 0xFFF9C2F8, 0x0, 0x4984, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_96D)
    WaitChrThread(0xA, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    SetChrPos(0x12, -400080, 0, 20260, 0)
    SetChrChipByIndex(0xA, 27)
    OP_99(0xA, 0x0, 0x4, 0x3E8)
    OP_22(0x1FA, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0xA, 250, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(100)
    OP_99(0xA, 0x4, 0x0, 0x3E8)
    Sleep(700)
    OP_43(0xF, 0x0, 0x0, 0xA)
    OP_7C(0x64, 0x64, 0xBB8, 0x190)
    Sleep(50)
    OP_43(0xD, 0x0, 0x0, 0x9)
    Sleep(50)
    OP_43(0x11, 0x0, 0x0, 0xA)
    Sleep(50)
    OP_43(0xC, 0x0, 0x0, 0x9)
    Sleep(50)
    OP_43(0xE, 0x0, 0x0, 0x9)
    OP_43(0x10, 0x0, 0x0, 0xA)
    Sleep(1000)

    ChrTalk(    #1
        0xA,
        "#196F#6P吉尔，下一个！\x02",
    )

    CloseMessageWindow()

    def lambda_A71():
        OP_6D(-401900, 60, 23650, 400)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_A71)

    def lambda_A89():
        OP_6C(70000, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_A89)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #2
        0xB,
        "#201F#5P交给我吧大哥！\x02",
    )

    SetChrChipByIndex(0xB, 29)
    OP_99(0xB, 0x0, 0x3, 0x6D6)
    OP_99(0xB, 0x0, 0x3, 0x6D6)
    CloseMessageWindow()
    OP_22(0xA3, 0x0, 0x64)

    def lambda_ADB():
        OP_96(0xFE, 0xFFF9CAC8, 0x2E4, 0x65AE, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_ADB)
    Sleep(100)
    OP_8C(0xB, 205, 0)
    Sleep(100)
    OP_8C(0xB, 160, 0)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_B1B():
        OP_6D(-400120, 0, 21590, 600)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_B1B)

    def lambda_B33():
        OP_6C(90000, 600)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_B33)
    SetChrChipByIndex(0xB, 29)
    SetChrSubChip(0xB, 4)
    OP_8C(0xB, 115, 0)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_B59():
        OP_96(0xFE, 0xFFF9D1C6, 0xD2, 0x5F78, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_B59)
    WaitChrThread(0xB, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    Sleep(100)
    SetChrChipByIndex(0xB, 30)
    SetChrSubChip(0xB, 1)
    SetChrPos(0x12, -399630, 0, 20170, 0)
    PlayEffect(0x1, 0x1, 0xB, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x12, -400940, 0, 21210, 0)
    PlayEffect(0x1, 0x2, 0xB, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(100)
    SetChrPos(0x12, -399060, 0, 18490, 0)
    PlayEffect(0x1, 0x3, 0xB, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(1300)
    OP_43(0xF, 0x0, 0x0, 0xA)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Sleep(50)
    OP_43(0x11, 0x0, 0x0, 0xA)
    Sleep(100)
    OP_43(0xC, 0x0, 0x0, 0x9)
    OP_43(0xD, 0x0, 0x0, 0x9)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0xA)
    OP_43(0xE, 0x0, 0x0, 0x9)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Fade(250)
    SetChrChipByIndex(0xB, 28)
    OP_0D()
    Sleep(500)

    ChrTalk(    #3
        0xB,
        "#201F#6P#3S乔丝特！\x02",
    )

    CloseMessageWindow()

    def lambda_D06():
        OP_6D(-401900, 60, 14630, 600)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D06)

    def lambda_D1E():
        OP_6C(112000, 600)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_D1E)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)

    ChrTalk(    #4
        0x9,
        "#210F#6PＯＫ！\x02",
    )

    CloseMessageWindow()
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x9, 0x4)

    def lambda_D56():
        OP_96(0xFE, 0xFFF9CC62, 0x140, 0x32D2, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D56)

    def lambda_D74():
        OP_8C(0xFE, 51, 400)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D74)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_D8C():
        OP_6D(-398750, 50, 17130, 600)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_D8C)

    def lambda_DA4():
        OP_6C(96000, 600)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_DA4)

    def lambda_DB4():
        OP_96(0xFE, 0xFFF9D59A, 0x244, 0x3912, 0x258, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DB4)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    ClearChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x9, 39)
    SetChrSubChip(0x9, 0)
    Sleep(200)
    SetChrChipByIndex(0x9, 39)
    SetChrSubChip(0x9, 1)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    SetChrPos(0x12, -401340, 0, 20290, 0)
    PlayEffect(0x1, 0x1, 0x9, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(50)
    SetChrPos(0x12, -399070, 0, 18620, 0)
    PlayEffect(0x1, 0x2, 0x9, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(100)
    SetChrPos(0x12, -399810, 0, 21560, 0)
    PlayEffect(0x1, 0x3, 0x9, 250, 200, 330, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    Sleep(350)
    SetChrChipByIndex(0x9, 25)
    OP_99(0x9, 0x0, 0x2, 0x3E8)
    SetChrPos(0x12, -401340, 0, 20290, 0)
    PlayEffect(0x2, 0x4, 0x9, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    OP_83(0x4, 0x2)
    OP_82(0x1, 0x0)
    PlayEffect(0x3, 0xFF, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_43(0x9, 0x3, 0x0, 0xD)
    SetChrPos(0x12, -399070, 0, 18620, 0)
    PlayEffect(0x2, 0x5, 0x9, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)
    OP_83(0x5, 0x2)
    OP_82(0x2, 0x0)
    PlayEffect(0x3, 0xFF, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x12, -399810, 0, 21560, 0)
    PlayEffect(0x2, 0x6, 0x9, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0x12, 0, 0, 0, 0)

    def lambda_1041():
        OP_99(0xFE, 0x2, 0x7, 0x7D0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1041)
    OP_83(0x6, 0x2)
    OP_82(0x3, 0x0)
    PlayEffect(0x3, 0xFF, 0x12, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    ChrTalk(    #5
        0x9,
        "#214F#4P约修亚！\x02",
    )

    CloseMessageWindow()

    def lambda_10A7():
        OP_6D(-392600, 0, 21260, 1000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_10A7)

    def lambda_10BF():
        OP_67(0, 3400, -10000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10BF)

    def lambda_10D7():
        OP_6C(82000, 1000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_10D7)

    def lambda_10E7():
        OP_6E(400, 1000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_10E7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -392600, 0, 21260, 270)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 42)
    SetChrSubChip(0x8, 0)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    WaitChrThread(0x0, 0x3)
    PlayEffect(0x7, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    OP_99(0x8, 0x0, 0x7, 0x7D0)
    Sleep(500)
    OP_8C(0xC, 260, 0)
    OP_8C(0xD, 260, 0)
    OP_8C(0xE, 260, 0)
    OP_8C(0xF, 260, 0)
    OP_8C(0x10, 260, 0)
    OP_8C(0x11, 260, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0x0, 0x8, 0x14, 0x1F4)

    def lambda_11CE():
        OP_6D(-400180, 10, 18460, 2000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_11CE)

    def lambda_11E6():
        OP_6C(114000, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_11E6)

    def lambda_11F6():
        OP_6E(380, 2000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_11F6)
    SetChrChipByIndex(0x8, 40)
    SetChrSubChip(0x8, 7)

    def lambda_1210():
        OP_96(0xFE, 0xFFF9D37E, 0x0, 0x4C86, 0x64, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_1210)

    def lambda_122E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0xC8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_122E)
    WaitChrThread(0x8, 0x0)
    PlayEffect(0x4, 0x0, 0xC, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 36)

    def lambda_1284():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1284)

    def lambda_129F():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_129F)
    Sleep(200)
    PlayEffect(0x4, 0x1, 0x10, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrFlags(0x10, 0x20)
    SetChrChipByIndex(0x10, 32)

    def lambda_12FD():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_12FD)

    def lambda_1318():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1318)
    Sleep(200)
    PlayEffect(0x4, 0x2, 0xE, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrFlags(0xE, 0x20)
    SetChrChipByIndex(0xE, 36)

    def lambda_1376():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1376)

    def lambda_1391():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1391)
    Sleep(200)
    PlayEffect(0x4, 0x3, 0xD, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrFlags(0xD, 0x20)
    SetChrChipByIndex(0xD, 36)

    def lambda_13EF():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_13EF)

    def lambda_140A():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_140A)
    Sleep(200)
    PlayEffect(0x4, 0x4, 0x11, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrFlags(0x11, 0x20)
    SetChrChipByIndex(0x11, 32)

    def lambda_1468():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1468)

    def lambda_1483():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1483)
    Sleep(200)
    PlayEffect(0x4, 0x5, 0xF, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xC, 0, 0, 0, 0)
    SetChrFlags(0xF, 0x20)
    SetChrChipByIndex(0xF, 32)

    def lambda_14E1():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_14E1)

    def lambda_14FC():
        OP_9E(0xFE, 0x1E, 0x0, 0x320, 0xFA0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_14FC)
    OP_83(0x5, 0x2)
    OP_22(0x9B, 0x0, 0x64)
    Sleep(1000)
    PlayEffect(0x7, 0x1, 0x8, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x8, -404610, 0, 19590, 270)

    def lambda_1569():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1569)
    WaitChrThread(0x8, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_7D(0x1, 0x8, 0x0, 0x0)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    Sleep(1000)

    ChrTalk(    #6
        0x8,
        "#1035F#6P……………………………\x02",
    )

    CloseMessageWindow()
    OP_99(0x8, 0x7, 0xB, 0x5DC)
    SetChrChipByIndex(0x8, 41)
    SetChrSubChip(0x8, 2)
    SetChrFlags(0x8, 0x2)
    OP_99(0x8, 0x2, 0x10, 0x5DC)
    OP_8C(0xB, 124, 0)
    OP_8C(0xC, 254, 0)
    OP_8C(0xD, 254, 0)
    OP_8C(0xE, 254, 0)
    OP_8C(0xF, 254, 0)
    OP_8C(0x10, 254, 0)
    OP_8C(0x11, 254, 0)

    def lambda_161C():
        OP_6D(-400090, 10, 18730, 4000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_161C)

    def lambda_1634():
        OP_6C(100000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_1634)

    def lambda_1644():
        OP_6E(448, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1644)
    OP_43(0xC, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0x10, 0x0, 0x0, 0xC)
    Sleep(200)
    OP_43(0xE, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0xD, 0x0, 0x0, 0xB)
    Sleep(200)
    OP_43(0x11, 0x0, 0x0, 0xC)
    Sleep(200)
    OP_43(0xF, 0x0, 0x0, 0xC)
    FadeToDark(2500, 16777215, -1)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    Sleep(2000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 38)
    SetChrSubChip(0xC, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 38)
    SetChrSubChip(0xE, 1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x2)
    SetChrChipByIndex(0x10, 38)
    SetChrSubChip(0x10, 2)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x2)
    SetChrChipByIndex(0x11, 38)
    SetChrSubChip(0x11, 2)
    OP_6D(-404970, 0, 18110, 0)
    OP_67(0, 6240, -10000, 0)
    OP_6C(118000, 0)
    OP_6E(368, 0)

    def lambda_173E():
        OP_6E(368, 3000)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_173E)
    OP_20(0xBB8)
    FadeToBright(3000, 16777215)
    SetChrChipByIndex(0x9, 19)
    TurnDirection(0x9, 0x8, 400)

    def lambda_1768():
        OP_8E(0xFE, 0xFFF9CBCC, 0x0, 0x4588, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1768)
    SetChrChipByIndex(0xB, 21)
    TurnDirection(0xB, 0x8, 400)

    def lambda_178F():
        OP_8E(0xFE, 0xFFF9C924, 0x0, 0x4F60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_178F)
    SetChrChipByIndex(0xA, 20)
    TurnDirection(0xA, 0x8, 400)

    def lambda_17B6():
        OP_8E(0xFE, 0xFFF9C88E, 0x0, 0x4AB0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17B6)
    WaitChrThread(0x9, 0x1)

    def lambda_17D6():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17D6)
    WaitChrThread(0xB, 0x1)

    def lambda_17E9():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_17E9)
    WaitChrThread(0xA, 0x1)

    def lambda_17FC():
        TurnDirection(0xFE, 0x8, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_17FC)
    WaitChrThread(0x0, 0x0)
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    WaitChrThread(0x0, 0x3)
    OP_0D()
    OP_1D(0x54)

    ChrTalk(    #7
        0xB,
        (
            "#202F#6P嘿嘿，你的本事\x01",
            "还是一样地出色嘛。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x8, 18)
    SetChrSubChip(0x8, 0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)

    ChrTalk(    #8
        0x8,
        (
            "#1031F#5P……你们的\x01",
            "连携攻击才是相当漂亮。\x02\x03",

            "托你们的福一口气解决了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x9,
        (
            "#413F#4P哼、哼……\x01",
            "拍马屁也没有什么好处哦。\x02\x03",

            "#212F这是第１０只了吧？\x01",
            "还要再猎杀多少才行呢？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x8,
        (
            "#1033F#5P是啊……\x01",
            "我想差不多该猎杀完毕了。\x02\x03",

            "#1035F王国军大概也出动了\x01",
            "我们就在这里收手吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x9,
        "#210F#4P是吗……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xA,
        (
            "#198F#4P不过这结社\x01",
            "还真不知道在想些什么。\x02\x03",

            "#190F为什么要让那些\x01",
            "黑小子的人偶四处游荡啊？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        (
            "#206F#6P对，就是这个。\x02\x03",

            "真正的特务兵余党们\x01",
            "到底去哪儿了？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "#1035F#5P或许，很有可能是\x01",
            "那张纸条上提到的『茶会』……\x02\x03",

            "#1031F人形兵器恐怕是用来\x01",
            "转移军方的注意力吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xB,
        (
            "#203F#6P原来如此啊……\x02\x03",

            "#207F虽然不知道在哪儿搞什么鬼\x01",
            "但是总感觉十分可疑。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xA,
        (
            "#198F#4P不过，我们也没有\x01",
            "义务要出手……\x02\x03",

            "#197F那个『茶会』\x01",
            "也可以不管吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "#1033F#5P…………………………………\x02\x03",

            "#1035F现在游击士们\x01",
            "应该正在搜索那个废坑。\x02\x03",

            "就这样交给军方和协会吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x9,
        (
            "#210F#4P是啊是啊，留下\x01",
            "纸条和设计图就足够了。\x02\x03",

            "反正也帮协会\x01",
            "处理了人偶。\x02\x03",

            "#211F之后的事情交给那个\x01",
            "少根筋的女人他们就行了吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x8,
        "#1033F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        (
            "#216F#4P哼，哼，什么嘛。\x02\x03",

            "#215F到现在还在担心以前的同伴？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#1035F#5P不……\x01",
            "他们已经和我无关了。\x02\x03",

            "#1031F如果『茶会』开始的话\x01",
            "军方的注意力也会集中到那边。\x02\x03",

            "这样的机会可不能错过。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xA,
        "#490F#4P哦！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xB,
        "#202F#6P那么～看来有得忙啰。\x02",
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    Sleep(1000)
    OP_22(0xD, 0x0, 0x64)
    Sleep(5000)
    OP_A2(0x10F0)
    SetMapFlags(0x10)
    NewScene("ED6_DT21/T4302   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_46B end

    def Function_3_1D6D(): pass

    label("Function_3_1D6D")

    OP_8E(0xFE, 0xFFFA3FEE, 0x0, 0x415A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA27A2, 0x0, 0x53D4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA14EC, 0x0, 0x53D4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9FACA, 0x0, 0x4AC4, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_94(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    Return()

    # Function_3_1D6D end

    def Function_4_1DD4(): pass

    label("Function_4_1DD4")

    OP_8E(0xFE, 0xFFFA3ED6, 0x0, 0x48C6, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA2FF4, 0x0, 0x5B36, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA119A, 0x0, 0x5B36, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9F6C4, 0x0, 0x5334, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_94(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    Return()

    # Function_4_1DD4 end

    def Function_5_1E3B(): pass

    label("Function_5_1E3B")

    OP_8E(0xFE, 0xFFFA3C7E, 0x0, 0x3C3C, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA273E, 0x0, 0x51A4, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA1258, 0x0, 0x5140, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9EC06, 0x0, 0x460A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9E81E, 0x0, 0x460A, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_94(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    Return()

    # Function_5_1E3B end

    def Function_6_1EB6(): pass

    label("Function_6_1EB6")

    OP_8E(0xFE, 0xFFFA3B52, 0x0, 0x4038, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA2932, 0x0, 0x5578, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA1820, 0x0, 0x5578, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA05F6, 0x0, 0x4E52, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9F08E, 0x0, 0x4BFA, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_94(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    Return()

    # Function_6_1EB6 end

    def Function_7_1F31(): pass

    label("Function_7_1F31")

    OP_8E(0xFE, 0xFFFA3F12, 0x0, 0x4632, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA28C4, 0x0, 0x5D2A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA1294, 0x0, 0x5D2A, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9FFE8, 0x0, 0x5500, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9EEAE, 0x0, 0x55B4, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_94(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    Return()

    # Function_7_1F31 end

    def Function_8_1FAC(): pass

    label("Function_8_1FAC")

    OP_8E(0xFE, 0xFFFA3EFE, 0x0, 0x425E, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA27A2, 0x0, 0x5938, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFFA110E, 0x0, 0x5938, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9F3CC, 0x0, 0x4ECA, 0xBB8, 0x0)
    OP_8E(0xFE, 0xFFF9E6F2, 0x0, 0x4ECA, 0xBB8, 0x0)
    OP_8C(0xFE, 270, 0)
    OP_94(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    Return()

    # Function_8_1FAC end

    def Function_9_2027(): pass

    label("Function_9_2027")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 36)

    def lambda_2037():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2037)

    def lambda_2052():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2052)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 35)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_9_2027 end

    def Function_10_207A(): pass

    label("Function_10_207A")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 32)

    def lambda_208A():
        OP_91(0xFE, 0x1F4, 0x0, 0x64, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_208A)

    def lambda_20A5():
        OP_9E(0xFE, 0x14, 0x0, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_20A5)
    WaitChrThread(0xFE, 0x1)
    OP_44(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 31)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_10_207A end

    def Function_11_20CD(): pass

    label("Function_11_20CD")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 37)

    def lambda_20DD():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_20DD)
    PlayEffect(0x5, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1200)
    PlayEffect(0x6, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x80)
    OP_7C(0x64, 0x64, 0xBB8, 0x190)
    Return()

    # Function_11_20CD end

    def Function_12_216D(): pass

    label("Function_12_216D")

    ClearChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 33)

    def lambda_217D():
        OP_99(0xFE, 0x0, 0x3, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_217D)
    PlayEffect(0x5, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1200)
    PlayEffect(0x6, 0xFF, 0xFE, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x80)
    OP_7C(0x64, 0x64, 0xBB8, 0x190)
    Return()

    # Function_12_216D end

    def Function_13_220D(): pass

    label("Function_13_220D")

    OP_43(0xF, 0x0, 0x0, 0xA)
    Sleep(50)
    OP_43(0x11, 0x0, 0x0, 0xA)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Sleep(100)
    OP_43(0xC, 0x0, 0x0, 0x9)
    Sleep(50)
    OP_43(0xD, 0x0, 0x0, 0x9)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Sleep(100)
    OP_43(0x10, 0x0, 0x0, 0xA)
    Sleep(50)
    OP_43(0xE, 0x0, 0x0, 0x9)
    OP_7C(0x64, 0x64, 0xBB8, 0xC8)
    Return()

    # Function_13_220D end

    def Function_14_2284(): pass

    label("Function_14_2284")

    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(200)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Sleep(200)
    OP_7C(0xC8, 0xC8, 0xBB8, 0x3E8)
    Return()

    # Function_14_2284 end

    def Function_15_22C2(): pass

    label("Function_15_22C2")

    Return()

    # Function_15_22C2 end

    SaveToFile()

Try(main)
