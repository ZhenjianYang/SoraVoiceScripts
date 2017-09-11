from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3106   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3106.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
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
        'Major Cid',                            # 9
        'Soldier',                              # 10
        'Soldier',                              # 11
        'Natl Guard Officer',                   # 12
        'Soldier',                              # 13
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
        'ED6_DT07/CH02450 ._CH',             # 00
        'ED6_DT07/CH01640 ._CH',             # 01
        'ED6_DT07/CH01310 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
        'ED6_DT07/CH01310P._CP',             # 02
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
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = 16500,
        TriggerZ            = 0,
        TriggerY            = 42000,
        TriggerRange        = 800,
        ActorX              = 16500,
        ActorZ              = 1000,
        ActorY              = 42000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -12960,
        TriggerZ            = 0,
        TriggerY            = 34480,
        TriggerRange        = 1000,
        ActorX              = -12960,
        ActorZ              = 1000,
        ActorY              = 34480,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AA",          # 00, 0
        "Function_1_1C6",          # 01, 1
        "Function_2_226",          # 02, 2
        "Function_3_1821",         # 03, 3
        "Function_4_192B",         # 04, 4
    )


    def Function_0_1AA(): pass

    label("Function_0_1AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7F, 2)), scpexpr(EXPR_END)), "loc_1C5")
    SetMapFlags(0x40000000)
    AddParty(0xFF, 0xFF)
    SetMapFlags(0x10000000)
    OP_A3(0x3FA)
    Event(0, 2)

    label("loc_1C5")

    Return()

    # Function_0_1AA end

    def Function_1_1C6(): pass

    label("Function_1_1C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 1)), scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1DC")
    OP_65(0x0, 0x1)

    label("loc_1DC")

    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_1_1C6 end

    def Function_2_226(): pass

    label("Function_2_226")

    ClearMapFlags(0x10000000)
    SetChrPos(0x0, -10080, 0, 27870, 0)
    SetChrPos(0x1, -10080, 0, 27870, 0)
    SetChrPos(0x2, -10080, 0, 27870, 0)
    SetChrPos(0x3, -10080, 0, 27870, 0)
    EventBegin(0x0)
    OP_6D(-1220, 0, 23900, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4460, 0)
    OP_6C(67000, 0)
    OP_6E(423, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrPos(0x8, -11370, 0, 21640, 270)
    SetChrPos(0x9, -13090, 0, 22310, 90)
    SetChrPos(0xA, -13360, 0, 21070, 90)

    def lambda_305():
        OP_6C(45000, 8000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_305)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_31F():
        OP_6E(262, 6000)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_31F)

    def lambda_32F():
        OP_6B(3250, 6000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_32F)
    OP_6D(-12330, 0, 21630, 6000)

    ChrTalk(    #0
        0x8,
        (
            "#701FI appreciate your efforts.\x02\x03",

            "We'll bring the containers in\x01",
            "tomorrow, so you can return\x01",
            "to the barracks for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x9,
        "P-Pardon me, Major...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x9,
        (
            "...but how long is the current\x01",
            "emergency command structure\x01",
            "expected to last?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x8,
        "#700F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xA,
        "Th-That's right!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xA,
        (
            "We're army, sir. Why do we\x01",
            "have to associate with them?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "#703FIt's not that I don't understand\x01",
            "what you're getting at...\x02\x03",

            "But it is not the place of a\x01",
            "soldier to question the orders\x01",
            "of a superior officer.\x02\x03",

            "#701FBesides, you never know who's\x01",
            "watching or listening.\x02\x03",

            "Discretion is a must\x01",
            "at all times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x9,
        "Yes, sir...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xA,
        "Understood, sir.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 270, 400)

    def lambda_5BD():
        OP_8E(0xFE, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5BD)
    Sleep(100)
    OP_8C(0x9, 270, 400)
    OP_8E(0x9, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)

    ChrTalk(    #9
        0x8,
        (
            "#703F*sigh*\x01",
            "I feel guilty...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -22160, 0, 22550, 0)
    ClearChrFlags(0xB, 0x80)

    def lambda_63A():

        label("loc_63A")

        TurnDirection(0xFE, 0xB, 0)
        OP_48()
        Jump("loc_63A")

    QueueWorkItem2(0x8, 1, lambda_63A)
    OP_8E(0xB, 0xFFFFCC34, 0x0, 0x591A, 0xFA0, 0x0)
    TurnDirection(0xB, 0x8, 400)

    ChrTalk(    #10
        0xB,
        "#3PMajor, I have intel to report!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xB,
        (
            "Captain Amalthea has come and\x01",
            "wishes to speak with you, sir.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "#700FI see... Very well.\x02\x03",

            "#703FI suppose I'll have to see what\x01",
            "the little vixen has to say.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_730():

        label("loc_730")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_730")

    QueueWorkItem2(0xB, 1, lambda_730)

    def lambda_741():
        OP_8E(0xFE, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_741)
    Sleep(1000)
    OP_8E(0xB, 0xFFFFA970, 0x0, 0x5816, 0xBB8, 0x0)
    OP_6D(-9480, 0, 27600, 5000)
    OP_22(0xA9, 0x0, 0x64)
    OP_B0(0x12, 0x78)
    OP_70(0x12, 0xB4)
    OP_73(0x12)
    Sleep(500)

    def lambda_79E():
        OP_6D(-7220, 0, 27280, 7000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_79E)

    def lambda_7B6():
        OP_6C(21000, 7000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_7B6)

    def lambda_7C6():
        OP_6B(2800, 7000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7C6)
    SetChrFlags(0x106, 0x4)
    SetChrFlags(0x107, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    OP_8E(0x106, 0xFFFFE3FE, 0x0, 0x6E3C, 0xBB8, 0x0)
    OP_8C(0x106, 156, 400)
    OP_8E(0x107, 0xFFFFE7B4, 0x0, 0x6AAE, 0xBB8, 0x0)
    OP_8C(0x107, 304, 400)
    OP_8E(0x101, 0xFFFFE494, 0x0, 0x67D4, 0xBB8, 0x0)
    OP_8C(0x101, 342, 400)
    OP_8E(0x102, 0xFFFFE0DE, 0x0, 0x69BE, 0xBB8, 0x0)
    OP_8C(0x102, 71, 400)
    ClearChrFlags(0x106, 0x4)
    ClearChrFlags(0x107, 0x4)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    WaitChrThread(0x101, 0x2)

    ChrTalk(    #13
        0x101,
        (
            "#007FWhew... Uggh...I can't feel my\x01",
            "legs anymore...\x02\x03",

            "#008FYou okay, Tita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x107,
        (
            "#066FYeah... Just a little fuzzy \x01",
            "in the head, is all...\x02\x03",

            "But I'm glad we got the\x01",
            "equipment to work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        (
            "#053FYeah, nice job.\x02\x03",

            "#051FIt was a tight situation, literally,\x01",
            "but you stepped up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x107,
        (
            "#067FHee hee...\x01",
            "Thank you, Agate.\x02\x03",

            "But Antoine showing up like that really spooked\x01",
            "me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#007FYeah, he was right in the\x01",
            "next container over.\x02\x03",

            "I thought we'd be discovered\x01",
            "for sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#010FI think the chief put him in\x01",
            "there on purpose.\x02\x03",

            "That false alarm got the\x01",
            "soldiers to relax.\x02\x03",

            "He kept a cool head, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x107,
        (
            "#560FHehe... that does sound like something\x01",
            "the chief would do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x106,
        (
            "#051FDefinitely a man not to\x01",
            "mess with.\x02\x03",

            "Now...\x01",
            "We ought to get moving.\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x40025, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_77(0x0, 0x0, 0x0, 0x0, 0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #21
        (
            "\x07\x00#050FWe're somewhere close to\x01",
            "the airship port.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(500)
    OP_AD(0x4002C, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #22
        (
            "#050FWe need a plan, or else we'll\x01",
            "never find the professor.\x02\x03",

            "So, Estelle... Check the map and\x01",
            "tell me which way we should go.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #23
        (
            "#004FHuh?\x01",
            "Wh-Why are you asking me?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #24
        (
            "#051FCall it a test of how observant\x01",
            "you are.\x02\x03",

            "Time's short, so let's have\x01",
            "your answer.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        12,
        12,
        0,
        (
            "[Barracks, to the southwest]\x01",         # 0
            "[Command Center, in the middle]\x01",      # 1
            "[Research Wing, in the middle]\x01",       # 2
            "[Watchtower, in the northeast]\x01",       # 3
            "[Main Gate, to the south]\x01",            # 4
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_DE7"),
        (1, "loc_F95"),
        (2, "loc_10DD"),
        (3, "loc_1246"),
        (4, "loc_142B"),
        (SWITCH_DEFAULT, "loc_15AA"),
    )


    label("loc_DE7")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #25
        (
            "#053FNo good. Too many troops there.\x02\x03",

            "Think about where classified\x01",
            "info would likely be kept.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #26
        (
            "#007FHmmm...\x01",
            "Yeah, you're probably right.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #27
        "#050FWhat's your take, Joshua?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #28
        (
            "#012FI think the research facilities\x01",
            "would be our best bet.\x02\x03",

            "And since it's a standalone facility,\x01",
            "it'd probably be the best place to\x01",
            "make use of the professor's abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_F95")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #29
        (
            "#053FThere's a decent chance, but\x01",
            "I think we've got a better\x01",
            "shot elsewhere.\x02\x03",

            "#050FWhat's your take, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #30
        (
            "#012FI think the research facilities\x01",
            "would be our best bet.\x02\x03",

            "And since it's a standalone facility,\x01",
            "it'd probably be the best place to\x01",
            "make use of the professor's abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_10DD")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #31
        (
            "#052FWell, well.\x01",
            "Color me surprised.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #32
        "#502FHah! Just leave it to me.♪\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #33
        (
            "#551FGreat job, kid, but don't\x01",
            "get cocky.\x02\x03",

            "#050FWhat's your take, Joshua?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #34
        (
            "#012FI agree with her.\x02\x03",

            "Since it's a standalone facility,\x01",
            "it's probably the best place to make\x01",
            "use of the professor's talents.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_1246")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #35
        (
            "#552FI get what you're thinking... It does\x01",
            "seem a little suspicious, what with\x01",
            "all the people in and out constantly.\x02\x03",

            "#051FStill, I think we've got a\x01",
            "better shot somewhere else.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #36
        "#505FReally?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #37
        "#050FWhat's your take, Joshua?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #38
        (
            "#012FI think the research facilities\x01",
            "would be our best bet.\x02\x03",

            "And since it's a standalone facility,\x01",
            "it'd probably be the best place to\x01",
            "make use of the professor's abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_142B")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #39
        (
            "#551FThis is the fortress exit.\x01",
            "There's nowhere to keep\x01",
            "prisoners here.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #40
        "#007FOh, yeah...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #41
        "#050FWhat's your take, Joshua?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #42
        (
            "#012FI think the research facilities\x01",
            "would be our best bet.\x02\x03",

            "And since it's a standalone facility,\x01",
            "it'd probably be the best place to\x01",
            "make use of the professor's abilities.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_15AA")

    label("loc_15AA")

    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #43
        "#053FI think you're right.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(500)
    OP_AD(0x4002D, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #44
        (
            "#050FWe don't have much time,\x01",
            "so let's go check it out.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(150, 350, -1, -1)
    SetChrName("Joshua")

    AnonymousTalk(    #45
        (
            "#010FAgate, do we have an\x01",
            "exit strategy?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #46
        (
            "#052FOh, right.\x02\x03",

            "The lake on the other side of\x01",
            "the airship port has a wharf.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_AE(0x3E8)
    Sleep(500)
    OP_AD(0x4002E, 0x0, 0x0, 0x1F4)
    Sleep(1500)
    OP_3F(0x359, 1)
    OP_3E(0x35A, 1)
    SetMessageWindowPos(75, 300, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #47
        (
            "#050FOnce we get the old man, we\x01",
            "can steal a boat from there.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(400, 400, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #48
        "#002FOkay, got it.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #49
        0x101,
        (
            "#006FAll right, let's go check\x01",
            "out the research area.\x02\x03",

            "You stay close, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x107,
        "#062FO-Okay...!\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    EventEnd(0x0)
    Return()

    # Function_2_226 end

    def Function_3_1821(): pass

    label("Function_3_1821")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C1")
    OP_A2(0x0)

    ChrTalk(    #51
        0x106,
        (
            "#050FThese stairs lead down to\x01",
            "the wharf.\x02\x03",

            "We can use them to get out\x01",
            "of here when we come back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        "#006FUnderstood.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        "#012FRoger that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1927")

    label("loc_18C1")


    ChrTalk(    #54
        0x106,
        (
            "#050FThese stairs lead down to\x01",
            "the wharf.\x02\x03",

            "We can use them to get out\x01",
            "of here when we come back.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1927")

    TalkEnd(0xFF)
    Return()

    # Function_3_1821 end

    def Function_4_192B(): pass

    label("Function_4_192B")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #55
        "\x07\x05Orbment repair device installed.\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B3C")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, -12960, 1000, 34480, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_70(0x11, 0x32)
    OP_73(0x11)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x2, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0x0, 0xFE, 0x0)
    OP_31(0x1, 0xFE, 0x0)
    OP_31(0x2, 0xFE, 0x0)
    OP_31(0x3, 0xFE, 0x0)
    OP_31(0x4, 0xFE, 0x0)
    OP_31(0x5, 0xFE, 0x0)
    OP_31(0x6, 0xFE, 0x0)
    OP_31(0x7, 0xFE, 0x0)
    SetChrPos(0x0, -14350, 0, 33010, 39)
    SetChrPos(0x1, -14350, 0, 33010, 39)
    SetChrPos(0x2, -14350, 0, 33010, 39)
    SetChrPos(0x3, -14350, 0, 33010, 39)
    OP_69(0x0, 0x0)
    OP_30(0x0)
    Sleep(3500)
    OP_82(0x1, 0x2)
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, -12960, 1000, 34480, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x11, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B56")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_1B56")

    Return()

    # Function_4_192B end

    SaveToFile()

Try(main)
