from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4220   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4220.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Queen Alicia',                         # 9
        'Duke Dunan',                           # 10
        'Elnan',                                # 11
        'Prince Olivert',                       # 12
        'Major Vander',                         # 13
        'Princess Klaudia',                     # 14
        'Brig. General Bright',                 # 15
        'Captain Schwarz',                      # 16
        'Chancellor Osborne',                   # 17
        'Head Maid Hilda',                      # 18
        'Secretary Lechter',                    # 19
        'Royal Guardsman',                      # 20
        'Royal Guardsman',                      # 21
        'Royal Guardsman',                      # 22
        'Royal Guardsman',                      # 23
        'Royal Guardsman',                      # 24
        'Royal Guardsman',                      # 25
        'Royal Guardsman',                      # 26
        'Royal Guardsman',                      # 27
        'Royal Guardsman',                      # 28
        'Royal Guardsman',                      # 29
        'Royal Guardsman',                      # 30
        'Royal Guardsman',                      # 31
        'Target Camera',                        # 32
        'Queen Alicia',                         # 33
        'Prince Olivert',                       # 34
        'Major Vander',                         # 35
        'Princess Klaudia',                     # 36
        'Brig. General Bright',                 # 37
        'Chancellor Osborne',                   # 38
        'Secretary Lechter',                    # 39
        'Head Maid Hilda',                      # 40
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
        'ED6_DT07/CH02010 ._CH',             # 00
        'ED6_DT07/CH02140 ._CH',             # 01
        'ED6_DT07/CH02580 ._CH',             # 02
        'ED6_DT27/CH03260 ._CH',             # 03
        'ED6_DT27/CH03570 ._CH',             # 04
        'ED6_DT27/CH03960 ._CH',             # 05
        'ED6_DT27/CH03670 ._CH',             # 06
        'ED6_DT07/CH02090 ._CH',             # 07
        'ED6_DT27/CH03950 ._CH',             # 08
        'ED6_DT06/CH20129 ._CH',             # 09
        'ED6_DT07/CH01320 ._CH',             # 0A
        'ED6_DT07/CH02460 ._CH',             # 0B
        'ED6_DT26/CH20805 ._CH',             # 0C
        'ED6_DT26/CH20808 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT07/CH02010P._CP',             # 00
        'ED6_DT07/CH02140P._CP',             # 01
        'ED6_DT07/CH02580P._CP',             # 02
        'ED6_DT27/CH03260P._CP',             # 03
        'ED6_DT27/CH03570P._CP',             # 04
        'ED6_DT27/CH03960P._CP',             # 05
        'ED6_DT27/CH03670P._CP',             # 06
        'ED6_DT07/CH02090P._CP',             # 07
        'ED6_DT27/CH03950P._CP',             # 08
        'ED6_DT06/CH20129P._CP',             # 09
        'ED6_DT07/CH01320P._CP',             # 0A
        'ED6_DT07/CH02460P._CP',             # 0B
        'ED6_DT26/CH20805P._CP',             # 0C
        'ED6_DT26/CH20808P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x1C1,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_51A",          # 00, 0
        "Function_1_56B",          # 01, 1
        "Function_2_56C",          # 02, 2
        "Function_3_16D1",         # 03, 3
    )


    def Function_0_51A(): pass

    label("Function_0_51A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_542")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_542")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 2)

    label("loc_542")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_56A")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_56A")

    Return()

    # Function_0_51A end

    def Function_1_56B(): pass

    label("Function_1_56B")

    Return()

    # Function_1_56B end

    def Function_2_56C(): pass

    label("Function_2_56C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_C4(0x0, 0x20000000)
    Sleep(2000)
    OP_C4(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        (
            "\x07\x00Roughly two months after the crisis that struck \x01",
            "Liberl came to an end...\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x800)
    Sleep(800)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 500, 154350, 180)
    SetChrPos(0x10E, 0, 0, 149740, 0)
    OP_6D(200, 0, 133360, 0)
    OP_67(0, 6820, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(318, 0)

    def lambda_664():
        OP_6D(1660, 200, 153680, 6000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_664)

    def lambda_67C():
        OP_67(0, 4059, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_67C)

    def lambda_694():
        OP_6B(2800, 6000)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_694)

    def lambda_6A4():
        OP_6C(45000, 6000)
        ExitThread()

    QueueWorkItem(0x27, 3, lambda_6A4)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x27, 0x0)
    Sleep(500)

    NpcTalk(    #1
        0x10E,
        "Captain Schwarz",
        (
            "#178FThat concludes my report on all that transpired\x01",
            "here two months prior.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#094FI really cannot thank you enough for your above\x01",
            "and beyond efforts, Captain.\x02\x03",

            "#90FBringing an end to the chaos and restoring hope\x01",
            "to its people was no easy task. You should truly\x01",
            "be proud of yourself.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #3
        0x10E,
        "Captain Schwarz",
        (
            "#176FYour Majesty, please...\x02\x03",

            "#176FI have done nothing to deserve such praise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#090FI would beg to differ, and it's why I want to\x01",
            "thank you on behalf of every one of Liberl's\x01",
            "citizens.\x02\x03",

            "#090FNot only did you ensure our safety, you went \x01",
            "from place to place aiding in the restoration\x01",
            "as well.\x02\x03",

            "Now you continue to be just as busy serving as\x01",
            "the leader of the Royal Guard. You deserve all\x01",
            "the thanks you get.\x02\x03",

            "#090FI really am proud of you, Captain Schwarz.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #5
        0x10E,
        "Captain Schwarz",
        "#170FI am honored, Your Majesty!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#090FI believe I'll be able to formally present you with\x01",
            "at least one medal for your achievements at a\x01",
            "later date, too.\x02\x03",

            "#91FHaha. General Morgan seems to think a promotion\x01",
            "is almost assured as well. I'm looking forward to\x01",
            "seeing what the future holds in store for you.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #7
        0x10E,
        "Captain Schwarz",
        (
            "#172FB-But, Your Majesty...I must object.\x02\x03",

            "#178FThe only reason this crisis was resolved at all\x01",
            "was because of the efforts of countless people,\x01",
            "all of whom gave their all for Liberl's sake.\x02\x03",

            "My contribution was but a minor part of a much,\x01",
            "much greater whole.\x02\x03",

            "#175FI don't feel it would be appropriate for me to be\x01",
            "receiving medals or promotions...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#094F...Captain.\x02\x03",

            "I agree that countless people contributed to\x01",
            "achieving the peace that we now have.\x02\x03",

            "Everyone who fought, who tried to protect their\x01",
            "loved ones, and who endured the suffering they\x01",
            "faced contributed in some way. \x02\x03",

            "#090FBut I believe it's clear to everyone that without\x01",
            "the Arseille, the crisis would not have seen the\x01",
            "conclusion that it did.\x02\x03",

            "And the one who commanded the Arseille was\x01",
            "you.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #9
        0x10E,
        "Captain Schwarz",
        (
            "#175FB-Be that as it may...medals are one thing,\x01",
            "but I couldn't possibly consider accepting a\x01",
            "promotion...\x02\x03",

            "I feel as though I've barely spent all that much\x01",
            "time in my current position, so assuming one\x01",
            "with even greater responsibility would be...erm...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#090FHeehee. There's no need to be so modest.\x02\x03",

            "In my opinion, you've accomplished much more in\x01",
            "your current position than you seem to believe\x01",
            "you have.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10)
    Sleep(500)

    ChrTalk(    #11
        0x10,
        (
            "#094F...Actually...\x02\x03",

            "#090FCaptain, I'd like to propose that you take\x01",
            "the rest of today off. How would you feel\x01",
            "about that?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    NpcTalk(    #12
        0x10E,
        "Captain Schwarz",
        (
            "#173FMay I ask why, Your Majesty? I'm not sure\x01",
            "I quite understand...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "#090FAs I mentioned, I want to show my thanks to you \x01",
            "for all you did...and I believe there to be better\x01",
            "ways to do that than formal meetings like these. \x02\x03",

            "You certainly deserve some rest, too, given how\x01",
            "exhausting going back and forth between military\x01",
            "HQ and the castle practically every day must be.\x02\x03",

            "I've even been receiving requests from members\x01",
            "of the Royal Guard saying that they would like\x01",
            "for you to take a break as well.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10E, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    NpcTalk(    #14
        0x10E,
        "Captain Schwarz",
        (
            "#172FI-I'm terribly sorry that you had to listen to\x01",
            "such complaints, Your Majesty.\x02\x03",

            "It was certainly not my intent that you should\x01",
            "be troubled so...\x02\x03",

            "#176F(So who was it? Lux? Leon? It could easily be\x01",
            "both, knowing them...)\x02\x03",

            "(I'm used to them telling me as much every time\x01",
            "they see me, but I cannot believe they chose to\x01",
            "bother Her Majesty with the issue!)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#090FAs such, I would like for you to take the remainder\x01",
            "of the day and use it to relax.\x02\x03",

            "That way, you can return to your duties tomorrow\x01",
            "feeling refreshed and ready to work for the good\x01",
            "of this nation anew.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #16
        0x10E,
        "Captain Schwarz",
        (
            "#172FV-Very well...\x02\x03",

            "#176FIf that is your wish, Your Majesty.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(500)
    OP_6D(200500, 0, 149240, 0)
    OP_67(0, 4960, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(135000, 0)
    OP_6E(280, 0)
    SetChrPos(0x10, 200000, 500, 154350, 180)
    SetChrPos(0x10E, 200000, 0, 149740, 0)
    OP_0D()
    Sleep(100)

    def lambda_15E8():
        OP_6B(2700, 400)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_15E8)
    SetChrChipByIndex(0x10E, 9)
    SetChrSubChip(0x10E, 0)
    OP_99(0x10E, 0x0, 0x1, 0x5DC)
    Sleep(600)

    NpcTalk(    #17
        0x10E,
        "Captain Schwarz",
        (
            "#170F#5PI, Captain Julia Schwarz of the Royal Guard,\x01",
            "accept your proposal and shall take leave of\x01",
            "my duties for the remainder of the day.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_16AF():
        OP_6B(2900, 3000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_16AF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_56C end

    def Function_3_16D1(): pass

    label("Function_3_16D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x10, 0, 500, 154350, 180)
    SetChrPos(0x15, -1400, 500, 154070, 180)
    SetChrPos(0x16, 1090, 500, 152800, 180)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x13, -200, 0, 148930, 0)
    SetChrPos(0x14, 630, 0, 147940, 0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x1B, 2200, 0, 142260, 270)
    SetChrPos(0x1C, 2200, 0, 140760, 270)
    SetChrPos(0x1D, 2200, 0, 139260, 270)
    SetChrPos(0x1E, 3300, 0, 142260, 270)
    SetChrPos(0x1F, 3300, 0, 140760, 270)
    SetChrPos(0x20, 3300, 0, 139260, 270)
    SetChrPos(0x21, -2200, 0, 142260, 90)
    SetChrPos(0x22, -2200, 0, 140760, 90)
    SetChrPos(0x23, -2200, 0, 139260, 90)
    SetChrPos(0x24, -3300, 0, 142260, 90)
    SetChrPos(0x25, -3300, 0, 140760, 90)
    SetChrPos(0x26, -3300, 0, 139260, 90)
    OP_6D(1940, 0, 136940, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)

    def lambda_18AA():
        OP_6D(1940, 0, 153520, 6000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_18AA)

    def lambda_18C2():
        OP_67(0, 5140, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_18C2)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x27, 0x0)
    Sleep(500)
    Fade(1000)
    OP_6D(1410, 250, 152950, 0)
    OP_67(0, 4070, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(317, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #18
        0x13,
        (
            "#1545F#12PYour Majesty, Your Highness, I humbly thank you\x01",
            "both for your generous hospitality during my stay\x01",
            "in your fine kingdom.\x02\x03",

            "#1540FYou were even gracious enough to humor my\x01",
            "brazen request of escorting me back to Heimdallr\x01",
            "aboard the Arseille.\x02\x03",

            "#1541FThis debt I owe you will be repaid many times over\x01",
            "in the future. Rest assured of that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#091F#5PHaha. Oh, you needn't think of this as anything\x01",
            "we went out of our way for.\x02\x03",

            "#090FEscorting an honored state guest back home is\x01",
            "a matter of course.\x02\x03",

            "Particularly a guest to whom we owe a great debt\x01",
            "of gratitude.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x15,
        (
            "#1818F#5PIf you ever have the opportunity, please do come\x01",
            "back to Liberl again in the future.\x02\x03",

            "I imagine Estelle and Joshua will be back by then,\x01",
            "too.\x02\x03",

            "So we'll all be able to give you a nice, warm \x01",
            "welcome.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x13,
        (
            "#1541F#12PHaha. I'm already excited for my next visit.\x02\x03",

            "#1540FHave they left the country yet, by the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x16,
        (
            "#1125F#5PThey're busy getting ready to leave over\x01",
            "in Rolent at the moment, I believe.\x02\x03",

            "#1120FI'm planning to see them off when the time\x01",
            "comes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x13,
        (
            "#1545F#12PI see...\x02\x03",

            "#1540FIncidentally, while the ruins of Hamel are\x01",
            "currently sealed off, I'll do what I can on\x01",
            "my end to ensure they are allowed inside.\x02\x03",

            "Could I trouble you to pass that along to\x01",
            "them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x16,
        (
            "#1125F#5PCertainly.\x02\x03",

            "Thank you very much, Your Highness.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x13,
        (
            "#1541F#12POh, think nothing of it. It's the least I could\x01",
            "do after all they've done for me.\x02\x03",

            "#1540FI owe you a great deal, too, Cassius.\x02\x03",

            "If not for your assistance, stopping that\x01",
            "armored division from crossing into Liberl\x01",
            "wouldn't have been as simple as it was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x16,
        (
            "#1120F#5PHaha... I could say the same to you.\x02\x03",

            "#1125FStill, as I'm sure you're aware, that outcome will\x01",
            "have been well within the realm of possibility for\x01",
            "the chancellor.\x02\x03",

            "#1122FI doubt he was even surprised by the incident.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x13,
        "#1545F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x15,
        "#1814F#5P...Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#093F#5PMost likely not...\x02\x03",

            "#094FErebonia had nothing anything to gain from\x01",
            "using that situation to occupy Liberl.\x02\x03",

            "Certainly not to the extent that it would be\x01",
            "worth going out of their way to develop \x01",
            "inefficient steam tanks.\x02\x03",

            "#092FThe only reason I can see for him doing what\x01",
            "he did...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x13,
        (
            "#1551F#12P...was as a show of power to surrounding\x01",
            "nations. A statement that even without orbal\x01",
            "power, Erebonia's army could still act.\x02\x03",

            "#1542FI indeed suspect that was his true aim all along.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #31
        0x15,
        "#1813F#5PGoodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x16,
        (
            "#1125F#5PSo you did notice.\x02\x03",

            "#1122FThe Orbal Shutdown Phenomenon was a complete\x01",
            "unknown to the rest of the continent.\x02\x03",

            "Perhaps it might never occur again--but there's\x01",
            "always the chance it might, whether it's here or\x01",
            "somewhere else entirely.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x14,
        (
            "#272F#11PI hear the Empire only built a relatively small\x01",
            "number of those tanks in all, too. Certainly not\x01",
            "enough to launch a full-scale invasion.\x02\x03",

            "#276FBy the sounds of it, they were just put together \x01",
            "in Reinford's factories using parts intended for\x01",
            "standard orbal tanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x13,
        (
            "#1545F#12PBut as it stands, the knowhow to put together\x01",
            "tanks like that only exists in the Empire.\x02\x03",

            "And in these unpredictable times, no other nation\x01",
            "has the time or resources to try and develop\x01",
            "extremely inefficient steam-powered weaponry.\x02\x03",

            "#1540FIn a sense, because of what just happened,\x01",
            "the Imperial Army's effect as a deterrent is even\x01",
            "greater than ever.\x02\x03",

            "#1541FHe's using war as a diplomatic tool...and very\x01",
            "effectively at that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x15,
        (
            "#1813F#5PNone of this had even occurred to me...\x02\x03",

            "#1819FI have a long way to go before I'm fit to be\x01",
            "the ruler of this country...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x13,
        (
            "#1544F#12PDon't beat yourself up too much about it. He's no\x01",
            "ordinary foe to even the most hardened veterans.\x02\x03",

            "#1542FThe chancellor always seems to be thinking several\x01",
            "steps ahead of the rest of the world. It's impressive,\x01",
            "no matter what we may think of his actual ideas.\x02\x03",

            "#1541FHeh. I'm quite the reckless fool to be trying to\x01",
            "challenge him, if I do say so myself.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x15,
        "#1872F#5PDon't be silly, Your Highness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x14,
        (
            "#274F#11PHow you can say that with a smile on your face is\x01",
            "utterly beyond me...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10,
        (
            "#094F#5PYou should focus on building yourself a strong\x01",
            "foothold to begin with.\x02\x03",

            "#090FI do hope you'll be careful.\x02\x03",

            "No matter what may occur, be sure not to\x01",
            "lose sight of exactly where you stand.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x13,
        (
            "#1545F#12P...Of course, Your Majesty.\x02\x03",

            "#1540FIf I were to go and bring shame upon myself now,\x01",
            "I'd be wasting all the effort involved in escorting\x01",
            "me back home.\x02\x03",

            "I'll be sure to take what you have said to heart.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -500, 0, 138900, 0)

    NpcTalk(    #41
        0x19,
        "Woman's Voice",
        "#1PE-Excuse me, Your Majesty!\x02",
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_2B58():

        label("loc_2B58")

        TurnDirection(0xFE, 0x19, 500)
        OP_48()
        Jump("loc_2B58")

    QueueWorkItem2(0x13, 2, lambda_2B58)
    Sleep(50)

    def lambda_2B6E():

        label("loc_2B6E")

        TurnDirection(0xFE, 0x19, 500)
        OP_48()
        Jump("loc_2B6E")

    QueueWorkItem2(0x14, 2, lambda_2B6E)

    def lambda_2B7F():
        OP_6D(1510, 250, 152250, 2500)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_2B7F)

    def lambda_2B97():
        OP_67(0, 3740, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_2B97)

    def lambda_2BAF():
        OP_6B(3000, 2500)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_2BAF)

    def lambda_2BBF():
        OP_8E(0xFE, 0xFFFFFE0C, 0x0, 0x23E9C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2BBF)
    WaitChrThread(0x19, 0x1)
    OP_44(0x13, 0x2)
    OP_44(0x14, 0x2)
    Sleep(500)

    ChrTalk(    #42
        0x15,
        "#1814F#5PHilda...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x10,
        (
            "#097F#5PWhatever is the matter?\x02\x03",

            "It's not often I see you so flustered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x19,
        (
            "#716F#12PMy apologies, Your Majesty. It's just that a guest\x01",
            "for you arrived all of a sudden at the castle...\x02\x03",

            "#714FOrdinarily, I would not have rushed in while you \x01",
            "were meeting with others, but the visitor is so \x01",
            "irregular that I thought you should know at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#093F#5PIrregular? How so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x13,
        (
            "#1540F#5PHmm... It sounds like it's about time\x01",
            "I take my leave, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x19,
        (
            "#716FActually...\x02\x03",

            "#714F...the visitor said he would like to greet\x01",
            "you as well, and not just Her Majesty.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #48
        0x14,
        "#273F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x13,
        (
            "#1543F#5P...\x02\x03",

            "#1542FHilda. Just who is this visitor?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x19,
        (
            "#713F#12PWell...\x02\x03",

            "#710F...he introduced himself as Chancellor Giliath\x01",
            "Osborne of the Erebonian Empire.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x2B, 0x80)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x2F, 0x80)
    SetChrPos(0x28, 0, 500, 154350, 180)
    SetChrPos(0x2B, -1400, 500, 154070, 180)
    SetChrPos(0x2C, 201090, 500, 152800, 180)
    SetChrPos(0x29, 2140, 0, 149660, 225)
    SetChrPos(0x2A, 3000, 0, 148560, 225)
    SetChrPos(0x2F, -3380, 0, 148560, 135)
    SetChrPos(0x10, 200000, 500, 154350, 180)
    SetChrPos(0x15, 198600, 500, 154070, 180)
    SetChrPos(0x16, 201090, 500, 152800, 180)
    SetChrPos(0x19, 196620, 0, 150160, 135)
    SetChrPos(0x13, 202140, 0, 149660, 225)
    SetChrPos(0x14, 203000, 0, 148560, 225)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x18, 200000, 0, 126680, 0)
    SetChrPos(0x1A, 199200, 0, 126680, 0)
    OP_9F(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    SetChrPos(0x2D, 0, 0, 126680, 0)
    SetChrPos(0x2E, -800, 0, 126680, 0)
    OP_9F(0x2D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(0, 0, 137500, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3220, 0)
    OP_6C(45000, 0)
    OP_6E(338, 0)
    OP_6D(1940, 0, 136940, 0)
    OP_67(0, 3640, -10000, 0)
    OP_6B(3660, 0)
    OP_6C(45000, 0)
    OP_6E(366, 0)
    OP_1D(0x74)
    Sleep(500)
    FadeToBright(1000, 0)

    def lambda_3131():
        OP_6D(1940, 0, 153520, 8000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_3131)

    def lambda_3149():
        OP_67(0, 5140, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_3149)

    def lambda_3161():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_3161)

    def lambda_3173():
        OP_8E(0xFE, 0x30D40, 0x0, 0x2394C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3173)

    def lambda_318E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_318E)

    def lambda_31A0():
        OP_8E(0xFE, 0x0, 0x0, 0x2394C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_31A0)
    Sleep(500)

    def lambda_31C0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_31C0)

    def lambda_31D2():
        OP_8E(0xFE, 0x30A20, 0x0, 0x2317C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_31D2)

    def lambda_31ED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_31ED)

    def lambda_31FF():
        OP_8E(0xFE, 0xFFFFFCE0, 0x0, 0x2317C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_31FF)
    Sleep(5000)
    Fade(500)
    OP_44(0x27, 0xFF)
    OP_6D(200060, 0, 142400, 0)
    OP_67(0, 4920, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(180000, 0)
    OP_6E(280, 0)

    def lambda_3265():
        OP_8E(0xFE, 0x30D40, 0x0, 0x2394C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3265)

    def lambda_3280():
        OP_8E(0xFE, 0x30A20, 0x0, 0x2317C, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3280)
    SetChrPos(0x1B, 202200, 0, 142260, 270)
    SetChrPos(0x1C, 202200, 0, 140760, 270)
    SetChrPos(0x1D, 202200, 0, 139260, 270)
    SetChrPos(0x1E, 203300, 0, 142260, 270)
    SetChrPos(0x1F, 203300, 0, 140760, 270)
    SetChrPos(0x20, 203300, 0, 139260, 270)
    SetChrPos(0x21, 197800, 0, 142260, 90)
    SetChrPos(0x22, 197800, 0, 140760, 90)
    SetChrPos(0x23, 197800, 0, 139260, 90)
    SetChrPos(0x24, 196700, 0, 142260, 90)
    SetChrPos(0x25, 196700, 0, 140760, 90)
    SetChrPos(0x26, 196700, 0, 139260, 90)

    def lambda_3367():
        OP_6D(200060, 0, 145750, 2000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_3367)

    def lambda_337F():
        OP_67(0, 3810, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_337F)
    WaitChrThread(0x27, 0x0)
    WaitChrThread(0x18, 0x1)
    Sleep(500)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x200, 0x5A, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x200, 0xFFFFFF, 0x0, "C_VIS354._CH")
    OP_C6(0x0, 0x0, 140000, 0, 500)
    OP_C6(0x0, 0x3, -1, 500, 0)
    Sleep(1000)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("Chancellor Osborne")

    AnonymousTalk(    #51
        (
            "Ahh, it's an honor to be granted a personal audience.\x02\x03",

            "I am Giliath Osborne, representative of the Imperial government.\x02\x03",

            "My apologies for the abrupt intrusion.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_C6(0x0, 0x3, 16777215, 250, 0)
    OP_C7(0x0, 0x0, 0x3)
    OP_C7(0x1, 0xFF, 0x0)
    Sleep(500)

    ChrTalk(    #52
        0x10,
        "#097F#6PSo you are Chancellor Osborne...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x15,
        "#1814F#4P...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 45, 400)
    Sleep(300)

    ChrTalk(    #54
        0x18,
        (
            "#1485F#11PAnd it's a pleasure to see you again as well,\x01",
            "Your Highness.\x02\x03",

            "#1480FIt's been a year since we last met, has it not?\x01",
            "I hope these passing months have seen you well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x13,
        (
            "#1545F#6P...Yes, a year sounds about right.\x02\x03",

            "#1542FStill, while I hope you'll forgive me for asking...\x02\x03",

            "...just what did prompt someone of your stature\x01",
            "to appear at the castle without warning?\x02\x03",

            "I'd very much like to hear your side of the story.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x18,
        (
            "#1483F#11PMy apologies, Your Highness.\x02\x03",

            "#1485FYou see, these past few days, I've been touring\x01",
            "eastern Erebonia on routine inspections.\x02\x03",

            "#1480FIt's been going very smoothly--more so than I had\x01",
            "initially anticipated. I had enough free time in my\x01",
            "schedule to pay a cordial visit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x13,
        "#1543F#6POh, my... Is that so?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x18,
        (
            "#1485F#11PNaturally, I would have preferred to come here\x01",
            "while the crisis was still unfolding like you yourself\x01",
            "did, Your Highness...\x02\x03",

            "Unfortunately, the confusion in southern Erebonia\x01",
            "was simply too pressing a matter, and I had no\x01",
            "choice but to deal with that first.\x02\x03",

            "#1480FThis was the first chance that presented itself to\x01",
            "come here and meet directly with Her Majesty, so\x01",
            "I acted with the utmost expediency.\x02\x03",

            "I hope you'll forgive my lack of proper decorum in\x01",
            "failing to give advance notice of my arrival.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x13,
        (
            "#1545F#6P...That does make sense, at least.\x02\x03",

            "#1540FRegardless, please don't concern yourself with me.\x01",
            "No doubt you wish to offer your greetings to Her\x01",
            "Majesty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x18,
        "#1485F#11PMy thanks, Your Highness. \x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_8C(0x18, 0, 400)
    Sleep(300)

    def lambda_3AEC():
        OP_6D(201240, 100, 149300, 2000)
        ExitThread()

    QueueWorkItem(0x27, 0, lambda_3AEC)

    def lambda_3B04():
        OP_67(0, 4920, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_3B04)

    def lambda_3B1C():
        OP_6C(142000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_3B1C)

    def lambda_3B2C():
        OP_6B(3000, 2000)
        ExitThread()

    QueueWorkItem(0x27, 3, lambda_3B2C)

    def lambda_3B3C():

        label("loc_3B3C")

        TurnDirection(0xFE, 0x18, 400)
        OP_48()
        Jump("loc_3B3C")

    QueueWorkItem2(0x14, 2, lambda_3B3C)

    def lambda_3B4D():
        OP_8E(0xFE, 0x30D40, 0x0, 0x247FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3B4D)
    Sleep(200)

    def lambda_3B6D():
        OP_8E(0xFE, 0x30868, 0x0, 0x24540, 0x8FC, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3B6D)
    Sleep(400)

    def lambda_3B8D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_3B8D)
    Sleep(100)

    def lambda_3BA0():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3BA0)
    WaitChrThread(0x18, 0x1)
    WaitChrThread(0x1A, 0x1)
    Sleep(500)
    Fade(100)
    SetChrChipByIndex(0x18, 13)
    SetChrSubChip(0x18, 0)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x18, 0x0, 0x5, 0x3E8)
    Sleep(500)

    ChrTalk(    #61
        0x18,
        (
            "#1485F#11PWell, then...\x02\x03",

            "Allow me to extend my most heartfelt greetings to\x01",
            "both of you, Queen Alicia and Princess Klaudia.\x02\x03",

            "#1482FIt's abundantly clear that the crisis that unfolded\x01",
            "here has been quite the ordeal for yourselves and\x01",
            "for your nation's people.\x02\x03",

            "#1484FYou have my deepest sympathies for the hardships \x01",
            "you have endured, as well as my commendation for \x01",
            "bringing the situation under control.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x15,
        (
            "#1813F#6PI...\x02\x03",

            "#1815FI thank you for your kind words, Your Excellency.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10,
        (
            "#094F#6PIf anything, we should be apologizing to you for\x01",
            "the fact that the southern side of your nation was\x01",
            "caught up in what should have been our problem.\x02\x03",

            "We should be the ones going to you, rather than\x01",
            "having you trouble yourself to come all the way\x01",
            "to Liberl.\x02\x03",

            "#090FI beg you to accept our apologies together with\x01",
            "my deepest thanks for coming here today.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(250)
    OP_99(0x18, 0x6, 0x7, 0x3E8)
    SetChrChipByIndex(0x18, 8)
    SetChrSubChip(0x18, 0)
    Sleep(500)

    ChrTalk(    #64
        0x18,
        (
            "#1480F#11PI would never ask for apologies; I've heard what\x01",
            "happened was the work of a shadowy organization\x01",
            "stirring up trouble within your borders.\x02\x03",

            "While I meant well by sending a military force\x01",
            "to aid you, I wouldn't have done something so\x01",
            "careless had I known the truth of the matter.\x02\x03",

            "#1485FMy actions were rash. Foolish, even, and I was\x01",
            "rightfully reprimanded by His Imperial Majesty\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x10,
        "#097F#6POh, my... \x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x18,
        (
            "#1480F#11PFortunately, His Highness the Prince was able\x01",
            "to act with all due haste to put right my\x01",
            "misstep before even greater harm was done...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 90, 400)
    Sleep(500)

    ChrTalk(    #67
        0x18,
        (
            "#1485F#12PI owe you a great debt of gratitude for that,\x01",
            "Your Highness.\x02\x03",

            "#1480FAnd congratulations besides, for your part in\x01",
            "bringing an end to the crisis.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x13,
        (
            "#1545F#5POh, I did nothing out of the ordinary.\x02\x03",

            "#1540FI had a lot of help from Her Majesty,\x01",
            "Her Highness, and Brigadier General\x01",
            "Bright here, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x18, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_8C(0x18, 0, 400)
    Sleep(300)

    ChrTalk(    #69
        0x18,
        "#1483F#11PBright, you say?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x16,
        (
            "#1125F#6P...It's a pleasure to meet you, Your Excellency.\x02\x03",

            "#1120FI am Cassius Bright, a brigadier general in the\x01",
            "Liberlian Royal Army.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x18,
        (
            "#1485F#11PHaha. The pleasure is all mine, I assure you.\x02\x03",

            "#1480FYour name is rather well known even in the\x01",
            "Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x16,
        (
            "#1120F#6PNot as much as yours is known here in Liberl,\x01",
            "I would imagine. It's an honor to be able to\x01",
            "speak with you in person.\x02\x03",

            "#1123FIt's certainly a surprise to be able to, though.\x01",
            "Coming here on a whim can't have been easy\x01",
            "for a man as busy as yourself.\x02\x03",

            "#1122FIt sounds as though I may have underestimated\x01",
            "just how capable you truly are.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x18,
        (
            "#1485F#11PNot at all. I was greatly impressed to see the\x01",
            "Royal Army's effectiveness in dealing with the\x01",
            "tumult here.\x02\x03",

            "Your forces have proven powerful yet flexible,\x01",
            "capable of dealing with emergencies ably and\x01",
            "decisively.\x02\x03",

            "#1481FI might go so far as to say it embodies an ideal\x01",
            "that the Imperial Army, with its swollen ranks,\x01",
            "could never hope to realize.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x16,
        (
            "#1125F#6PYou flatter us, Your Excellency.\x02\x03",

            "#1120FFor your part, I hear you were responsible for\x01",
            "the establishment of the Imperial Army's famed \x01",
            "Intelligence Division.\x02\x03",

            "Our army is in desperate need of a new one of\x01",
            "its own, so I find myself quite envious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x18,
        (
            "#1486F#11PHaha... It almost sounds as though the two\x01",
            "of us each want what the other has.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x16,
        "#1121F#6PHaha. So it does!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        (
            "#1551F#5P...May I ask, Your Excellency, what will you be\x01",
            "doing now?\x02\x03",

            "#1540FFor my part, I'm intending to leave Liberl today,\x01",
            "so I'm afraid I won't be around much longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x18, 90, 400)
    Sleep(300)

    ChrTalk(    #78
        0x18,
        (
            "#1485F#12PYes, so I've been told.\x02\x03",

            "#1480FI believe you're intending to make your grand\x01",
            "arrival in Heimdallr aboard the famous Arseille?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x13,
        "#1542F#5PI'm impressed you're already aware.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x18,
        (
            "#1485F#12PI almost wish I could return to Erebonia on\x01",
            "board it alongside you...\x02\x03",

            "#1480F...but alas, I'm afraid I have other business\x01",
            "demanding my attention after I'm finished here.\x02\x03",

            "I'll be leaving Liberl separately this afternoon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x10,
        (
            "#097F#6PThat is a shame... I would very much have liked\x01",
            "to invite you to this evening's banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x18,
        (
            "#1486F#12PPlease, you need not go to such troubles on my\x01",
            "account.\x02\x03",

            "I feel as though I've put you out enough showing\x01",
            "up unannounced as I did, to say nothing of dining\x01",
            "with such esteemed company.\x02\x03",

            "#1485FStill, I do have some time before the airship I'll be\x01",
            "leaving on is due to depart...\x02\x03",

            "That being the case, might I ask for a little of\x01",
            "your time, Your Highness?\x02\x03",

            "#1481FI have a few things I'd like to discuss with you\x01",
            "personally.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        "#270F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x1A,
        "#1885F#11P...Heh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x15,
        "#1813F#6P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x13)
    Sleep(500)

    ChrTalk(    #86
        0x13,
        (
            "#1545F#5PVery well.\x02\x03",

            "#1540FI have some matters I would actually like to\x01",
            "discuss personally with you as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x18,
        "#1485F#12PWhat a fortuitous coincidence.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x10,
        (
            "#094F#6PAllow me to have a room arranged for the two\x01",
            "of you to have your discussion, then.\x02\x03",

            "#090FHilda, if you would?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x19,
        "#713F#12PCertainly, Your Majesty.\x02",
    )

    CloseMessageWindow()

    def lambda_4E7A():
        OP_6B(3500, 3000)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_4E7A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xFA0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4221   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_16D1 end

    SaveToFile()

Try(main)
