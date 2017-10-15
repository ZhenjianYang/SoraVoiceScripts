from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5613   ._SN',
        MapName             = 'Other',
        Location            = 'C5613.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        'Black-Haired Boy',                     # 9
        'Black-Haired Boy',                     # 10
        'Black-Haired Boy',                     # 11
        'Renne',                                # 12
        'Loewe',                                # 13
        'Professor Weissmann',                  # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12320 ._CH',             # 02
        'ED6_DT29/CH12321 ._CH',             # 03
        'ED6_DT29/CH12330 ._CH',             # 04
        'ED6_DT29/CH12331 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
        'ED6_DT26/CH20375 ._CH',             # 0A
        'ED6_DT27/CH03005 ._CH',             # 0B
        'ED6_DT27/CH04560 ._CH',             # 0C
        'ED6_DT27/CH04561 ._CH',             # 0D
        'ED6_DT07/CH00112 ._CH',             # 0E
        'ED6_DT26/CH20377 ._CH',             # 0F
        'ED6_DT27/CH04000 ._CH',             # 10
        'ED6_DT27/CH04004 ._CH',             # 11
        'ED6_DT07/CH00124 ._CH',             # 12
        'ED6_DT07/CH00154 ._CH',             # 13
        'ED6_DT07/CH00134 ._CH',             # 14
        'ED6_DT07/CH00144 ._CH',             # 15
        'ED6_DT07/CH00164 ._CH',             # 16
        'ED6_DT07/CH00174 ._CH',             # 17
        'ED6_DT27/CH04084 ._CH',             # 18
        'ED6_DT27/CH03510 ._CH',             # 19
        'ED6_DT07/CH02040 ._CH',             # 1A
        'ED6_DT26/CH20378 ._CH',             # 1B
        'ED6_DT27/CH03550 ._CH',             # 1C
        'ED6_DT26/CH20212 ._CH',             # 1D
        'ED6_DT26/CH20215 ._CH',             # 1E
        'ED6_DT26/CH20213 ._CH',             # 1F
        'ED6_DT26/CH20214 ._CH',             # 20
        'ED6_DT26/CH20216 ._CH',             # 21
        'ED6_DT26/CH20217 ._CH',             # 22
        'ED6_DT26/CH20219 ._CH',             # 23
        'ED6_DT07/CH00120 ._CH',             # 24
        'ED6_DT07/CH00150 ._CH',             # 25
        'ED6_DT07/CH00130 ._CH',             # 26
        'ED6_DT07/CH00140 ._CH',             # 27
        'ED6_DT07/CH00160 ._CH',             # 28
        'ED6_DT07/CH00170 ._CH',             # 29
        'ED6_DT27/CH04080 ._CH',             # 2A
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12320P._CP',             # 02
        'ED6_DT29/CH12321P._CP',             # 03
        'ED6_DT29/CH12330P._CP',             # 04
        'ED6_DT29/CH12331P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
        'ED6_DT26/CH20375P._CP',             # 0A
        'ED6_DT27/CH03005P._CP',             # 0B
        'ED6_DT27/CH04560P._CP',             # 0C
        'ED6_DT27/CH04561P._CP',             # 0D
        'ED6_DT07/CH00112P._CP',             # 0E
        'ED6_DT26/CH20377P._CP',             # 0F
        'ED6_DT27/CH04000P._CP',             # 10
        'ED6_DT27/CH04004P._CP',             # 11
        'ED6_DT07/CH00124P._CP',             # 12
        'ED6_DT07/CH00154P._CP',             # 13
        'ED6_DT07/CH00134P._CP',             # 14
        'ED6_DT07/CH00144P._CP',             # 15
        'ED6_DT07/CH00164P._CP',             # 16
        'ED6_DT07/CH00174P._CP',             # 17
        'ED6_DT27/CH04084P._CP',             # 18
        'ED6_DT27/CH03510P._CP',             # 19
        'ED6_DT07/CH02040P._CP',             # 1A
        'ED6_DT26/CH20378P._CP',             # 1B
        'ED6_DT27/CH03550P._CP',             # 1C
        'ED6_DT26/CH20212P._CP',             # 1D
        'ED6_DT26/CH20215P._CP',             # 1E
        'ED6_DT26/CH20213P._CP',             # 1F
        'ED6_DT26/CH20214P._CP',             # 20
        'ED6_DT26/CH20216P._CP',             # 21
        'ED6_DT26/CH20217P._CP',             # 22
        'ED6_DT26/CH20219P._CP',             # 23
        'ED6_DT07/CH00120P._CP',             # 24
        'ED6_DT07/CH00150P._CP',             # 25
        'ED6_DT07/CH00130P._CP',             # 26
        'ED6_DT07/CH00140P._CP',             # 27
        'ED6_DT07/CH00160P._CP',             # 28
        'ED6_DT07/CH00170P._CP',             # 29
        'ED6_DT27/CH04080P._CP',             # 2A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
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
        Unknown3            = 26,
        ChipIndex           = 0x1A,
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
        Unknown3            = 27,
        ChipIndex           = 0x1B,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 33810,
        Z                   = 0,
        Y                   = 140000,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 68690,
        Z                   = 0,
        Y                   = 59150,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 43770,
        Z                   = 0,
        Y                   = 56260,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 40910,
        Z                   = 0,
        Y                   = 29220,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -30680,
        Y                   = 0,
        Z                   = 53220,
        Range               = -27120,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xDC64,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 19040,
        Y                   = -1000,
        Z                   = 143410,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 17,
    )


    DeclActor(
        TriggerX            = -33630,
        TriggerZ            = 0,
        TriggerY            = 11690,
        TriggerRange        = 1000,
        ActorX              = -33630,
        ActorZ              = 1000,
        ActorY              = 11690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_396",          # 00, 0
        "Function_1_3AF",          # 01, 1
        "Function_2_42A",          # 02, 2
        "Function_3_433",          # 03, 3
        "Function_4_10D5",         # 04, 4
        "Function_5_10F1",         # 05, 5
        "Function_6_110D",         # 06, 6
        "Function_7_1129",         # 07, 7
        "Function_8_1145",         # 08, 8
        "Function_9_1161",         # 09, 9
        "Function_10_117D",        # 0A, 10
        "Function_11_2983",        # 0B, 11
        "Function_12_29AF",        # 0C, 12
        "Function_13_29DB",        # 0D, 13
        "Function_14_2B3C",        # 0E, 14
        "Function_15_2BC5",        # 0F, 15
        "Function_16_2C22",        # 10, 16
        "Function_17_2E44",        # 11, 17
    )


    def Function_0_396(): pass

    label("Function_0_396")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AE")
    Event(0, 2)

    label("loc_3AE")

    Return()

    # Function_0_396 end

    def Function_1_3AF(): pass

    label("Function_1_3AF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x421), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 7)), scpexpr(EXPR_END)), "loc_3D4")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_429")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -33630, 1000, 11690, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)

    label("loc_429")

    Return()

    # Function_1_3AF end

    def Function_2_42A(): pass

    label("Function_2_42A")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_42A end

    def Function_3_433(): pass

    label("Function_3_433")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44A")
    Call(0, 14)
    Call(0, 15)

    label("loc_44A")

    SetChrPos(0x8, -28400, 0, 69850, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x40)
    ClearChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 48)
    SetChrPos(0x101, -28090, 20, 57140, 0)
    SetChrPos(0x109, -29480, 20, 57110, 0)
    SetChrPos(0xF8, -28090, 0, 55760, 0)
    SetChrPos(0xF9, -29480, 0, 55760, 0)
    OP_6D(-28600, 0, 57330, 0)
    OP_67(0, 8580, -10000, 0)
    OP_6B(2580, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0xBB8)

    def lambda_52B():
        OP_6D(-29160, 20, 70000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_52B)

    def lambda_543():
        OP_67(0, 6570, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_543)

    def lambda_55B():
        OP_6B(2580, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_55B)

    def lambda_56B():
        OP_6E(278, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_56B)
    WaitChrThread(0x101, 0x0)
    Sleep(1000)
    Fade(500)
    OP_6D(-29050, 10, 62510, 0)
    OP_67(0, 6100, -10000, 0)
    OP_6B(2410, 0)
    OP_6E(393, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #0
        0x101,
        "#3S#1020F#5PJOSHUA?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_1D(0x30)
    Sleep(500)

    def lambda_5F6():
        OP_8E(0x101, 0xFFFF8F08, 0x14, 0x10EB4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5F6)
    Sleep(500)
    Fade(500)
    OP_6D(-28990, 20, 70000, 0)
    OP_67(0, 6570, -10000, 0)
    OP_6B(2600, 0)
    OP_6E(290, 0)
    OP_0D()
    WaitChrThread(0x101, 0x0)
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 11)
    OP_0D()
    Sleep(500)

    def lambda_66A():
        OP_9E(0xFE, 0x0, 0xA, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_66A)
    OP_43(0x109, 0x1, 0x0, 0x4)
    Sleep(70)
    OP_43(0xF8, 0x1, 0x0, 0x5)
    Sleep(70)
    OP_43(0xF9, 0x1, 0x0, 0x6)

    ChrTalk(    #1
        0x101,
        (
            "#1023F#6PJoshua!\x02\x03",

            "Joshua, say something!\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D1():
        OP_9E(0xFE, 0x0, 0xA, 0x3E8, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6D1)
    Sleep(1500)

    ChrTalk(    #2
        0x101,
        (
            "#1027F#6PWh-Why are you s-so cold...\x02\x03",

            "#1014FWake up... WAKE UP!\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0xF9, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_757")

    ChrTalk(    #3
        0x105,
        "#049FNo...\x02",
    )

    CloseMessageWindow()

    label("loc_757")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77D")

    ChrTalk(    #4
        0x107,
        "#065FJ-Joshuaaa...\x02",
    )

    CloseMessageWindow()

    label("loc_77D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_79F")

    ChrTalk(    #5
        0x103,
        "#522FOh, no...\x02",
    )

    CloseMessageWindow()

    label("loc_79F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C2")

    ChrTalk(    #6
        0x106,
        "#552FDamn it...\x02",
    )

    CloseMessageWindow()

    label("loc_7C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DE")

    ChrTalk(    #7
        0x104,
        "#032FHm.\x02",
    )

    CloseMessageWindow()

    label("loc_7DE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7FA")

    ChrTalk(    #8
        0x108,
        "#572F...\x02",
    )

    CloseMessageWindow()

    label("loc_7FA")


    ChrTalk(    #9
        0x8,
        "#2P#40W...Nn.\x02",
    )

    OP_9E(0x8, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_87F")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BD")

    label("loc_87F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A6")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_8BD")

    label("loc_8A6")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_8BD")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E9")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_927")

    label("loc_8E9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_910")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_927")

    label("loc_910")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_927")

    Sleep(1000)

    ChrTalk(    #10
        0x101,
        "#1023F#6PJoshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "#2P#40WE... Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        "#2P#40WWhy are...you here...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#1027F#6POh, thank Aidios you're...\x02\x03",

            "#1005FHang on, I'll--\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x109,
        "#1069F#5PDAMN IT! Get away!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    LoadEffect(0x2, "map\\\\mp009_00.eff")
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_A21():
        OP_6B(2400, 500)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_A21)
    OP_20(0x190)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_A3B():
        OP_96(0xFE, 0xFFFF8FE4, 0x0, 0x1129C, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A3B)
    Sleep(50)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1)
    SetChrChipByIndex(0x8, 14)
    SetChrSubChip(0x8, 1)
    OP_8C(0x8, 180, 0)
    WaitChrThread(0x8, 0x1)
    OP_22(0x1F5, 0x0, 0x64)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x8, 14)

    def lambda_A92():
        OP_99(0x8, 0x1, 0xB, 0xFA0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A92)
    SetChrChipByIndex(0x101, 16)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1)
    Sleep(100)
    PlayEffect(0x2, 0x1, 0x101, 0, 500, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xD6, 0x0, 0x64)

    def lambda_AF0():
        OP_9E(0xFE, 0x14, 0x0, 0x7D0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AF0)

    def lambda_B0A():
        OP_9E(0xFE, 0x14, 0x0, 0x7D0, 0x9C4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B0A)
    WaitChrThread(0x8, 0x1)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)
    Sleep(50)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_43(0x109, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xF8, 0x1, 0x0, 0x8)
    Sleep(50)
    OP_43(0xF9, 0x1, 0x0, 0x9)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1021F#6PGyah!\x02",
    )

    CloseMessageWindow()

    def lambda_B79():
        OP_6D(-28920, 0, 70500, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B79)

    def lambda_B91():
        OP_67(0, 6800, -10000, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_B91)

    def lambda_BA9():
        OP_6B(2700, 500)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_BA9)
    OP_22(0xA3, 0x0, 0x64)
    SetChrChipByIndex(0x8, 10)
    SetChrSubChip(0x8, 0)

    def lambda_BC8():
        OP_96(0xFE, 0xFFFF8F08, 0x0, 0x11D14, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BC8)

    def lambda_BE6():
        OP_8F(0xFE, 0xFFFF8F08, 0x0, 0x10ACC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BE6)
    WaitChrThread(0x109, 0x3)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C27")

    ChrTalk(    #16
        0x105,
        "#043FWhat?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C27")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C4B")

    ChrTalk(    #17
        0x107,
        "#065FJoshua?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C73")

    ChrTalk(    #18
        0x103,
        "#024FWhat in...?!\x02",
    )

    CloseMessageWindow()
    Jump("loc_C98")

    label("loc_C73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C98")

    ChrTalk(    #19
        0x106,
        "#054FWhat in...?!\x02",
    )

    CloseMessageWindow()

    label("loc_C98")


    ChrTalk(    #20
        0x101,
        "#1020F#1PJ-Joshua...what...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        "#4P...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6D(-28920, 0, 71980, 0)
    OP_67(0, 6040, -10000, 0)
    OP_6B(2770, 0)
    OP_6C(0, 0)
    OP_6E(290, 0)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 6)
    OP_0D()
    OP_22(0x12C, 0x0, 0x50)
    OP_22(0x111, 0x0, 0x50)

    def lambda_D28():

        label("loc_D28")

        OP_99(0xFE, 0x20, 0x21, 0x9C4)
        OP_48()
        Jump("loc_D28")

    QueueWorkItem2(0x8, 1, lambda_D28)
    Sleep(1000)
    OP_44(0x8, 0x1)
    Fade(300)
    OP_99(0x8, 0x22, 0x25, 0x3E8)
    Fade(500)
    SetChrSubChip(0x8, 30)
    OP_0D()
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)

    NpcTalk(    #22
        0x8,
        "Black-Haired Doll",
        "#6P#1140F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1020F#5P#4SNO!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        "#1069F#5PA doll weapon!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DDF")

    ChrTalk(    #25
        0x104,
        "#530F#5PAs I feared!\x02",
    )

    CloseMessageWindow()

    label("loc_DDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E04")

    ChrTalk(    #26
        0x108,
        "#077F#5PHow vile!\x02",
    )

    CloseMessageWindow()

    label("loc_E04")

    Sleep(100)
    Fade(500)
    OP_6C(315000, 0)

    def lambda_E1D():
        OP_6D(-29050, 20, 68500, 0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E1D)

    def lambda_E35():
        OP_6B(2800, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E35)
    ClearChrFlags(0x8, 0x2)
    OP_8C(0x8, 180, 0)
    SetChrSubChip(0x8, 3)
    OP_0D()
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x9, 0x4)
    SetChrFlags(0xA, 0x4)
    SetChrPos(0x9, -32509, 3000, 64540, 45)
    SetChrPos(0xA, -24330, 3000, 64720, 315)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    def lambda_EA3():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_EA3)

    def lambda_EB5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_EB5)

    def lambda_EC7():
        OP_8F(0xFE, 0xFFFF8103, 0x0, 0xFC1C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EC7)
    OP_22(0x211, 0x0, 0x64)
    Sleep(200)

    def lambda_EEC():
        OP_8F(0xA, 0xFFFFA0F6, 0x0, 0xFCD0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_EEC)
    OP_22(0x211, 0x0, 0x64)
    WaitChrThread(0x9, 0x1)
    OP_22(0xA4, 0x0, 0x64)
    WaitChrThread(0xA, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_F20():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F20)
    Sleep(100)

    def lambda_F33():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_F33)
    Sleep(100)
    OP_8C(0xF8, 135, 400)
    SetChrChipByIndex(0x109, 42)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_F6D"),
        (5, "loc_F75"),
        (3, "loc_F7D"),
        (4, "loc_F85"),
        (6, "loc_F8D"),
        (7, "loc_F95"),
        (SWITCH_DEFAULT, "loc_F9D"),
    )


    label("loc_F6D")

    SetChrChipByIndex(0xF8, 36)
    Jump("loc_F9D")

    label("loc_F75")

    SetChrChipByIndex(0xF8, 37)
    Jump("loc_F9D")

    label("loc_F7D")

    SetChrChipByIndex(0xF8, 38)
    Jump("loc_F9D")

    label("loc_F85")

    SetChrChipByIndex(0xF8, 39)
    Jump("loc_F9D")

    label("loc_F8D")

    SetChrChipByIndex(0xF8, 40)
    Jump("loc_F9D")

    label("loc_F95")

    SetChrChipByIndex(0xF8, 41)
    Jump("loc_F9D")

    label("loc_F9D")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_FBE"),
        (5, "loc_FC6"),
        (3, "loc_FCE"),
        (4, "loc_FD6"),
        (6, "loc_FDE"),
        (7, "loc_FE6"),
        (SWITCH_DEFAULT, "loc_FEE"),
    )


    label("loc_FBE")

    SetChrChipByIndex(0xF9, 36)
    Jump("loc_FEE")

    label("loc_FC6")

    SetChrChipByIndex(0xF9, 37)
    Jump("loc_FEE")

    label("loc_FCE")

    SetChrChipByIndex(0xF9, 38)
    Jump("loc_FEE")

    label("loc_FD6")

    SetChrChipByIndex(0xF9, 39)
    Jump("loc_FEE")

    label("loc_FDE")

    SetChrChipByIndex(0xF9, 40)
    Jump("loc_FEE")

    label("loc_FE6")

    SetChrChipByIndex(0xF9, 41)
    Jump("loc_FEE")

    label("loc_FEE")

    Sleep(500)
    OP_1D(0x1B)
    Sleep(500)

    def lambda_1000():
        OP_6D(-28860, 20, 68620, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1000)

    def lambda_1018():
        OP_6B(2130, 300)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1018)
    ClearChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 13)

    def lambda_1032():
        OP_8E(0xFE, 0xFFFF8F12, 0x14, 0x111E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1032)
    Sleep(50)
    SetChrChipByIndex(0x9, 13)

    def lambda_1057():
        OP_8E(0xFE, 0xFFFF89B8, 0x14, 0x1072A, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1057)
    SetChrChipByIndex(0xA, 13)

    def lambda_1077():
        OP_8E(0xFE, 0xFFFF966A, 0x14, 0x105EA, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1077)
    Sleep(60)
    OP_94(0x0, 0xA, 0x0, 0x7D0, 0x1B58, 0x0)
    WaitChrThread(0x101, 0x1)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    Battle(0x421, 0x0, 0x1, 0x0, 0xFF)
    OP_31(0xFF, 0xF9, 0x0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_10CF"),
        (SWITCH_DEFAULT, "loc_10D4"),
    )


    label("loc_10CF")

    OP_B4(0x0)
    Jump("loc_10D4")

    label("loc_10D4")

    Return()

    # Function_3_433 end

    def Function_4_10D5(): pass

    label("Function_4_10D5")

    OP_8E(0xFE, 0xFFFF9002, 0x14, 0x105D6, 0x1388, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_4_10D5 end

    def Function_5_10F1(): pass

    label("Function_5_10F1")

    OP_8E(0xFE, 0xFFFF950C, 0x14, 0x109C8, 0x1388, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_5_10F1 end

    def Function_6_110D(): pass

    label("Function_6_110D")

    OP_8E(0xFE, 0xFFFF8A12, 0x14, 0x109FA, 0x1388, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_6_110D end

    def Function_7_1129(): pass

    label("Function_7_1129")

    OP_8C(0xFE, 0, 0)
    OP_8F(0xFE, 0xFFFF9002, 0x14, 0x103C4, 0x1388, 0x0)
    Return()

    # Function_7_1129 end

    def Function_8_1145(): pass

    label("Function_8_1145")

    OP_8C(0xFE, 0, 0)
    OP_8F(0xFE, 0xFFFF950C, 0x14, 0x107AC, 0x1388, 0x0)
    Return()

    # Function_8_1145 end

    def Function_9_1161(): pass

    label("Function_9_1161")

    OP_8C(0xFE, 0, 0)
    OP_8F(0xFE, 0xFFFF8A12, 0x14, 0x107AC, 0x1388, 0x0)
    Return()

    # Function_9_1161 end

    def Function_10_117D(): pass

    label("Function_10_117D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_44(0x101, 0x1)
    OP_44(0x101, 0x2)
    OP_44(0x8, 0x1)
    OP_44(0x9, 0x1)
    OP_44(0xA, 0x1)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, -32200, 0, 69470, 0)
    SetChrPos(0x9, -28040, 0, 65390, 0)
    SetChrPos(0xA, -24030, 0, 69690, 0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0x8, 15)
    SetChrSubChip(0x8, 3)
    SetChrChipByIndex(0x9, 15)
    SetChrSubChip(0x9, 1)
    SetChrChipByIndex(0xA, 15)
    SetChrSubChip(0xA, 7)
    ClearChrFlags(0x8, 0x1)
    ClearChrFlags(0x9, 0x1)
    ClearChrFlags(0xA, 0x1)
    Sleep(500)
    OP_D2(0x26022D, 0x260230, 0x0)
    SetChrPos(0x101, -27400, 20, 70790, 90)
    SetChrPos(0x109, -28810, 20, 68890, 180)
    SetChrPos(0xF8, -27120, 20, 69000, 135)
    SetChrPos(0xF9, -28990, 20, 70710, 270)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 16)
    SetChrChipByIndex(0x109, 42)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_12AE"),
        (5, "loc_12B6"),
        (3, "loc_12BE"),
        (4, "loc_12C6"),
        (6, "loc_12CE"),
        (7, "loc_12D6"),
        (SWITCH_DEFAULT, "loc_12DE"),
    )


    label("loc_12AE")

    SetChrChipByIndex(0xF8, 36)
    Jump("loc_12DE")

    label("loc_12B6")

    SetChrChipByIndex(0xF8, 37)
    Jump("loc_12DE")

    label("loc_12BE")

    SetChrChipByIndex(0xF8, 38)
    Jump("loc_12DE")

    label("loc_12C6")

    SetChrChipByIndex(0xF8, 39)
    Jump("loc_12DE")

    label("loc_12CE")

    SetChrChipByIndex(0xF8, 40)
    Jump("loc_12DE")

    label("loc_12D6")

    SetChrChipByIndex(0xF8, 41)
    Jump("loc_12DE")

    label("loc_12DE")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_12FF"),
        (5, "loc_1307"),
        (3, "loc_130F"),
        (4, "loc_1317"),
        (6, "loc_131F"),
        (7, "loc_1327"),
        (SWITCH_DEFAULT, "loc_132F"),
    )


    label("loc_12FF")

    SetChrChipByIndex(0xF9, 36)
    Jump("loc_132F")

    label("loc_1307")

    SetChrChipByIndex(0xF9, 37)
    Jump("loc_132F")

    label("loc_130F")

    SetChrChipByIndex(0xF9, 38)
    Jump("loc_132F")

    label("loc_1317")

    SetChrChipByIndex(0xF9, 39)
    Jump("loc_132F")

    label("loc_131F")

    SetChrChipByIndex(0xF9, 40)
    Jump("loc_132F")

    label("loc_1327")

    SetChrChipByIndex(0xF9, 41)
    Jump("loc_132F")

    label("loc_132F")

    OP_6D(-29090, 20, 70550, 0)
    OP_67(0, 6590, -10000, 0)
    OP_6B(2410, 0)
    OP_6C(315000, 0)
    OP_6E(323, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0x101,
        "#1022F#6P*pant* *pant*...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        "#1070F#6PGuh! That was tough...\x02",
    )

    CloseMessageWindow()
    OP_22(0x7B, 0x0, 0x64)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1461")

    label("loc_1423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144A")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1461")

    label("loc_144A")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1461")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1488")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14C6")

    label("loc_1488")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AF")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_14C6")

    label("loc_14AF")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_14C6")

    Sleep(500)
    OP_1D(0x5A)
    Sleep(500)

    def lambda_14D8():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14D8)
    Sleep(50)

    def lambda_14EB():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14EB)
    Sleep(50)

    def lambda_14FE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_14FE)
    Sleep(50)
    OP_8C(0xF8, 0, 400)
    Fade(500)
    SetMapFlags(0x10)
    OP_11(0x0, 0x0, 0x0, 0x6DC4, 0x927C, 0x0)
    SetChrChipByIndex(0xD, 27)
    SetChrSubChip(0xD, 0)
    SetChrFlags(0xD, 0x800)
    SetChrPos(0xD, -29000, 500, 85950, 180)
    SetChrPos(0xB, -28040, 500, 84990, 180)
    SetChrPos(0xC, -30050, 500, 84890, 180)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    OP_6D(-29070, 0, 77150, 0)
    OP_67(0, 4500, -10000, 0)
    OP_6B(3160, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)

    def lambda_15C0():
        OP_6D(-28990, 500, 84290, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15C0)
    WaitChrThread(0x101, 0x1)
    Sleep(500)

    ChrTalk(    #29
        0x101,
        "#1020F#5PAh...!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #30
        0xB,
        "Girl",
        "#4PHeehee...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #31
        0xC,
        "Young Man",
        "#3P...\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #32
        0xD,
        "Seated Man",
        (
            "#6PHa-ha! You were just a fraction too slow\x01",
            "in realizing the deception, I fear.\x02\x03",

            "I'm afraid this is check and mate.\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 0)
    SetChrSubChip(0xD, 0)
    Sleep(300)
    OP_22(0xBC, 0x0, 0x64)
    SetChrSubChip(0xD, 1)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0xD, 0x2)
    SetChrChipByIndex(0xD, 27)
    SetChrSubChip(0xD, 0)
    ClearChrFlags(0xD, 0x800)
    OP_8C(0x101, 0, 0)
    OP_8C(0x109, 0, 0)
    OP_8C(0xF8, 0, 0)
    OP_8C(0xF9, 0, 0)
    OP_6D(-28620, 20, 74760, 0)
    OP_67(0, 5020, -10000, 0)
    OP_6B(2260, 0)
    OP_6C(315000, 0)
    OP_6E(364, 0)
    OP_0D()
    OP_B0(0x7, 0x1E)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x1E)
    OP_22(0x130, 0x0, 0x64)
    OP_73(0x7)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #33
        0x101,
        "#1005F#5PWha--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1069F#5POh, hell!\x02",
    )

    CloseMessageWindow()

    def lambda_17EA():
        OP_6D(-28950, 20, 70480, 1500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_17EA)
    LoadEffect(0x1, "map\\mp089_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -28170, 0, 69720, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    OP_22(0x3C0, 0x0, 0x64)
    Sleep(2000)
    OP_11(0xFF, 0xFF, 0xFF, 0x0, 0x1D4C0, 0x0)
    SetMapFlags(0x10)
    StopSound(0x0, 0x7530, 0xFA0)
    SetChrSubChip(0x101, 0)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x101, 17)
    SetChrChipByIndex(0x109, 24)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_18AF"),
        (5, "loc_18B7"),
        (3, "loc_18BF"),
        (4, "loc_18C7"),
        (6, "loc_18CF"),
        (7, "loc_18D7"),
        (SWITCH_DEFAULT, "loc_18DF"),
    )


    label("loc_18AF")

    SetChrChipByIndex(0xF8, 18)
    Jump("loc_18DF")

    label("loc_18B7")

    SetChrChipByIndex(0xF8, 19)
    Jump("loc_18DF")

    label("loc_18BF")

    SetChrChipByIndex(0xF8, 20)
    Jump("loc_18DF")

    label("loc_18C7")

    SetChrChipByIndex(0xF8, 21)
    Jump("loc_18DF")

    label("loc_18CF")

    SetChrChipByIndex(0xF8, 22)
    Jump("loc_18DF")

    label("loc_18D7")

    SetChrChipByIndex(0xF8, 23)
    Jump("loc_18DF")

    label("loc_18DF")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1900"),
        (5, "loc_1908"),
        (3, "loc_1910"),
        (4, "loc_1918"),
        (6, "loc_1920"),
        (7, "loc_1928"),
        (SWITCH_DEFAULT, "loc_1930"),
    )


    label("loc_1900")

    SetChrChipByIndex(0xF9, 18)
    Jump("loc_1930")

    label("loc_1908")

    SetChrChipByIndex(0xF9, 19)
    Jump("loc_1930")

    label("loc_1910")

    SetChrChipByIndex(0xF9, 20)
    Jump("loc_1930")

    label("loc_1918")

    SetChrChipByIndex(0xF9, 21)
    Jump("loc_1930")

    label("loc_1920")

    SetChrChipByIndex(0xF9, 22)
    Jump("loc_1930")

    label("loc_1928")

    SetChrChipByIndex(0xF9, 23)
    Jump("loc_1930")

    label("loc_1930")


    ChrTalk(    #35
        0x101,
        "#1020F#6PAaah!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_196B")

    ChrTalk(    #36
        0x108,
        "#077FThis is...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A09")

    label("loc_196B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1992")

    ChrTalk(    #37
        0x106,
        "#057FThis is...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A09")

    label("loc_1992")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19B9")

    ChrTalk(    #38
        0x103,
        "#523FThis is...!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A09")

    label("loc_19B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19E1")

    ChrTalk(    #39
        0x107,
        "#065FIsn't this--\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A09")

    label("loc_19E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A09")

    ChrTalk(    #40
        0x105,
        "#541FIt can't be...!\x02",
    )

    CloseMessageWindow()

    label("loc_1A09")


    ChrTalk(    #41
        0x109,
        "#1070F#6PNnngh... Can't stay...awake...\x02",
    )

    CloseMessageWindow()

    def lambda_1A3C():
        OP_99(0x101, 0x0, 0x3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A3C)
    Sleep(200)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_1A56():
        OP_99(0x109, 0x0, 0x3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1A56)
    Sleep(150)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_1A70():
        OP_99(0xF8, 0x0, 0x3, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1A70)
    Sleep(230)
    OP_22(0x20C, 0x0, 0x64)

    def lambda_1A8A():
        OP_99(0xF9, 0x0, 0x3, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1A8A)
    Sleep(200)
    OP_22(0x20C, 0x0, 0x64)
    WaitChrThread(0xF9, 0x1)
    Sleep(2000)
    Fade(500)
    OP_6D(-29730, 0, 82210, 0)
    OP_67(0, 6670, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(224000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, -29400, 20, 70790, 0)
    SetChrPos(0x109, -30810, 20, 68890, 0)
    SetChrPos(0xF8, -29120, 20, 69000, 0)
    SetChrPos(0xF9, -30990, 20, 70710, 0)
    ClearMapFlags(0x10)
    OP_0D()
    Sleep(500)
    OP_82(0x0, 0x2)
    Fade(500)
    SetChrChipByIndex(0xD, 28)
    SetChrSubChip(0xD, 0)
    SetChrPos(0xD, -28900, 500, 85500, 180)
    OP_0D()
    Sleep(500)

    def lambda_1B68():
        OP_6D(-29110, 0, 78890, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B68)

    def lambda_1B80():
        OP_67(0, 5430, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1B80)
    SetChrFlags(0xD, 0x4)
    OP_8E(0xD, 0xFFFF8F58, 0x1F4, 0x14A28, 0x5DC, 0x0)
    ClearChrFlags(0xD, 0x4)

    def lambda_1BB6():
        OP_8E(0xFE, 0xFFFF8FDA, 0x0, 0x139B6, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1BB6)
    Sleep(500)

    def lambda_1BD6():
        OP_8E(0xFE, 0xFFFF94EE, 0x0, 0x13B1E, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1BD6)
    Sleep(100)

    def lambda_1BF6():
        OP_8E(0xFE, 0xFFFF8AA8, 0x0, 0x13CCC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1BF6)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0xD, 0x1)
    Sleep(500)

    ChrTalk(    #42
        0xD,
        (
            "#1154F#7PIt was a bit too easy a sport, really,\x01",
            "but at least your reactions were amusing.\x02\x03",

            "#1151FIt may be a small token of gratitude,\x01",
            "but...allow me to invite you to a place\x01",
            "I think you'll find very interesting.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x1388)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(5000)
    OP_6F(0x7, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0x101, 0x80)
    SetChrPos(0x109, -28500, 20, 68210, 0)
    SetChrPos(0xF8, -27250, 20, 70600, 315)
    SetChrPos(0xF9, -30300, 20, 70530, 45)
    SetChrFlags(0x109, 0x800)
    SetChrFlags(0xF8, 0x800)
    SetChrFlags(0xF9, 0x800)
    SetChrSubChip(0x109, 0)
    SetChrSubChip(0xF8, 0)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0x109, 35)
    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_END)),
        (2, "loc_1DB9"),
        (5, "loc_1DC1"),
        (3, "loc_1DC9"),
        (4, "loc_1DD1"),
        (6, "loc_1DD9"),
        (7, "loc_1DE1"),
        (SWITCH_DEFAULT, "loc_1DE9"),
    )


    label("loc_1DB9")

    SetChrChipByIndex(0xF8, 29)
    Jump("loc_1DE9")

    label("loc_1DC1")

    SetChrChipByIndex(0xF8, 30)
    Jump("loc_1DE9")

    label("loc_1DC9")

    SetChrChipByIndex(0xF8, 31)
    Jump("loc_1DE9")

    label("loc_1DD1")

    SetChrChipByIndex(0xF8, 32)
    Jump("loc_1DE9")

    label("loc_1DD9")

    SetChrChipByIndex(0xF8, 33)
    Jump("loc_1DE9")

    label("loc_1DE1")

    SetChrChipByIndex(0xF8, 34)
    Jump("loc_1DE9")

    label("loc_1DE9")

    Switch(
        (scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_END)),
        (2, "loc_1E0A"),
        (5, "loc_1E12"),
        (3, "loc_1E1A"),
        (4, "loc_1E22"),
        (6, "loc_1E2A"),
        (7, "loc_1E32"),
        (SWITCH_DEFAULT, "loc_1E3A"),
    )


    label("loc_1E0A")

    SetChrChipByIndex(0xF9, 29)
    Jump("loc_1E3A")

    label("loc_1E12")

    SetChrChipByIndex(0xF9, 30)
    Jump("loc_1E3A")

    label("loc_1E1A")

    SetChrChipByIndex(0xF9, 31)
    Jump("loc_1E3A")

    label("loc_1E22")

    SetChrChipByIndex(0xF9, 32)
    Jump("loc_1E3A")

    label("loc_1E2A")

    SetChrChipByIndex(0xF9, 33)
    Jump("loc_1E3A")

    label("loc_1E32")

    SetChrChipByIndex(0xF9, 34)
    Jump("loc_1E3A")

    label("loc_1E3A")

    OP_6D(-29040, 20, 70130, 0)
    OP_67(0, 6870, -10000, 0)
    OP_6B(2530, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    OP_9E(0x109, 0xF, 0x0, 0x12C, 0xBB8)
    Sleep(500)

    ChrTalk(    #43
        0x109,
        "#1070F#5PUhhhh...\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_1EC5():

        label("loc_1EC5")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1EC5")

    QueueWorkItem2(0x109, 3, lambda_1EC5)
    SetChrChipByIndex(0x109, 24)
    SetChrSubChip(0x109, 3)
    OP_0D()
    OP_99(0x109, 0x3, 0x0, 0x1F4)
    OP_44(0x109, 0x3)
    Fade(250)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x109, 65535)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F86")

    ChrTalk(    #44
        0x106,
        "#056FGhhh...\x02",
    )

    OP_9E(0x106, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_1F47():

        label("loc_1F47")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1F47")

    QueueWorkItem2(0x106, 3, lambda_1F47)
    SetChrChipByIndex(0x106, 19)
    SetChrSubChip(0x106, 3)
    OP_0D()
    OP_99(0x106, 0x3, 0x0, 0x1F4)
    OP_44(0x106, 0x3)
    Fade(250)
    SetChrSubChip(0x106, 0)
    SetChrChipByIndex(0x106, 65535)
    OP_0D()

    label("loc_1F86")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2007")

    ChrTalk(    #45
        0x103,
        "#522FNnn...\x02",
    )

    OP_9E(0x103, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_1FC8():

        label("loc_1FC8")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_1FC8")

    QueueWorkItem2(0x103, 3, lambda_1FC8)
    SetChrChipByIndex(0x103, 18)
    SetChrSubChip(0x103, 3)
    OP_0D()
    OP_99(0x103, 0x3, 0x0, 0x1F4)
    OP_44(0x103, 0x3)
    Fade(250)
    SetChrSubChip(0x103, 0)
    SetChrChipByIndex(0x103, 65535)
    OP_0D()

    label("loc_2007")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2088")

    ChrTalk(    #46
        0x108,
        "#572FMrh...\x02",
    )

    OP_9E(0x108, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_2049():

        label("loc_2049")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_2049")

    QueueWorkItem2(0x108, 3, lambda_2049)
    SetChrChipByIndex(0x108, 23)
    SetChrSubChip(0x108, 3)
    OP_0D()
    OP_99(0x108, 0x3, 0x0, 0x1F4)
    OP_44(0x108, 0x3)
    Fade(250)
    SetChrSubChip(0x108, 0)
    SetChrChipByIndex(0x108, 65535)
    OP_0D()

    label("loc_2088")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2109")

    ChrTalk(    #47
        0x105,
        "#049FNnn...\x02",
    )

    OP_9E(0x105, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_20CA():

        label("loc_20CA")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_20CA")

    QueueWorkItem2(0x105, 3, lambda_20CA)
    SetChrChipByIndex(0x105, 21)
    SetChrSubChip(0x105, 3)
    OP_0D()
    OP_99(0x105, 0x3, 0x0, 0x1F4)
    OP_44(0x105, 0x3)
    Fade(250)
    SetChrSubChip(0x105, 0)
    SetChrChipByIndex(0x105, 65535)
    OP_0D()

    label("loc_2109")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_218B")

    ChrTalk(    #48
        0x107,
        "#561FMmmm...\x02",
    )

    OP_9E(0x107, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_214C():

        label("loc_214C")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_214C")

    QueueWorkItem2(0x107, 3, lambda_214C)
    SetChrChipByIndex(0x107, 22)
    SetChrSubChip(0x107, 3)
    OP_0D()
    OP_99(0x107, 0x3, 0x0, 0x1F4)
    OP_44(0x107, 0x3)
    Fade(250)
    SetChrSubChip(0x107, 0)
    SetChrChipByIndex(0x107, 65535)
    OP_0D()

    label("loc_218B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_220B")

    ChrTalk(    #49
        0x104,
        "#039FGh...\x02",
    )

    OP_9E(0x104, 0xF, 0x0, 0x12C, 0xBB8)
    CloseMessageWindow()
    Sleep(200)
    Fade(500)

    def lambda_21CC():

        label("loc_21CC")

        OP_9E(0xFE, 0x1E, 0x0, 0x1388, 0x7D0)
        OP_48()
        Jump("loc_21CC")

    QueueWorkItem2(0x104, 3, lambda_21CC)
    SetChrChipByIndex(0x104, 20)
    SetChrSubChip(0x104, 3)
    OP_0D()
    OP_99(0x104, 0x3, 0x0, 0x1F4)
    OP_44(0x104, 0x3)
    Fade(250)
    SetChrSubChip(0x104, 0)
    SetChrChipByIndex(0x104, 65535)
    OP_0D()

    label("loc_220B")

    Sleep(500)
    ClearChrFlags(0x109, 0x800)
    ClearChrFlags(0xF8, 0x800)
    ClearChrFlags(0xF9, 0x800)

    def lambda_2225():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_2225)
    Sleep(100)
    OP_8C(0xF8, 270, 400)

    ChrTalk(    #50
        0x109,
        (
            "#1068F#1PTalk about walking right into\x01",
            "a snake pit...\x02\x03",

            "#1063FHey, Estelle, you all ri--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x51)
    Sleep(500)
    OP_62(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0x109, 90, 600)
    OP_8C(0x109, 180, 600)
    Sleep(500)
    OP_8C(0x109, 270, 600)
    Sleep(500)
    OP_8C(0x109, 180, 600)
    Fade(500)
    SetChrSubChip(0xF8, 0)
    SetChrChipByIndex(0xF8, 65535)
    SetChrSubChip(0xF9, 0)
    SetChrChipByIndex(0xF9, 65535)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_239A")
    TurnDirection(0x107, 0x109, 400)

    ChrTalk(    #51
        0x107,
        "#065FWhat's wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x109,
        (
            "#1069F#2PEstelle?!\x02\x03",

            "#1067FSomeone tell me this is a bad joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_25E3")

    label("loc_239A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2432")
    TurnDirection(0x105, 0x109, 400)

    ChrTalk(    #53
        0x105,
        "#043FIs something wrong...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x109,
        (
            "#1069F#2PEstelle?!\x02\x03",

            "#1067FSomeone tell me this is a bad joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_25E3")

    label("loc_2432")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24BF")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #55
        0x103,
        "#522FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x109,
        (
            "#1069F#2PEstelle?!\x02\x03",

            "#1067FSomeone tell me this is a bad joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_25E3")

    label("loc_24BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2551")
    TurnDirection(0x106, 0x109, 400)

    ChrTalk(    #57
        0x106,
        "#552FSomething up...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x109,
        (
            "#1069F#2PEstelle?!\x02\x03",

            "#1067FSomeone tell me this is a bad joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_25E3")

    label("loc_2551")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E3")
    TurnDirection(0x104, 0x109, 400)

    ChrTalk(    #59
        0x104,
        "#033FIs something amiss?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x109,
        (
            "#1069F#2PEstelle?!\x02\x03",

            "#1067FSomeone tell me this is a bad joke!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    label("loc_25E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2605")
    OP_62(0xF8, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2639")

    label("loc_2605")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2627")
    OP_62(0xF8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_2639")

    label("loc_2627")

    OP_62(0xF8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_2639")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265B")
    OP_62(0xF9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_268F")

    label("loc_265B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267D")
    OP_62(0xF9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Jump("loc_268F")

    label("loc_267D")

    OP_62(0xF9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    label("loc_268F")

    OP_43(0xF8, 0x0, 0x0, 0xB)
    OP_43(0xF9, 0x0, 0x0, 0xC)
    WaitChrThread(0xF8, 0x0)
    WaitChrThread(0xF9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2708")
    OP_62(0x108, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x108, 0, 500)
    OP_90(0x108, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)

    ChrTalk(    #61
        0x108,
        "#076F#6POver there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2891")

    label("loc_2708")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2764")
    OP_62(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x104, 0, 500)
    OP_90(0x104, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)

    ChrTalk(    #62
        0x104,
        "#530F#6PThere!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2891")

    label("loc_2764")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C5")
    OP_62(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x106, 0, 500)
    OP_90(0x106, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)

    ChrTalk(    #63
        0x106,
        "#054F#6POver there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2891")

    label("loc_27C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2826")
    OP_62(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x103, 0, 500)
    OP_90(0x103, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)

    ChrTalk(    #64
        0x103,
        "#024F#6POver there!\x02",
    )

    CloseMessageWindow()
    Jump("loc_2891")

    label("loc_2826")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2891")
    OP_62(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x105, 0, 500)
    OP_90(0x105, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)

    ChrTalk(    #65
        0x105,
        "#046F#6PThere's something there!\x02",
    )

    CloseMessageWindow()

    label("loc_2891")


    def lambda_2897():
        OP_6D(-33100, 0, 90600, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2897)

    def lambda_28AF():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_28AF)
    Sleep(50)

    def lambda_28C2():
        OP_8C(0xFE, 0, 500)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_28C2)
    Sleep(50)
    OP_8C(0x109, 0, 500)
    WaitChrThread(0x109, 0x1)
    Sleep(500)

    ChrTalk(    #66
        0x109,
        "#1063FDamn it...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C0F)
    Sleep(100)
    Fade(500)
    RemoveParty(0x0, 0xFF)
    SetChrPos(0x0, -29120, 0, 69960, 0)
    SetChrPos(0x1, -29120, 0, 69960, 0)
    SetChrPos(0x2, -29120, 0, 69960, 0)
    OP_69(0x0, 0x0)
    OP_6A(0x0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_D6(0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x0)
    SetMapFlags(0x2000000)
    Return()

    # Function_10_117D end

    def Function_11_2983(): pass

    label("Function_11_2983")

    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 180, 400)
    Sleep(500)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_11_2983 end

    def Function_12_29AF(): pass

    label("Function_12_29AF")

    OP_8C(0xFE, 0, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_12_29AF end

    def Function_13_29DB(): pass

    label("Function_13_29DB")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A0B")

    ChrTalk(    #67
        0x109,
        "#1063F(No, not this way!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2A0B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A3A")

    ChrTalk(    #68
        0x107,
        "#065F(N-No, not this way!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2A3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A6A")

    ChrTalk(    #69
        0x105,
        "#042F(No... The other way!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2A6A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A98")

    ChrTalk(    #70
        0x103,
        "#022F(No, the other way!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2A98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AC6")

    ChrTalk(    #71
        0x106,
        "#057F(Nah, not this way!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2AC6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AF3")

    ChrTalk(    #72
        0x104,
        "#032F(No... Over there!)\x02",
    )

    CloseMessageWindow()
    Jump("loc_2B1B")

    label("loc_2AF3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B1B")

    ChrTalk(    #73
        0x108,
        "#072F(No. Over there!)\x02",
    )

    CloseMessageWindow()

    label("loc_2B1B")

    OP_90(0x0, 0x0, 0x0, 0x5DC, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    Return()

    # Function_13_29DB end

    def Function_14_2B3C(): pass

    label("Function_14_2B3C")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BB8"),
        (1, "loc_2BBE"),
        (SWITCH_DEFAULT, "loc_2BC4"),
    )


    label("loc_2BB8")

    OP_A2(0x1200)
    Jump("loc_2BC4")

    label("loc_2BBE")

    OP_A2(0x1201)
    Jump("loc_2BC4")

    label("loc_2BC4")

    Return()

    # Function_14_2B3C end

    def Function_15_2BC5(): pass

    label("Function_15_2BC5")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_15_2BC5 end

    def Function_16_2C22(): pass

    label("Function_16_2C22")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C88")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #74
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_2E43")

    label("loc_2C88")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #75
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E28")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, -33630, 1000, 11690, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x32)
    OP_73(0x0)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -33630, 1000, 11690, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, -33630, 1000, 11690, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x0, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2E28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E42")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2E42")

    Return()

    label("loc_2E43")

    Return()

    # Function_16_2C22 end

    def Function_17_2E44(): pass

    label("Function_17_2E44")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A3(0x1C9E)
    OP_A2(0x1C9F)
    Return()

    # Function_17_2E44 end

    SaveToFile()

Try(main)
