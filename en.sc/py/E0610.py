from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0610   ._SN',
        MapName             = 'Event',
        Location            = 'E0610.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60001",
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
        'Luciola',                              # 9
        'Walter',                               # 10
        'Campanella',                           # 11
        'Crimson Soldier',                      # 12
        'Crimson Soldier',                      # 13
        'Crimson Soldier',                      # 14
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
        'ED6_DT27/CH03523 ._CH',             # 00
        'ED6_DT27/CH03503 ._CH',             # 01
        'ED6_DT27/CH03600 ._CH',             # 02
        'ED6_DT26/CH20396 ._CH',             # 03
        'ED6_DT26/CH20387 ._CH',             # 04
        'ED6_DT26/CH20392 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT27/CH03523P._CP',             # 00
        'ED6_DT27/CH03503P._CP',             # 01
        'ED6_DT27/CH03600P._CP',             # 02
        'ED6_DT26/CH20396P._CP',             # 03
        'ED6_DT26/CH20387P._CP',             # 04
        'ED6_DT26/CH20392P._CP',             # 05
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
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_19A",          # 00, 0
        "Function_1_27E",          # 01, 1
        "Function_2_284",          # 02, 2
        "Function_3_9AD",          # 03, 3
        "Function_4_EEE",          # 04, 4
        "Function_5_11AA",         # 05, 5
        "Function_6_15E1",         # 06, 6
        "Function_7_1630",         # 07, 7
        "Function_8_1678",         # 08, 8
        "Function_9_1975",         # 09, 9
        "Function_10_1EB1",        # 0A, 10
        "Function_11_22A6",        # 0B, 11
        "Function_12_29FF",        # 0C, 12
    )


    def Function_0_19A(): pass

    label("Function_0_19A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B9")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 2)
    Jump("loc_27D")

    label("loc_1B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1D3")
    OP_A3(0x10F1)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)
    Jump("loc_27D")

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_1ED")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 4)
    Jump("loc_27D")

    label("loc_1ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_207")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F3)
    Event(0, 5)
    Jump("loc_27D")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_221")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F4)
    Event(0, 8)
    Jump("loc_27D")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_23B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    Event(0, 9)
    Jump("loc_27D")

    label("loc_23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_255")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F6)
    Event(0, 10)
    Jump("loc_27D")

    label("loc_255")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_26F")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x2B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F7)
    Event(0, 11)
    Jump("loc_27D")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_27D")
    OP_A3(0x10F8)
    Event(0, 12)

    label("loc_27D")

    Return()

    # Function_0_19A end

    def Function_1_27E(): pass

    label("Function_1_27E")

    OP_22(0x7A, 0x1, 0x46)
    Return()

    # Function_1_27E end

    def Function_2_284(): pass

    label("Function_2_284")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(-2140, 0, 2420, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(1580, 0)
    OP_6C(315000, 0)
    OP_6E(522, 0)
    SetChrFlags(0x8, 0x4)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0x8, 0)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x8, 1)
    SetChrSubChip(0x9, 2)
    SetChrPos(0x8, -630, 300, 2150, 180)
    SetChrPos(0x9, 1130, 300, 2150, 180)
    SetChrPos(0xA, -2470, 0, 1930, 0)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #0
        0x8,
        (
            "#240F#6PThe last experiment... They mean to go up\x01",
            "against the legend, I take it?\x02\x03",

            "Even the professor and Loewe are going to\x01",
            "struggle with that, I would imagine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        (
            "#250F#4PHeh. Maybe.\x02\x03",

            "We're talking 'bout hijacking a creature\x01",
            "of legend, after all. Ain't quite like throwin'\x01",
            "pictures around or shakin' the earth.\x02\x03",

            "#252FBut hey, Campanella. This ain't like you.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4BB():
        OP_8C(0xA, 90, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_4BB)
    Sleep(200)
    SetChrSubChip(0x8, 0)
    Sleep(100)
    SetChrSubChip(0x8, 2)
    Sleep(200)

    ChrTalk(    #2
        0xA,
        "#850F#6POoooh, what's this, now?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x9,
        (
            "#252F#4PYou're usually happily taggin' along with\x01",
            "the professor.\x02\x03",

            "If you ain't doin' that--especially when things\x01",
            "are THIS interesting--that means something\x01",
            "even better's come up.\x02\x03",

            "So spit it out, already.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        (
            "#852F#6PWhy, Walter, I'm hurt.\x01",
            "Have you so little faith in me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x9,
        "#252F#4PI trust you as much as your number.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#241F#4PWhat overflowing camaraderie,\x01",
            "Walter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xA,
        (
            "#855F#6PSuch slings! Such arrows! You two are\x01",
            "so cruel!\x02\x03",

            "#850FWell. In truth, I would love to sit back and\x01",
            "watch the fireworks unfold, but as it turns\x01",
            "out, I've a bit of work to do.\x02\x03",

            "I'm off to gain us permission\x01",
            "to use the Ark.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #8
        0x9,
        (
            "#253F#4PShit! Seriously?!\x02\x03",

            "We're finally busting THAT monstrosity\x01",
            "out?! This mission gets better every day!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "#244F#4PThe crimson ark... The Glorious.\x02\x03",

            "#242FI find it hard to believe we would use such...\x01",
            "Do we intend to turn this nation into nothing\x01",
            "more than a smoking crater?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xA,
        (
            "#854F#6PHeh heh. That will be up to the professor\x01",
            "and Loewe.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xA, 0, 300)
    Sleep(500)

    ChrTalk(    #11
        0xA,
        (
            "#853F#6PSo I am afraid I must depart as soon\x01",
            "as we're done.\x02\x03",

            "I so look forward to hearing about our\x01",
            "experiment when I get back!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C1600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_284 end

    def Function_3_9AD(): pass

    label("Function_3_9AD")

    EventBegin(0x0)
    OP_24(0x7A, 0x46)
    SetChrFlags(0x102, 0x80)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -70600, 1300, -160, 270)
    SetChrPos(0xC, -70600, 1200, 2150, 270)
    SetChrPos(0xD, -70600, 1200, -2500, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_A89():

        label("loc_A89")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_A89")

    QueueWorkItem2(0x101, 3, lambda_A89)
    OP_71(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_71(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #12
        0xB,
        (
            "#4PAltitude stable at 1559 arge.\x01",
            "Crossing into Liberlian airspace now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xB,
        "#4PSet course for Valleria Lake.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xC,
        "Roger.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xC, 1)
    Sleep(300)

    ChrTalk(    #15
        0xC,
        (
            "Doesn't look like the Liberlian airships\x01",
            "noticed us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xC,
        (
            "Stealth functionality... Nice little piece of\x01",
            "tech they loaded us up with.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xD, 2)
    Sleep(300)

    ChrTalk(    #17
        0xD,
        (
            "#1PIf we didn't have that doohickey we'd be\x01",
            "causing a bit of a fuss right about now,\x01",
            "y'know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xD,
        (
            "#1PI mean, forget us. Imagine what would happen\x01",
            "if those Liberl hicks saw THAT monster comin'\x01",
            "for them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xC,
        "Haha, don't I wish I could see that.\x02",
    )

    CloseMessageWindow()
    OP_20(0x0)
    OP_44(0x101, 0x3)
    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    OP_22(0x1F7, 0x0, 0x55)
    Sleep(100)
    OP_22(0x1FA, 0x0, 0x55)
    Sleep(900)
    OP_62(0xB, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0xD, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x1F7, 0x0, 0x55)
    Sleep(500)
    OP_7C(0x0, 0x64, 0xBB8, 0x3E8)
    OP_22(0x1FA, 0x0, 0x55)
    Sleep(1000)

    def lambda_D83():

        label("loc_D83")

        OP_7C(0xA, 0xA, 0xBB8, 0x64)
        OP_48()
        Jump("loc_D83")

    QueueWorkItem2(0x101, 3, lambda_D83)
    SetChrSubChip(0xC, 0)
    Sleep(100)

    ChrTalk(    #20
        0xD,
        "#1PWha...!\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xD, 0)
    Sleep(100)

    ChrTalk(    #21
        0xC,
        "Are we under attack?!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_1D(0x59)
    Sleep(500)

    ChrTalk(    #22
        0xB,
        (
            "#4PThe hell are you idiots panicking for?!\x01",
            "Check the damn radar!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xC,
        (
            "Contact! One small ship approaching from\x01",
            "four o'clock!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xD,
        "#1PDatabase match...found!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xD,
        (
            "#1PThe Capua sky bandit ship 'Bobcat'!\x01",
            "Reinford make!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xB,
        "#4PSKY BANDITS?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_9AD end

    def Function_4_EEE(): pass

    label("Function_4_EEE")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrFlags(0x102, 0x80)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xB, -70600, 1300, -160, 270)
    SetChrPos(0xC, -70600, 1200, 2150, 270)
    SetChrPos(0xD, -70600, 1200, -2500, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xC, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrSubChip(0xB, 0)
    SetChrSubChip(0xC, 0)
    SetChrSubChip(0xD, 0)
    OP_76(0x4, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x4, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_FCA():

        label("loc_FCA")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_FCA")

    QueueWorkItem2(0x101, 3, lambda_FCA)
    OP_71(0x3, 0x4)
    OP_72(0x4, 0x4)
    OP_71(0x5, 0x4)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #27
        0xC,
        "The airship is breaking off?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xD,
        "#1PWhat do we do? Do we pursue?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        "#4PNo, leave 'em alone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xB,
        (
            "#4PIf they were Royal Army we'd have to\x01",
            "pike 'em all, but we don't have time to\x01",
            "bother with small fries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xD,
        "#1PUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xC,
        (
            "Right now our only job is clearing the\x01",
            "Glorious' flight path.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xB,
        "#4PLet's head back to base for now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xB,
        (
            "#4PWe should let Sir Campanella know about\x01",
            "the bandits.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_EEE end

    def Function_5_11AA(): pass

    label("Function_5_11AA")

    EventBegin(0x0)
    OP_23(0x7A)
    OP_6D(2150, 0, 700, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x0, 0x4)
    OP_72(0x1, 0x4)
    OP_74(0xFF, 0x6, 0x8)
    OP_75(0xFF, 0x6, 0x0)
    FadeToBright(1000, 0)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(1500)
    OP_43(0x101, 0x1, 0x0, 0x7)
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #35
        0x102,
        (
            "#1032F#6PLock the door.\x02\x03",

            "I'll get the ship launched immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1005FG-Got it!\x02",
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 600)

    def lambda_12A8():
        OP_8C(0xFE, 90, 600)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12A8)

    def lambda_12B6():
        OP_8E(0xFE, 0xFFFFF39E, 0x0, 0xFFFFFFA6, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12B6)
    WaitChrThread(0x101, 0x1)

    def lambda_12D6():
        OP_8E(0xFE, 0x1676, 0x0, 0xFFFFFFF6, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12D6)
    WaitChrThread(0x102, 0x1)
    OP_72(0x2, 0x10)
    OP_72(0x2, 0x20)
    OP_6F(0x2, 0)
    OP_70(0x2, 0xF)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x2)
    FadeToDark(1000, 0, -1)

    def lambda_1320():
        OP_8E(0xFE, 0xFFFFE912, 0x0, 0x8C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1320)
    Sleep(100)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    SetChrFlags(0x102, 0x80)
    OP_0D()
    Sleep(1500)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_44(0x102, 0x1)
    OP_9F(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 4)
    SetChrSubChip(0x102, 0)
    SetChrPos(0x102, -70600, 1200, -220, 270)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x102,
        (
            "#1033F#5P(Activation key...recognized.)\x02\x03",

            "(Confirmation code...entered.)\x02\x03",

            "#1035F(...And we can go!)\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    OP_75(0xFF, 0x6, 0x2)
    OP_74(0xFF, 0x6, 0x8)
    Sleep(100)
    OP_74(0xFF, 0x6, 0x9)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xA)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xB)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xC)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xD)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xE)
    Sleep(100)
    OP_74(0xFF, 0x6, 0xF)
    Sleep(100)
    OP_75(0xFF, 0x6, 0x2)
    Sleep(1000)

    def lambda_14CB():
        OP_6D(-69000, 1000, 300, 1500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14CB)
    OP_9F(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x101, -63530, 0, -80, 270)

    def lambda_14FF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_14FF)
    OP_8E(0x101, 0xFFFEFD0E, 0x0, 0xFFFFFFCE, 0xBB8, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #38
        0x101,
        "#1004F#2PWaaa-aaah!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(300)

    ChrTalk(    #39
        0x102,
        (
            "#1031F#3PI'm opening the hatch via remote control.\x02\x03",

            "We'll be launching immediately,\x01",
            "so take a seat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1006F#2POkay!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5406   ._SN", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_5_11AA end

    def Function_6_15E1(): pass

    label("Function_6_15E1")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 7480, 0, -60, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1608():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1608)
    OP_8E(0xFE, 0x7D0, 0x0, 0xFFFFFFC4, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_15E1 end

    def Function_7_1630(): pass

    label("Function_7_1630")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 7480, 0, -60, 270)
    ClearChrFlags(0xFE, 0x80)

    def lambda_1657():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1657)
    OP_8E(0xFE, 0x1388, 0x0, 0xFFFFFFC4, 0xFA0, 0x0)
    Return()

    # Function_7_1630 end

    def Function_8_1678(): pass

    label("Function_8_1678")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x4, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0xC, 0x0, 0x0, 0x0)

    def lambda_173E():

        label("loc_173E")

        OP_7C(0x3C, 0x3C, 0xBB8, 0x64)
        OP_48()
        Jump("loc_173E")

    QueueWorkItem2(0x101, 2, lambda_173E)
    OP_D0(5000, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #41
        0x101,
        "#4P#1020FW-We're FALLING!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        "#1031F#6PIt's fine. We'll correct shortly.\x02",
    )

    OP_D0(4000, 0)
    Sleep(500)
    OP_D0(3000, 0)
    Sleep(500)
    OP_D0(2000, 0)
    Sleep(500)
    OP_D0(1000, 0)
    Sleep(500)
    OP_D0(0, 0)
    Sleep(500)

    def lambda_1805():

        label("loc_1805")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1805")

    QueueWorkItem2(0x101, 2, lambda_1805)

    ChrTalk(    #43 op#A op#5
        0x102,
        "#1035F#6P#20AThere we go.\x05\x02",
    )

    Sleep(1000)
    OP_DB()
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x3, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x9, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x3, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x1, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x2, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_76(0x3, 0x0, 0x1, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0x0, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DB()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1678 end

    def Function_9_1975(): pass

    label("Function_9_1975")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_1A31():

        label("loc_1A31")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1A31")

    QueueWorkItem2(0x101, 3, lambda_1A31)
    FadeToBright(1000, 0)
    OP_0D()
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    Sleep(200)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #44
        0x101,
        (
            "#1020F#4PWhoa! This is a radar, isn't it?\x02\x03",

            "There's, um, three lights, getting closer!\x01",
            "I think!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1030F#6PMm. Pursuers.\x02\x03",

            "We'll need to evade them somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1015F#4PUh, Joshua.\x01",
            "You know how to fly an airship?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x102,
        (
            "#1031F#6PThe basics, at least.\x02\x03",

            "#1035FThis ship doesn't have any armaments,\x01",
            "however.\x02\x03",

            "This isn't the best situation for us\x01",
            "to be in...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x101,
        (
            "#1007F#4POh, great...\x02\x03",

            "#1004FWait, why did you go for a ship with\x01",
            "no weapons?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x102,
        (
            "#1033F#6P...This ship was undergoing maintenance so\x01",
            "the security was lighter.\x02\x03",

            "It was an emergency, so I didn't have time\x01",
            "to be picky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        "#1015F#4PAn emergency...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #51
        0x101,
        (
            "#1026F#4PUm... You don't mean...\x02\x03",

            "You don't mean the fact that I was caught\x01",
            "on the Glorious?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x102,
        (
            "#1035F#6P...\x02\x03",

            "#1031FEnough. We're going to be flying rough,\x01",
            "so hang on to something.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1FA, 0x1, 0x50)

    def lambda_1E26():

        label("loc_1E26")

        OP_7C(0x0, 0x64, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1E26")

    QueueWorkItem2(0x101, 3, lambda_1E26)
    Sleep(1000)
    OP_22(0x1FA, 0x1, 0x5A)

    def lambda_1E4B():

        label("loc_1E4B")

        OP_7C(0x0, 0x96, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1E4B")

    QueueWorkItem2(0x101, 3, lambda_1E4B)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0)

    ChrTalk(    #53
        0x101,
        "#1020F#4PWaaaaaaaaaaah!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F9)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1975 end

    def Function_10_1EB1(): pass

    label("Function_10_1EB1")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71670, 900, 1010, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_6D(-72410, 1200, 1310, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_1FAA():

        label("loc_1FAA")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_1FAA")

    QueueWorkItem2(0x101, 3, lambda_1FAA)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #54
        0x102,
        "#1032F#5PTch. This is bad...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x101,
        "#1002F#4PThose guys chasing us seem pretty good...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x102,
        (
            "#1035F#5PThe pilots have been put through one of the\x01",
            "society's piloting-focused enhancement\x01",
            "programs, most likely.\x02\x03",

            "They won't be very good at adapting to the\x01",
            "unusual, but for more common tasks like\x01",
            "chasing down a ship...they're very good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1007F#4PI get it... They're like those guys from earlier.\x02\x03",

            "#1015FIf they're bad at adapting, though,\x01",
            "maybe we can cause some kind\x01",
            "of accident--\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x1FE, 0x0, 0x50)
    Sleep(1000)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #58
        0x101,
        "#1004F#4PGyah! Were we hit?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x102,
        "#1034F#5PNo, wait. That wasn't our ship!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FA)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_1EB1 end

    def Function_11_22A6(): pass

    label("Function_11_22A6")

    EventBegin(0x0)
    OP_24(0x7A, 0x64)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_2362():

        label("loc_2362")

        OP_7C(0x14, 0x14, 0xBB8, 0x64)
        OP_48()
        Jump("loc_2362")

    QueueWorkItem2(0x101, 3, lambda_2362)
    LoadEffect(0x0, "map\\\\mp001_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -71400, 2200, 2240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #60
        0x101,
        "#1020F#4PThat's...! No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x102,
        "#1034F#6PThe Bobcat! But why?\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x46)
    Sleep(1000)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Voice from Speaker")

    AnonymousTalk(    #62
        "\x07\x05Joshua!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Voice from Speaker")

    AnonymousTalk(    #63
        "\x07\x05Joshua, you're on that ship, right?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x101,
        "#1019F#4P(That voice... THAT voice.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#1031F#6PYes, it's me!\x02\x03",

            "What are you guys doing here?!\x02\x03",

            "I thought you'd be out of Liberl by now!\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #66
        (
            "\x07\x05Heh-heh! My brothers got all worried that\x01",
            "you might run into a problem.\x02\x03",

            "So we've been shadowing that flying whale\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("Kyle")

    AnonymousTalk(    #67
        (
            "\x07\x05Heh, reeeeeally?\x02\x03",

            "Who was the one begging us to follow Joshua,\x01",
            "lookin' all worked up and ready to faint?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #68
        "\x07\x05K-KYLE!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Don")

    AnonymousTalk(    #69
        (
            "\x07\x05Enough, you two.\x01",
            "And besides, we have a little payback\x01",
            "to give the society ourselves.\x02\x03",

            "We thought we could stick around here\x01",
            "until we settled our OTHER debt.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #70
        0x102,
        (
            "#1035F#6PI see.\x02\x03",

            "#1031FThank you. You saved me.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #71
        "\x07\x05Heheh! Yeah, you better be grateful!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("Kyle")

    AnonymousTalk(    #72
        (
            "\x07\x05We've had an eye on you for a while and\x01",
            "noticed you weren't firing back.\x02\x03",

            "There some kind of problem?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #73
        0x102,
        (
            "#1035F#6PI had to take a ship with no armaments.\x02\x03",

            "It's proven to be a bit of an issue.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("Kyle")

    AnonymousTalk(    #74
        "\x07\x05I can imagine.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #75
        "\x07\x05Wh-What do we do then...?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Don")

    AnonymousTalk(    #76
        (
            "\x07\x05Right, then! We'll split them in two!\x02\x03",

            "You can probably lose one, right?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #77
        0x102,
        "#1031F#6POne... No problem.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 100, -1, -1)
    SetChrName("Kyle")

    AnonymousTalk(    #78
        (
            "\x07\x05It's a plan, then.\x01",
            "Blessings of Aidios be with you!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(100, 50, -1, -1)
    SetChrName("Josette")

    AnonymousTalk(    #79
        "\x07\x05Joshua! Take care, you hear me?!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10FB)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_22A6 end

    def Function_12_29FF(): pass

    label("Function_12_29FF")

    EventBegin(0x0)
    SetChrChipByIndex(0x101, 5)
    SetChrChipByIndex(0x102, 4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -70610, 1200, 30, 270)
    SetChrPos(0x101, -70590, 1200, 2020, 270)
    OP_6D(-71650, 1200, 960, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_72(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_76(0x3, 0x0, 0x1, 0xFFFFFFFA, 0xFFFFFFFD, 0x0, 0x0, 0x0)
    OP_76(0x3, 0x1, 0x1, 0xFFFFFFF8, 0xFFFFFFFB, 0x0, 0x0, 0x0)

    def lambda_2AB7():

        label("loc_2AB7")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_2AB7")

    QueueWorkItem2(0x101, 3, lambda_2AB7)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(300)

    ChrTalk(    #80
        0x102,
        "#1031F#6P#6PEstelle, is anything on the radar?\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x101, 1)
    Sleep(300)

    ChrTalk(    #81
        0x101,
        (
            "#1006F#4PNope! All the lights are out, it looks like.\x02\x03",

            "Seems like we completely lost them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x102,
        (
            "#1031F#6PGood...\x02\x03",

            "#1033F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        "#1013F#4P...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_62(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #84
        0x101,
        (
            "#1008F#4PU-Umm...\x02\x03",

            "#1016FI gotta say, I was surprised by the bandits!\x01",
            "They're kind of okay!\x02\x03",

            "I never thought they'd show up out of the\x01",
            "blue to save us like that...\x02\x03",

            "#1017FMaybe I've been a bit too hard on them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x102,
        (
            "#1033F#6PIt's true.\x02\x03",

            "#1031FI just saw us as two parties bound to a contract...\x02\x03",

            "But I suppose relationships between people\x01",
            "aren't that simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x101,
        (
            "#1016F#4PHaha... What's this all of a sudden?\x02\x03",

            "#1006FPut two people together and maybe\x01",
            "they'll fight, maybe they'll be friends.\x01",
            "All kinds of stuff can happen.\x02\x03",

            "That's just how people act, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x102,
        (
            "#1035F#6PYes.\x02\x03",

            "#1030F...'How people act' was never\x01",
            "very clear in the world I lived in.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x101,
        "#1020F#4POh...\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)
    Sleep(500)
    SetChrSubChip(0x102, 0)
    OP_21()
    OP_1D(0x5B)
    Sleep(500)

    def lambda_2EBD():
        OP_6B(2730, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2EBD)
    Sleep(1500)

    ChrTalk(    #89
        0x102,
        (
            "#1035F#6PKill, or be killed.\x02\x03",

            "Take, or be taken from.\x02\x03",

            "Until I met you, my life was an endless\x01",
            "cycle of such...simplicity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        (
            "#1026F#4PBut, um.\x02\x03",

            "#1003FEven you had some good times with\x01",
            "Loewe and your sister, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x102,
        (
            "#1033F#6PLoewe told you about that, did he?\x02\x03",

            "#1035F...\x02\x03",

            "#1045FIt's true I have those memories,\x01",
            "but they feel like someone else's...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1026F#4PWha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#1031F#6PAfter my heart was shattered...my memories\x01",
            "of Hamel were no longer my own.\x02\x03",

            "I think it's because I gave up being human\x01",
            "and chose to become a puppet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1026F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x102,
        (
            "#1031F#6PI do clearly remember my sister's death.\x02\x03",

            "#1035FShe and I were attacked by a man lying\x01",
            "in wait for stragglers.\x02\x03",

            "The man swatted me away and...\x01",
            "forced my sister to the ground.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x101,
        "#1020F#4P...Oh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x102,
        (
            "#1033F#6PAt the time, I was too young to know what he\x01",
            "probably meant to do.\x02\x03",

            "All I knew was that he was hurting my sister\x01",
            "and I had a bad feeling, so I grabbed onto\x01",
            "the man's back.\x02\x03",

            "#1035FI ended up getting crushed and thrown\x01",
            "off immediately.\x02\x03",

            "Somehow, though, I had managed to\x01",
            "get my hands on the man's gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#1026F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x102,
        (
            "#1045F#6PThinking about it, I wonder.\x01",
            "Did I have a talent for killing people,\x01",
            "even then?\x02\x03",

            "I'd never even been taught how, but I still\x01",
            "removed the safety and pulled the trigger\x01",
            "with no hesitation.\x02\x03",

            "The man fell over, spewing blood from his\x01",
            "mouth, looking...confused.\x02\x03",

            "At that moment, I finally realized I'd\x01",
            "shot a man.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1003F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        (
            "#1032F#6PHe wasn't quite dead yet, though.\x02\x03",

            "He jumped up, combat knife out,\x01",
            "screaming and gurgling incoherently with\x01",
            "murder in his eyes.\x02\x03",

            "#1033FI curled up and closed my eyes,\x01",
            "like I was being attacked by a wild animal...\x02\x03",

            "#1035FBut there was no impact.\x01",
            "I was embraced by something soft.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#1026F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x102,
        (
            "#1033F#6PWhen I opened my eyes, there was my sister,\x01",
            "gently smiling at me.\x02\x03",

            "The man had collapsed at some point...\x01",
            "and Loewe was standing there, dumbstruck\x01",
            "with horror.\x02\x03",

            "My sister, cradled by Loewe, gave me her\x01",
            "harmonica...\x02\x03",

            "#1035F...and then she closed her eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        "#1027F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x102,
        (
            "#1035F#6PI remember every detail, you see.\x02\x03",

            "#1045FBut even talking about it like this\x01",
            "doesn't make me feel sad.\x02\x03",

            "It's just a slight tugging at the heart,\x01",
            "like reading a stranger's diary.\x02\x03",

            "#1033FAnd the same is true...of my time\x01",
            "with you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1026F#4P...No...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#1045F#6PI do think I was changed a little by\x01",
            "touching your warmth.\x02\x03",

            "I learned happiness and joy with you,\x01",
            "and finally came to think of you as\x01",
            "someone dear.\x02\x03",

            "But somewhere it all felt as if it was\x01",
            "distant.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #108
        (
            "\x07\x00#20WI suspect that's what my real self was feeling.\x02\x03",

            "The empty void...of the broken puppet that is\x01",
            "Joshua Astray.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_24(0x7A, 0x32)
    Sleep(100)
    OP_24(0x7A, 0x28)
    Sleep(100)
    OP_24(0x7A, 0x1E)
    Sleep(100)
    OP_24(0x7A, 0x14)
    Sleep(100)
    OP_24(0x7A, 0xA)
    Sleep(100)
    OP_24(0x7A, 0x0)
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2201   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_29FF end

    SaveToFile()

Try(main)
