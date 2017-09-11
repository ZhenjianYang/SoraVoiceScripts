from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4260   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4260.x',
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
        'Captain Amalthea',                     # 9
        '2nd Lieutenant Lorence',               # 10
        'Special Ops Soldier',                  # 11
        'Special Ops Soldier',                  # 12
        'Special Ops Soldier',                  # 13
        'Special Ops Soldier',                  # 14
        'Special Ops Soldier',                  # 15
        'Special Ops Soldier',                  # 16
        'Special Ops Soldier',                  # 17
        'Special Ops Soldier',                  # 18
        'Special Ops Soldier',                  # 19
        'Special Ops Soldier',                  # 20
        'Special Ops Soldier',                  # 21
        'Special Ops Soldier',                  # 22
        'Cassius',                              # 23
        'General Morgan',                       # 24
        'Queen Alicia',                         # 25
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
        'ED6_DT07/CH02460 ._CH',             # 00
        'ED6_DT07/CH02230 ._CH',             # 01
        'ED6_DT07/CH02240 ._CH',             # 02
        'ED6_DT07/CH02100 ._CH',             # 03
        'ED6_DT07/CH02200 ._CH',             # 04
        'ED6_DT07/CH01610 ._CH',             # 05
        'ED6_DT07/CH02000 ._CH',             # 06
        'ED6_DT07/CH02080 ._CH',             # 07
        'ED6_DT07/CH02010 ._CH',             # 08
    )

    AddCharChipPat(
        'ED6_DT07/CH02460P._CP',             # 00
        'ED6_DT07/CH02230P._CP',             # 01
        'ED6_DT07/CH02240P._CP',             # 02
        'ED6_DT07/CH02100P._CP',             # 03
        'ED6_DT07/CH02200P._CP',             # 04
        'ED6_DT07/CH01610P._CP',             # 05
        'ED6_DT07/CH02000P._CP',             # 06
        'ED6_DT07/CH02080P._CP',             # 07
        'ED6_DT07/CH02010P._CP',             # 08
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    ScpFunction(
        "Function_0_312",          # 00, 0
        "Function_1_3CF",          # 01, 1
        "Function_2_3F2",          # 02, 2
        "Function_3_408",          # 03, 3
        "Function_4_541",          # 04, 4
        "Function_5_69C",          # 05, 5
        "Function_6_93C",          # 06, 6
        "Function_7_113A",         # 07, 7
        "Function_8_1156",         # 08, 8
    )


    def Function_0_312(): pass

    label("Function_0_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_329")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x3FA)
    Event(0, 6)

    label("loc_329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_353")
    SetChrChipByIndex(0x0, 0)
    SetChrChipByIndex(0x1, 1)
    SetChrChipByIndex(0x138, 2)
    SetChrFlags(0x0, 0x1000)
    SetChrFlags(0x1, 0x1000)
    SetChrFlags(0x138, 0x1000)

    label("loc_353")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 7)), scpexpr(EXPR_END)), "loc_35D")
    Jump("loc_3CE")

    label("loc_35D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 3)), scpexpr(EXPR_END)), "loc_3A9")
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, 60, 500, 154950, 168)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x16, 60, 0, 150270, 7)
    SetChrPos(0x17, -800, 0, 149980, 356)
    Jump("loc_3CE")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 6)), scpexpr(EXPR_END)), "loc_3B3")
    Jump("loc_3CE")

    label("loc_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_3BD")
    Jump("loc_3CE")

    label("loc_3BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_END)), "loc_3C7")
    Jump("loc_3CE")

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC7, 1)), scpexpr(EXPR_END)), "loc_3CE")

    label("loc_3CE")

    Return()

    # Function_0_312 end

    def Function_1_3CF(): pass

    label("Function_1_3CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 4)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1), scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x54), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E8")

    OP_4F(0x2B, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_3CF end

    def Function_2_3F2(): pass

    label("Function_2_3F2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_407")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_3F2")

    label("loc_407")

    Return()

    # Function_2_3F2 end

    def Function_3_408(): pass

    label("Function_3_408")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0x18,
        (
            "#090FIt pains me to request that you return\x01",
            "to service after closing that chapter\x01",
            "of your life, Cassius...\x02\x03",

            "But, gentle though you be, I know\x01",
            "you have an iron will. And I know\x01",
            "you will do what you must.\x02\x03",

            "My sincerest apologies to you, but\x01",
            "I ask if you could lend me your\x01",
            "father's strength for a time.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_408 end

    def Function_4_541(): pass

    label("Function_4_541")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #1
        0x16,
        (
            "#080FI have some important matters\x01",
            "to discuss at the moment.\x02\x03",

            "You two go and enjoy the festivities\x01",
            "without me, if you would.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_698")

    label("loc_5D0")

    OP_A2(0x0)

    ChrTalk(    #2
        0x16,
        (
            "#080FThe town square must be alight\x01",
            "with activity right about now.\x02\x03",

            "But I have some important matters\x01",
            "to discuss at the moment.\x02\x03",

            "You two go and enjoy the festivities\x01",
            "without me, if you would.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_698")

    TalkEnd(0xFE)
    Return()

    # Function_4_541 end

    def Function_5_69C(): pass

    label("Function_5_69C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_6CC")

    ChrTalk(    #3
        0x17,
        "#160FRichard... That idiot...\x02",
    )

    CloseMessageWindow()
    Jump("loc_938")

    label("loc_6CC")

    OP_A2(0x1)

    ChrTalk(    #4
        0x17,
        "#160FWell, hello. It's been a while!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#000FGeneral Morgan?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x102,
        "#010FIt has been a long time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x17,
        (
            "#160FI heard you saved my granddaughter\x01",
            "out at the Erbe Royal Villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        "#000FThe Villa... Oh, yeah! Rianne!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x102,
        (
            "#010FWe only did what was needed.\x01",
            "It's the life of a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x17,
        (
            "#160FOh, stop with the humbleness\x01",
            "already. You're much too young\x01",
            "for that!\x02\x03",

            "This time, I'm going to thank\x01",
            "you properly.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        "#000FGeneral...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x17,
        "#160FYou two...did well. Very well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        (
            "#000F...I've got to say, I've heard\x01",
            "much more heartfelt thank yous\x01",
            "in my time.\x02\x03",

            "But not from you, General. So...\x01",
            "uh...thanks for the thanks!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_938")

    TalkEnd(0xFE)
    Return()

    # Function_5_69C end

    def Function_6_93C(): pass

    label("Function_6_93C")

    EventBegin(0x0)
    OP_6D(-20, 0, 140000, 0)
    OP_67(0, 8189, -10000, 0)
    OP_6B(2180, 0)
    OP_6C(45000, 0)
    OP_6E(473, 0)
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
    SetChrPos(0x8, 620, 500, 152930, 270)
    SetChrPos(0x9, -790, 500, 152790, 90)
    SetChrPos(0xA, -730, 0, 148500, 0)
    SetChrPos(0xB, 620, 0, 148500, 0)
    SetChrPos(0xC, -730, 0, 146900, 0)
    SetChrPos(0xD, 620, 0, 146900, 0)
    SetChrPos(0xE, -730, 0, 145500, 0)
    SetChrPos(0xF, 620, 0, 145500, 0)
    SetChrPos(0x10, -730, 0, 143900, 0)
    SetChrPos(0x11, 620, 0, 143900, 0)
    SetChrPos(0x12, -730, 0, 142300, 0)
    SetChrPos(0x13, 620, 0, 142300, 0)
    SetChrPos(0x14, -730, 0, 140700, 0)
    SetChrPos(0x15, 620, 0, 140700, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    FadeToBright(2000, 0)
    OP_6D(-60, 500, 152860, 5000)
    Fade(1000)
    OP_6D(-60, 500, 152860, 0)
    OP_67(0, 8189, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(45000, 0)
    OP_6E(473, 0)
    OP_0D()

    ChrTalk(    #14
        0x8,
        (
            "#187FWha...\x01",
            "What's the meaning of this?!\x02\x03",

            "How can we have lost contact\x01",
            "with the Erbe Royal Villa?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x9,
        (
            "#281FMost likely, it has fallen to\x01",
            "an external force.\x02\x03",

            "Either the Guardsmen or the bracers...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        (
            "#186FThose interfering little...\x02\x03",

            "Were you not in command of that\x01",
            "division, 2nd Lieutenant?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x9,
        (
            "#280FIt is a pity...\x02\x03",

            "But what's done is done. Obsessing\x01",
            "about it now will accomplish nothing.\x02\x03",

            "Furthermore, we must strengthen\x01",
            "the castle's defenses to ensure\x01",
            "that Her Majesty is not taken.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        "#187FI don't need you to tell me that!\x02",
    )

    CloseMessageWindow()

    def lambda_D43():
        OP_6D(-20, 500, 151500, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D43)
    OP_8C(0x8, 180, 400)
    OP_8E(0x8, 0x136, 0x1F4, 0x25206, 0x7D0, 0x0)
    OP_8C(0x9, 180, 400)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #19
        0x8,
        (
            "#185FI want the castle gate sealed!\x01",
            "Not a soul is to enter from\x01",
            "here on out!\x02\x03",

            "The only attacks I should need\x01",
            "to worry about are the ones\x01",
            "that come from the sky!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xB,
        "#2PYes, ma'am!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x8,
        (
            "#185FOnce that's done, scrape up troops from\x01",
            "wherever you can find them--anywhere in\x01",
            "Liberl--and send them to the villa!\x02\x03",

            "Priority one is to subjugate the\x01",
            "terrorists who deceived the royal\x01",
            "family!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    SetMessageWindowPos(350, 250, -1, -1)
    SetChrName("Special Ops Soldiers")

    AnonymousTalk(    #22
        "\x07\x00#5SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    OP_43(0xE, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xF, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0xC, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xD, 0x1, 0x0, 0x8)
    Sleep(300)
    OP_43(0xA, 0x1, 0x0, 0x7)
    Sleep(50)
    OP_43(0xB, 0x1, 0x0, 0x8)
    Sleep(1000)

    def lambda_F99():
        OP_6D(-250, 500, 152390, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F99)
    Sleep(500)

    def lambda_FB6():

        label("loc_FB6")

        TurnDirection(0xFE, 0x8, 400)
        OP_48()
        Jump("loc_FB6")

    QueueWorkItem2(0x9, 1, lambda_FB6)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #23
        0x9,
        "#280FHa ha... Nicely done.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 400)

    ChrTalk(    #24
        0x8,
        (
            "#180FHmph...of course it was. I've\x01",
            "served with this unit for some\x01",
            "time, unlike you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_104C():
        OP_6D(-1270, 2700, 154040, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_104C)

    def lambda_1064():
        OP_67(0, 3190, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1064)

    def lambda_107C():
        OP_6C(38000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_107C)

    def lambda_108C():
        OP_6B(1600, 2000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_108C)
    OP_8C(0x8, 0, 400)
    OP_8E(0x8, 0x15E, 0x1F4, 0x255C6, 0x3E8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #25
        0x8,
        (
            "#183F#2PI swear, I WILL protect this castle while His\x01",
            "Excellency is absent...no matter the cost!\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_21()
    OP_A2(0x3FC)
    NewScene("ED6_DT01/T4302   ._SN", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_6_93C end

    def Function_7_113A(): pass

    label("Function_7_113A")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0xFFFFFD26, 0x0, 0x1AE8C, 0xFA0, 0x0)
    Return()

    # Function_7_113A end

    def Function_8_1156(): pass

    label("Function_8_1156")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x26C, 0x0, 0x1AE8C, 0xFA0, 0x0)
    Return()

    # Function_8_1156 end

    SaveToFile()

Try(main)
