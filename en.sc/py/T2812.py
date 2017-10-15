from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2812   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2812.x',
        MapIndex            = 1,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Jill',                                 # 9
        'Rhody',                                # 10
        'Alice',                                # 11
        'Mickey',                               # 12
        'Roy',                                  # 13
        'Monika',                               # 14
        'Dennis',                               # 15
        'Felicity',                             # 16
        'Purity',                               # 17
        'Mr. Effort',                           # 18
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
        'ED6_DT26/CH20271 ._CH',             # 00
        'ED6_DT07/CH02390 ._CH',             # 01
        'ED6_DT07/CH01360 ._CH',             # 02
        'ED6_DT07/CH01780 ._CH',             # 03
        'ED6_DT07/CH01080 ._CH',             # 04
        'ED6_DT07/CH01580 ._CH',             # 05
        'ED6_DT07/CH01370 ._CH',             # 06
        'ED6_DT07/CH01363 ._CH',             # 07
        'ED6_DT07/CH01090 ._CH',             # 08
        'ED6_DT07/CH01093 ._CH',             # 09
        'ED6_DT07/CH01460 ._CH',             # 0A
        'ED6_DT07/CH01583 ._CH',             # 0B
    )

    AddCharChipPat(
        'ED6_DT26/CH20271P._CP',             # 00
        'ED6_DT07/CH02390P._CP',             # 01
        'ED6_DT07/CH01360P._CP',             # 02
        'ED6_DT07/CH01780P._CP',             # 03
        'ED6_DT07/CH01080P._CP',             # 04
        'ED6_DT07/CH01580P._CP',             # 05
        'ED6_DT07/CH01370P._CP',             # 06
        'ED6_DT07/CH01363P._CP',             # 07
        'ED6_DT07/CH01090P._CP',             # 08
        'ED6_DT07/CH01093P._CP',             # 09
        'ED6_DT07/CH01460P._CP',             # 0A
        'ED6_DT07/CH01583P._CP',             # 0B
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
        X                   = -1340,
        Z                   = 4000,
        Y                   = -1350,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = -58700,
        Z                   = 0,
        Y                   = 25010,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = -29460,
        Z                   = 0,
        Y                   = 30840,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = -30830,
        Z                   = 450,
        Y                   = 26450,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = -62080,
        Z                   = 0,
        Y                   = 27320,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -28980,
        Z                   = 0,
        Y                   = 970,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -60470,
        Z                   = 0,
        Y                   = 950,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -61916,
        Z                   = 200,
        Y                   = 30650,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x115,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 30000,
        Z                   = 0,
        Y                   = 30750,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )


    ScpFunction(
        "Function_0_24A",          # 00, 0
        "Function_1_25E",          # 01, 1
        "Function_2_25F",          # 02, 2
        "Function_3_2B6",          # 03, 3
        "Function_4_358",          # 04, 4
        "Function_5_50D",          # 05, 5
        "Function_6_67D",          # 06, 6
        "Function_7_796",          # 07, 7
        "Function_8_956",          # 08, 8
        "Function_9_995",          # 09, 9
        "Function_10_AA0",         # 0A, 10
        "Function_11_B38",         # 0B, 11
        "Function_12_C6F",         # 0C, 12
        "Function_13_C93",         # 0D, 13
        "Function_14_15B6",        # 0E, 14
        "Function_15_1F40",        # 0F, 15
    )


    def Function_0_24A(): pass

    label("Function_0_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_25D")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 12)

    label("loc_25D")

    Return()

    # Function_0_24A end

    def Function_1_25E(): pass

    label("Function_1_25E")

    Return()

    # Function_1_25E end

    def Function_2_25F(): pass

    label("Function_2_25F")

    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "Hey, what is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "It's almost curfew, so don't wander\x01",
            "around too much.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_25F end

    def Function_3_2B6(): pass

    label("Function_3_2B6")

    TalkBegin(0xFE)

    ChrTalk(    #2
        0xFE,
        (
            "Many characters who appear in novels\x01",
            "are inspired by real people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Writing solely on imagination tends to\x01",
            "make the characters shallow and boring.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_2B6 end

    def Function_4_358(): pass

    label("Function_4_358")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_459")

    ChrTalk(    #4
        0xFE,
        (
            "I know she's my servant, but I never\x01",
            "really thought of her that way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'm from Erebonia, so I would've been\x01",
            "all alone without her. To me, she's like\x01",
            "my best friend.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "I thought that was more important\x01",
            "than our 'roles' in society...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_509")

    label("loc_459")

    OP_A2(0x5)

    ChrTalk(    #7
        0xFE,
        (
            "Reina should've known how much\x01",
            "I was looking forward to this journey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "How could she arrange a return trip\x01",
            "home behind my back?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "I feel like she's betrayed me.\x02",
    )

    CloseMessageWindow()

    label("loc_509")

    TalkEnd(0xFE)
    Return()

    # Function_4_358 end

    def Function_5_50D(): pass

    label("Function_5_50D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_59C")

    ChrTalk(    #10
        0xFE,
        (
            "Now that tests are over, I can use the\x01",
            "downtime to get a leg up on everyone\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        "All right! Time to study my tush off!\x02",
    )

    CloseMessageWindow()
    Jump("loc_679")

    label("loc_59C")

    OP_A2(0x4)

    ChrTalk(    #12
        0xFE,
        (
            "Now that tests are over, I can use the\x01",
            "downtime to get a leg up on everyone\x01",
            "else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Heh heh. I'm gonna study my tush off while\x01",
            "everyone else is relaxing and get that top\x01",
            "score on the next exam. Just you watch!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_679")

    TalkEnd(0xFE)
    Return()

    # Function_5_50D end

    def Function_6_67D(): pass

    label("Function_6_67D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_6F3")

    ChrTalk(    #14
        0xFE,
        (
            "We're all so wildly different from\x01",
            "one another in this dorm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Maybe that's why we work so well.\x02",
    )

    CloseMessageWindow()
    Jump("loc_792")

    label("loc_6F3")

    OP_A2(0x3)

    ChrTalk(    #16
        0xFE,
        "Purity's a bookworm, Alice loves anything cute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        "And me? I'm all about sports.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "We're all so wildly different from\x01",
            "one another in this dorm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_792")

    TalkEnd(0xFE)
    Return()

    # Function_6_67D end

    def Function_7_796(): pass

    label("Function_7_796")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_836")

    ChrTalk(    #19
        0xFE,
        (
            "A lot of students don't care about\x01",
            "the election at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "Bummer. This would have been such\x01",
            "a good chance to really discuss politics,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_952")

    label("loc_836")

    OP_A2(0x2)

    ChrTalk(    #21
        0xFE,
        (
            "Since my focus is political science,\x01",
            "I find the election really interesting.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "But, not many others share my\x01",
            "enthusiasm. Most of the students\x01",
            "couldn't care less, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        (
            "Logic's dad is one of the candidates,\x01",
            "so you'd think he'd take this election\x01",
            "pretty personally...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_952")

    TalkEnd(0xFE)
    Return()

    # Function_7_796 end

    def Function_8_956(): pass

    label("Function_8_956")

    TalkBegin(0xFE)

    ChrTalk(    #24
        0xFE,
        "Weird. Argyle's gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "I wonder where he went.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_956 end

    def Function_9_995(): pass

    label("Function_9_995")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A0B")

    ChrTalk(    #26
        0xFE,
        (
            "Kaden made this outfit for me.\x01",
            "Super cute, right?\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)

    ChrTalk(    #27
        0xFE,
        (
            "The power of the Art Club strikes\x01",
            "again!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A99")

    label("loc_A0B")

    OP_A2(0x1)

    ChrTalk(    #28
        0xFE,
        (
            "While I was cleaning up, I found the\x01",
            "outfit I wore for the school festival!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        "Kaden made it for me.\x02",
    )

    CloseMessageWindow()
    Call(0, 10)

    ChrTalk(    #30
        0xFE,
        "Super cute, right? ㈱\x02",
    )

    CloseMessageWindow()

    label("loc_A99")

    OP_63(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_9_995 end

    def Function_10_AA0(): pass

    label("Function_10_AA0")

    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    OP_51(0xFE, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(30)
    Return()

    # Function_10_AA0 end

    def Function_11_B38(): pass

    label("Function_11_B38")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BED")

    ChrTalk(    #31
        0xFE,
        (
            "Dennis ALWAYS gets good scores\x01",
            "on his tests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "And yet he's always studying like\x01",
            "he's one point away from expulsion.\x01",
            "It's so annoying.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "Rich kids, I guess.\x02",
    )

    CloseMessageWindow()
    Jump("loc_C6B")

    label("loc_BED")

    OP_A2(0x0)

    ChrTalk(    #34
        0xFE,
        (
            "My roommate, Dennis, is already\x01",
            "nose deep in his books.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "The exams just ended too.\x01",
            "What the hell? Relax a little!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6B")

    TalkEnd(0xFE)
    Return()

    # Function_11_B38 end

    def Function_12_C6F(): pass

    label("Function_12_C6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C80")
    Call(0, 15)

    label("loc_C80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C8E")
    Call(0, 13)
    Jump("loc_C92")

    label("loc_C8E")

    Call(0, 14)

    label("loc_C92")

    Return()

    # Function_12_C6F end

    def Function_13_C93(): pass

    label("Function_13_C93")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 24)
    OP_6F(0x9, 12)
    SetChrPos(0x101, -118350, 500, -2400, 0)
    SetChrPos(0x105, -118420, 0, -1130, 175)
    SetChrPos(0x8, -119240, 0, -1120, 145)
    SetChrPos(0x127, -120350, 0, -2570, 90)
    OP_6D(-118450, 500, -2400, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #36
        "...elle...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #37
        "Estelle...ake up...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #38
        "#1007FMmm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0x54)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 39)
    Sleep(100)
    SetChrSubChip(0x101, 40)
    Sleep(500)

    ChrTalk(    #39
        0x101,
        "#1004FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x127,
        "#150FEstelle, you're awake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x105,
        (
            "#542F#6POh, thank goodness...\x02\x03",

            "How do you feel?\x01",
            "Are you hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x101,
        "#1000FNo, I...think I'm okay.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_6F(0x9, 12)
    OP_70(0x9, 0xF)
    SetChrPos(0x101, -118250, 500, -2400, 0)
    OP_99(0x101, 0x19, 0x20, 0x3E8)
    Sleep(500)
    SetChrSubChip(0x101, 41)
    Sleep(100)
    SetChrSubChip(0x101, 42)
    Sleep(500)

    ChrTalk(    #43
        0x101,
        (
            "#1015FWait... This is the girls' dorm, right?\x02\x03",

            "Why am I--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(200)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_96(0x101, 0xFFFE3072, 0x0, 0xFFFFF0EC, 0x64, 0xFA0)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 16, 0)
    OP_6F(0x9, 15)
    OP_70(0x9, 0xC)

    def lambda_F8E():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F8E)

    def lambda_F9C():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_F9C)

    def lambda_FAA():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FAA)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #44
        0x101,
        (
            "#1020F#2PWAIT! I SAW IT!\x01",
            "I saw the white shadow,\x01",
            "right out that window!\x02\x03",

            "And then it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x8,
        "#645F#3P*sigh* So you really did see a ghost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x105,
        (
            "#043F#6PEstelle...\x02\x03",

            "What did the white shadow look like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1007F#2PW-Well...\x02\x03",

            "#1003FIt was a man dressed in old-fashioned\x01",
            "clothes, like an opera get-up or something,\x01",
            "and wearing a mask...\x02\x03",

            "He danced in circles, and he was glowing...\x02\x03",

            "He flew off toward the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x127,
        "#153FWhoooa! What a neato ghost!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x105,
        (
            "#047F#6PI'm going to hazard a guess that\x01",
            "this matches the description you've\x01",
            "heard before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x8,
        (
            "#644F#3PI figured the old schoolhouse would\x01",
            "have something to do with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1019F#2P...Screw it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x8,
        "#643F#3PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1022F#2PI dunno if this is a spook or a dude with\x01",
            "an airship in his pants or whatever...\x02\x03",

            "If he's gonna run around, looking crazy and\x01",
            "scaring people and making them faint...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #54
        0x101,
        (
            "#1005F#2P#3SI'm going to beat him to\x01",
            "a pulp once and for all!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #55
        0x8,
        "#645F#3PBeat him to a pulp...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x127,
        (
            "#153FOh, Estelle, do ghosts make you\x01",
            "angry and afraid and stuff?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x127, 500)
    Sleep(300)

    ChrTalk(    #57
        0x101,
        (
            "#1019F#2PI WAS scared of ghosts because I wasn't\x01",
            "sure if they existed or could rip my soul\x01",
            "out or something!\x02\x03",

            "Now that I've seen one, I ain't\x01",
            "afraid of no ghost! Not at all!\x02\x03",

            "If I see it again, I'm going to\x01",
            "polish my staff with its face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#644F#3PI'm...not sure if this is courage or\x01",
            "if she's gone off the deep end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x105,
        "#041F#6PHeehee... Oh, Estelle.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_C93 end

    def Function_14_15B6(): pass

    label("Function_14_15B6")

    EventBegin(0x0)
    OP_20(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x1)
    SetChrChipByIndex(0x101, 0)
    SetChrSubChip(0x101, 24)
    OP_6F(0x9, 12)
    SetChrPos(0x101, -118350, 500, -2400, 0)
    SetChrPos(0x103, -120030, 0, -4110, 35)
    SetChrPos(0x105, -118420, 0, -1130, 180)
    SetChrPos(0x8, -119240, 0, -1120, 145)
    SetChrPos(0x127, -120350, 0, -2570, 90)
    OP_6D(-118450, 500, -2400, 0)
    OP_67(0, 4720, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_69(0x101, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #60
        "...elle...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Girl's Voice")

    AnonymousTalk(    #61
        "Estelle...ake up...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #62
        "#1007FMmm...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_1D(0x54)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 39)
    Sleep(100)
    SetChrSubChip(0x101, 40)
    Sleep(500)

    ChrTalk(    #63
        0x101,
        "#1004FHuh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x127,
        "#150FEstelle, you're awake!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x105,
        "#542F#6POh, thank goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x103,
        (
            "#025FPhew!\x01",
            "You had us sweating there, Estelle.\x02\x03",

            "#020FSo, how do you feel?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        "#1000FI...think I'm okay.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_6F(0x9, 12)
    OP_70(0x9, 0xF)
    SetChrPos(0x101, -118250, 500, -2400, 0)
    OP_99(0x101, 0x19, 0x20, 0x3E8)
    Sleep(500)
    SetChrSubChip(0x101, 41)
    Sleep(100)
    SetChrSubChip(0x101, 42)
    Sleep(500)

    ChrTalk(    #68
        0x101,
        (
            "#1015FWait... This is the girls' dorm, right?\x02\x03",

            "Why am I--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 1500, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    Sleep(200)
    SetChrFlags(0x101, 0x4)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    OP_96(0x101, 0xFFFE3072, 0x0, 0xFFFFF0EC, 0x64, 0xFA0)
    SetChrFlags(0x101, 0x1)
    OP_8C(0x101, 16, 0)
    OP_6F(0x9, 15)
    OP_70(0x9, 0xC)

    def lambda_18ED():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18ED)

    def lambda_18FB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_18FB)

    def lambda_1909():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x127, 1, lambda_1909)

    def lambda_1917():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1917)
    WaitChrThread(0x105, 0x1)
    WaitChrThread(0x127, 0x1)
    WaitChrThread(0x8, 0x1)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #69
        0x101,
        (
            "#1020F#2PWAIT! I SAW IT!\x01",
            "I saw the white shadow,\x01",
            "right out that window!\x02\x03",

            "And then it...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x103,
        "#020FWe know, honey. Calm down.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        "#645F#3P*sigh* So you really did see a ghost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x105,
        (
            "#043F#6PEstelle...\x02\x03",

            "What did the white shadow look like?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#1007F#2PW-Well...\x02\x03",

            "#1003FIt was a man dressed in old-fashioned\x01",
            "clothes, like an opera get-up or something,\x01",
            "and wearing a mask...\x02\x03",

            "He danced in circles, and he was glowing...\x02\x03",

            "He flew off toward the old schoolhouse.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x127,
        "#153FWhoooa! What a neato ghost!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x105,
        (
            "#047F#6PI'm going to hazard a guess that\x01",
            "this matches the description you've\x01",
            "heard before, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x8,
        (
            "#644F#3PI figured the old schoolhouse would\x01",
            "have something to do with this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        "#1019F#2P...Screw it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "#643F#3PBwuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x101,
        (
            "#1022F#2PI dunno if this is a spook or a dude with\x01",
            "an airship in his pants or whatever...\x02\x03",

            "If he's gonna run around, looking crazy and\x01",
            "scaring people and making them faint...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #80
        0x101,
        (
            "#1005F#2P#3SI'm going to beat him to\x01",
            "a pulp once and for all!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x8,
        "#645F#3PBeat him to a pulp...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x103,
        (
            "#027FAnd what, exactly, happened to\x01",
            "your fear of ghosts?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    ChrTalk(    #83
        0x101,
        (
            "#1019F#2PI WAS scared of ghosts because I wasn't\x01",
            "sure if they existed or could rip my soul\x01",
            "out or something!\x02\x03",

            "Now that I've seen one, I ain't afraid\x01",
            "of no ghost! Not at all!\x02\x03",

            "If I see it again, I'm going to\x01",
            "polish my staff with its face!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x8,
        (
            "#644F#3PI'm...not sure if this is courage or\x01",
            "if she's gone off the deep end...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x105,
        "#041F#6PHeehee... Oh, Estelle.\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T2811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_15B6 end

    def Function_15_1F40(): pass

    label("Function_15_1F40")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
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
        (0, "loc_1FB9"),
        (1, "loc_1FBF"),
        (SWITCH_DEFAULT, "loc_1FC5"),
    )


    label("loc_1FB9")

    OP_A2(0x1200)
    Jump("loc_1FC5")

    label("loc_1FBF")

    OP_A2(0x1201)
    Jump("loc_1FC5")

    label("loc_1FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1FD3")
    AddParty(0x2, 0xF7, 0xFF)
    Jump("loc_1FD7")

    label("loc_1FD3")

    AddParty(0x5, 0xF7, 0xFF)

    label("loc_1FD7")

    Return()

    # Function_15_1F40 end

    SaveToFile()

Try(main)
