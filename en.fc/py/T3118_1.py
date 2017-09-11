from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118_1 ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_AB",           # 01, 1
        "Function_2_AC",           # 02, 2
        "Function_3_11F9",         # 03, 3
        "Function_4_13DA",         # 04, 4
        "Function_5_2069",         # 05, 5
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    Return()

    # Function_1_AB end

    def Function_2_AC(): pass

    label("Function_2_AC")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-2930, 0, 6630, 0)
    SetChrPos(0x101, -2950, 0, 6740, 90)
    SetChrPos(0x102, -2810, 0, 5490, 45)
    SetChrPos(0x107, -3850, 0, 6140, 90)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x2C, 0x1, 0x2000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")

    ChrTalk(    #0
        0xFE,
        "I swear...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "This time, you're not getting\x01",
            "away...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A8")

    ChrTalk(    #2
        0x101,
        "#000FHi, Dr. Miriam.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x107,
        "#060FHi, there...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #4
        0xFE,
        "Oh, good afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Oh, my. So many of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#000FWe saw your posting on\x01",
            "the bulletin board.\x02\x03",

            "Heh, might help if we introduced\x01",
            "ourselves, huh?\x02\x03",

            "I'm Estelle, junior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010FAnd I'm Joshua. Also\x01",
            "a junior bracer.\x02\x03",

            "We heard that there might\x01",
            "be a case for us here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)
    Jump("loc_3D2")

    label("loc_2A8")

    OP_A2(0x589)
    OP_A2(0x58A)

    ChrTalk(    #8
        0x107,
        "#060FGood afternoon, Dr. Miriam.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #9
        0xFE,
        "Oh, good afternoon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Oh, my. So many of you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#000FYeah, we saw your posting\x01",
            "on the bulletin board.\x02\x03",

            "I'm Estelle, junior bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        (
            "#010FAnd I'm Joshua. Also\x01",
            "a junior bracer.\x02\x03",

            "We heard that there might\x01",
            "be a case for us here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    label("loc_3D2")


    ChrTalk(    #13
        0xFE,
        "Yes, I'd certainly say so.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "If you can, it'd be ideal if\x01",
            "you started your investigation\x01",
            "at once...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "Do you think it'd be possible?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4C9")

    label("loc_465")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #16
        0xFE,
        "Oh, hello, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Have you made up your minds\x01",
            "about starting the investigation?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[Yes]\x01",      # 0
            "[No]\x01",       # 1
        )
    )

    MenuEnd(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_647")
    Sleep(100)

    ChrTalk(    #18
        0x101,
        (
            "#505FMmm, now's really not the\x01",
            "best time.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #19
        0xFE,
        (
            "That's unfortunate. It really\x01",
            "is an urgent piece of business.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "But if your schedules don't \x01",
            "permit it, then I'll simply\x01",
            "have to wait.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#006FSorry...but we'll be back soon.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        "That would be most appreciated.\x02",
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x1, 0x2000)

    def lambda_63C():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_63C)
    EventEnd(0x0)
    Return()

    label("loc_647")

    Sleep(100)

    ChrTalk(    #23
        0x101,
        "#006FOkay, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        (
            "#012FI know this is urgent, but can\x01",
            "you provide us with any more\x01",
            "details?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #25
        0xFE,
        (
            "Well, it's not a complicated\x01",
            "tale to tell.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 90, 400)

    ChrTalk(    #26
        0xFE,
        (
            "Someone took the cigarettes\x01",
            "that were in this cabinet.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #27
        0x101,
        (
            "#505FThis is a medical office.\x01",
            "Why would you even have\x01",
            "cigarettes here?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #28
        0xFE,
        (
            "Under my supervision, this factory\x01",
            "has observed a no-smoking policy\x01",
            "for the last several years.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Any confiscated tobacco\x01",
            "is kept in here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#012FWhich would mean that anyone\x01",
            "who's had anything confiscated\x01",
            "is immediately a suspect.\x02\x03",

            "Since what was taken probably\x01",
            "belongs to that individual to\x01",
            "begin with.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x107,
        "#064FYeah, you're probably right.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #32
        0xFE,
        "I'm inclined to agree.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "It took so much work to get\x01",
            "the smoking ban established...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "If I just let this go, it will\x01",
            "completely undermine the entire\x01",
            "policy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#012FFirst of all, we should talk to\x01",
            "the people that were smokers to\x01",
            "begin with.\x02\x03",

            "Would you happen to know\x01",
            "who that would be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "My first suggestion would\x01",
            "be Supervisor Travis, from\x01",
            "Operations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "He's always been a heavy smoker.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "Plus, he's never really accepted\x01",
            "the ban, so I'd say he's got\x01",
            "motive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#505FHmmm...okay. Sounds like a good\x01",
            "place to start.\x02\x03",

            "#004F...So I'll make a note of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "There's also Hugo, in the\x01",
            "Design Room.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I think he's currently arranging\x01",
            "a meeting in the first floor lobby.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "The people who've worked\x01",
            "here the longest tend to\x01",
            "be the smokers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x107,
        "#064FAhh, okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#010FSo... There's Travis from the\x01",
            "Operations room, and Hugo on\x01",
            "the first floor.\x02\x03",

            "Is there anything else you\x01",
            "can tell us?\x02\x03",

            "If not, we can go ahead\x01",
            "and get started...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "Well, I don't know if it will\x01",
            "be of any use to you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        "But there was an eyewitness.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #47
        0x101,
        (
            "#004F...?!\x02\x03",

            "Uh, yeah, that might\x01",
            "be a lead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x102,
        "#012FAnd who was this eyewitness?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0xB, 400)

    ChrTalk(    #49
        0xFE,
        "He's right behind you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "Antoine...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DE3")

    def lambda_DDB():
        TurnDirection(0x1, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_DDB)

    label("loc_DE3")

    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E02")

    def lambda_DFA():
        TurnDirection(0x2, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_DFA)

    label("loc_E02")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E1C")

    def lambda_E14():
        TurnDirection(0x3, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_E14)

    label("loc_E1C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E36")

    def lambda_E2E():
        TurnDirection(0x4, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x4, 1, lambda_E2E)

    label("loc_E36")

    TurnDirection(0x0, 0xB, 400)
    Sleep(800)
    OP_4A(0xB, 255)
    OP_62(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x101, 400)
    Sleep(400)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #51
        0xB,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #52
        0x101,
        "#004FA...cat?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #53
        0xFE,
        (
            "I DID say that I wasn't sure\x01",
            "it would actually help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        "#018FThat you did.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #55
        0x107,
        (
            "#063FB-But Antoine's a really\x01",
            "smart cat.\x02\x03",

            "He might remember who\x01",
            "took the cigarettes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Indeed. If you bring him along\x01",
            "in your search, he might provide\x01",
            "you with a useful clue.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        (
            "He may not have as good a\x01",
            "sense of smell as a dog, but\x01",
            "it's still quite impressive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        "#000FThat's the hope, anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "If you bring along some Fresh\x01",
            "Milk, I'm sure he'll be more\x01",
            "than happy to follow you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "In light of the lack of other\x01",
            "clues, I'd like to try.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #61
        0x101,
        "#000FSure, it can't hurt.\x02",
    )

    CloseMessageWindow()

    def lambda_112C():
        TurnDirection(0x107, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_112C)
    TurnDirection(0x102, 0xFE, 400)

    ChrTalk(    #62
        0x102,
        (
            "#010FIf we find anything of note,\x01",
            "we'll be back to let you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "I'll be waiting. Whoever did\x01",
            "this absolutely must be caught.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x2C, 0x4, 0x8)
    OP_28(0x2C, 0x4, 0x4)
    OP_28(0x2C, 0x1, 0x1)
    OP_28(0x2C, 0x1, 0x2)
    OP_28(0x2C, 0x1, 0x4)
    ClearChrFlags(0xFE, 0x10)

    def lambda_11EA():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EA)
    EventEnd(0x0)
    OP_4B(0xB, 255)
    Return()

    # Function_2_AC end

    def Function_3_11F9(): pass

    label("Function_3_11F9")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "[Give Antoine the Fresh Milk]\x01",      # 0
            "[Cancel]\x01",                           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1265")
    Return()

    label("loc_1265")

    OP_3F(0x38A, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DB")

    ChrTalk(    #64
        0x101,
        (
            "#507FHere you go, Antoine.\x01",
            "Some nummy milk.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #65
        0xFE,
        "Nyaa～～o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C8")

    label("loc_12DB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1351")

    ChrTalk(    #66
        0x102,
        (
            "#019FAntoine... Here's some\x01",
            "milk for you, buddy.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #67
        0xFE,
        "Nyaa～～o.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C8")

    label("loc_1351")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C8")

    ChrTalk(    #68
        0x107,
        (
            "#066FHeeere, Antoine. I brought\x01",
            "you some miiiiilk...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(800)
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #69
        0xFE,
        "Nyaa～～o.\x02",
    )

    CloseMessageWindow()

    label("loc_13C8")

    Fade(1000)
    SetChrFlags(0xB, 0x80)
    AddParty(0x3B, 0xFF)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_3_11F9 end

    def Function_4_13DA(): pass

    label("Function_4_13DA")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3B)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F2")
    RemoveParty(0x3B, 0xFF)
    ClearChrFlags(0xB, 0x80)

    label("loc_13F2")

    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    OP_4A(0x8, 0)
    OP_6D(-6080, 0, 7020, 0)
    OP_6C(16000, 0)
    SetChrPos(0x8, -6740, 0, 7040, 135)
    SetChrPos(0xD, -5840, 0, 6240, 315)
    SetChrPos(0xB, -7340, 0, 6050, 130)
    SetChrPos(0x101, -4730, 0, 6330, 225)
    SetChrPos(0x102, -5570, 0, 5260, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_148E")
    SetChrPos(0x107, -4620, 0, 5220, 324)

    label("loc_148E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AD")
    SetChrPos(0x106, -3390, 0, 6350, 267)

    label("loc_14AD")

    OP_0D()
    Sleep(800)

    ChrTalk(    #70
        0x8,
        "I have to say, I'm simply amazed.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x8,
        (
            "I never would have suspected\x01",
            "YOU, of all people.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xD,
        (
            "#805F#4PI... I'm sorry.\x02\x03",

            "I just needed a smoke.\x02\x03",

            "I can't really explain it any\x01",
            "other way than saying that the\x01",
            "craving got the better of me.\x02\x03",

            "#803FDr. Miriam...\x01",
            "I really am sorry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x8,
        "Mr. Murdock...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x8,
        (
            "You know perfectly well that\x01",
            "the rule has been in place\x01",
            "for quite some time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xD,
        (
            "#802F#4PY-You're right.\x02\x03",

            "Coming up on ten years now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#004FHuh? Oh, yeah...\x02\x03",

            "So where did this sudden,\x01",
            "uncontrollable urge come\x01",
            "from, then?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xD, 45, 400)

    ChrTalk(    #77
        0xD,
        (
            "#806F#3PHonestly, I'm not so sure myself.\x02\x03",

            "After we had that orbal power\x01",
            "outage, I've heard no end of\x01",
            "complaints from the townsfolk...\x02\x03",

            "I guess that it just got to be\x01",
            "too much, and I needed a smoke\x01",
            "to help cool me down.\x02\x03",

            "*sigh*...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x8, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(120)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x107, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #78
        0x107,
        (
            "#065FMr. Murdock...\x02\x03",

            "#561FI-I'm sorry... This is all because\x01",
            "of what Grandpa and I did...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8C(0xD, 135, 400)

    ChrTalk(    #79
        0xD,
        (
            "#805F#3PNo, no, Tita. You haven't\x01",
            "done anything wrong, so\x01",
            "don't apologize.\x02\x03",

            "This doesn't really even have\x01",
            "anything to do with the professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        (
            "#003FMaybe you should take a little\x01",
            "break or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x102,
        (
            "#017FIt seems to me that this was\x01",
            "all because of too much stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x8,
        (
            "I do understand your situation,\x01",
            "Mr. Murdock.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x8,
        (
            "I think that I'm willing to\x01",
            "forgive and forget, in this\x01",
            "case.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)
    OP_8C(0xD, 315, 400)

    ChrTalk(    #84
        0xD,
        "#802F#4PWha...? R-Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x8,
        (
            "Instead... I'm going to insist\x01",
            "that you take a decent break.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x8,
        (
            "You're just going to ruin your\x01",
            "health, if you go on like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0xD,
        (
            "#806F#4PYou're right...\x02\x03",

            "#806FOnce things settle down a little\x01",
            "bit, I'll plan on using some of\x01",
            "my vacation time.\x02\x03",

            "#803FI'm still sorry for this whole\x01",
            "mess, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        "It's water under the bridge.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x8,
        "You need to focus on your health.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xD,
        "#800F#4PI will.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 135, 400)

    ChrTalk(    #91
        0xD,
        "#800F#3PI guess I'll be going now...\x02",
    )

    CloseMessageWindow()

    def lambda_1C25():

        label("loc_1C25")

        TurnDirection(0x8, 0xD, 0)
        OP_48()
        Jump("loc_1C25")

    QueueWorkItem2(0x8, 1, lambda_1C25)

    def lambda_1C36():

        label("loc_1C36")

        TurnDirection(0x101, 0xD, 0)
        OP_48()
        Jump("loc_1C36")

    QueueWorkItem2(0x101, 1, lambda_1C36)

    def lambda_1C47():

        label("loc_1C47")

        TurnDirection(0x102, 0xD, 0)
        OP_48()
        Jump("loc_1C47")

    QueueWorkItem2(0x102, 1, lambda_1C47)

    def lambda_1C58():

        label("loc_1C58")

        TurnDirection(0x107, 0xD, 0)
        OP_48()
        Jump("loc_1C58")

    QueueWorkItem2(0x107, 1, lambda_1C58)
    SetChrFlags(0xD, 0x40)
    OP_8E(0xD, 0xFFFFE6B0, 0x0, 0x13A6, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFE804, 0x0, 0x7BC, 0xBB8, 0x0)
    OP_8E(0xD, 0xFFFFF42A, 0x0, 0x2EE, 0xBB8, 0x0)
    OP_44(0x8, 0x1)
    OP_44(0x101, 0x1)
    OP_44(0x102, 0x1)
    OP_44(0x107, 0x1)
    OP_8E(0xD, 0xFFFFFECA, 0x0, 0x3B6, 0xBB8, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    Sleep(800)
    OP_22(0x6D, 0x0, 0x64)

    def lambda_1CE7():
        TurnDirection(0x101, 0x8, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CE7)

    def lambda_1CF5():
        OP_8C(0x102, 315, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1CF5)

    def lambda_1D03():
        OP_8C(0x107, 315, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1D03)
    OP_8C(0x8, 135, 400)
    Sleep(400)

    ChrTalk(    #92
        0x101,
        (
            "#007FWhew...\x01",
            "That's kinda sad.\x02\x03",

            "It's not like he was trying to\x01",
            "cause any trouble or anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x102,
        (
            "#010FBe that as it may, the factory\x01",
            "is still his responsibility.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x8,
        "Well, that much is true.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x8,
        (
            "...Now, I really must thank\x01",
            "you all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        "You've handled this case brilliantly.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        (
            "#001FYou're welcome.\x02\x03",

            "#000FI think half the credit has\x01",
            "to go to Antoine, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x107,
        "#061FHee hee. Yeah, no kidding.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x8,
        (
            "Ha ha. I'm glad my suggestion\x01",
            "bore fruit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x8,
        (
            "I trust you'll be nice to him\x01",
            "if you should meet again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x101,
        "#006FOf course!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x8,
        (
            "Well, thank you again for\x01",
            "your help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0x8,
        (
            "I'll be certain to call upon you\x01",
            "again, should another incident\x01",
            "arise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        (
            "#010FGlad to help.\x02\x03",

            "I think we'll be on our way, then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x101,
        "#000FSee you later.\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #106
        "\x07\x00Quest \x07\x02[Smoker's Revolt] \x07\x00completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0x8, 0)
    OP_28(0x2C, 0x4, 0x10)
    OP_28(0x2C, 0x1, 0x1000)
    OP_A2(0x3)
    EventEnd(0x0)
    Return()

    # Function_4_13DA end

    def Function_5_2069(): pass

    label("Function_5_2069")

    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #107
        "\x07\x00Found \x07\x02Kitty-Talk for Dummies\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x340, 1)
    SetChrFlags(0xE, 0x80)
    OP_64(0x0, 0x1)
    OP_28(0x2D, 0x1, 0x10)
    TalkEnd(0xFF)
    Return()

    # Function_5_2069 end

    SaveToFile()

Try(main)
