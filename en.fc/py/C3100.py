from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'C3100   ._SN',
        MapName             = 'Zeiss',
        Location            = 'C3100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60016",
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
        'Sentry',                               # 10
        'Sentry',                               # 11
        'Private Samuel',                       # 12
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
    )

    AddCharChipPat(
        'ED6_DT07/CH02450P._CP',             # 00
        'ED6_DT07/CH01640P._CP',             # 01
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3340,
        Z                   = 0,
        Y                   = -4720,
        Direction           = 174,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclEvent(
        X                   = -6310,
        Y                   = -1000,
        Z                   = -4980,
        Range               = 6020,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFDAC6,
        Unknown_18          = 0x0,
        Unknown_1C          = 5,
    )

    DeclEvent(
        X                   = 5480,
        Y                   = -1000,
        Z                   = -41450,
        Range               = -5800,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xFFFF61C2,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )

    DeclEvent(
        X                   = -5300,
        Y                   = -1000,
        Z                   = -7680,
        Range               = 5340,
        Unknown_10          = 0x7D0,
        Unknown_14          = 0xFFFFE94E,
        Unknown_18          = 0x0,
        Unknown_1C          = 7,
    )


    DeclActor(
        TriggerX            = 6000,
        TriggerZ            = 0,
        TriggerY            = -45540,
        TriggerRange        = 1500,
        ActorX              = 6000,
        ActorZ              = 1500,
        ActorY              = -45540,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1BE",          # 00, 0
        "Function_1_22B",          # 01, 1
        "Function_2_26D",          # 02, 2
        "Function_3_283",          # 03, 3
        "Function_4_830",          # 04, 4
        "Function_5_C22",          # 05, 5
        "Function_6_293F",         # 06, 6
        "Function_7_2B7F",         # 07, 7
        "Function_8_2C1A",         # 08, 8
    )


    def Function_0_1BE(): pass

    label("Function_0_1BE")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (100, "loc_1CA"),
        (SWITCH_DEFAULT, "loc_1E0"),
    )


    label("loc_1CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DD")
    OP_A2(0x55B)
    Event(0, 4)

    label("loc_1DD")

    Jump("loc_1E0")

    label("loc_1E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 0)), scpexpr(EXPR_END)), "loc_1EA")
    Jump("loc_22A")

    label("loc_1EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_205")
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    OP_8C(0xB, 90, 0)
    Jump("loc_22A")

    label("loc_205")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_END)), "loc_20F")
    Jump("loc_22A")

    label("loc_20F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_21E")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_22A")

    label("loc_21E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_22A")
    ClearChrFlags(0xB, 0x80)

    label("loc_22A")

    Return()

    # Function_0_1BE end

    def Function_1_22B(): pass

    label("Function_1_22B")

    OP_72(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_243")
    OP_6F(0x0, 310)

    label("loc_243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 2)), scpexpr(EXPR_END)), "loc_253")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x22), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_253")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x11C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_267")
    OP_28(0x2A, 0x1, 0x4000)

    label("loc_267")

    OP_22(0x1CD, 0x1, 0x64)
    Return()

    # Function_1_22B end

    def Function_2_26D(): pass

    label("Function_2_26D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_282")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_26D")

    label("loc_282")

    Return()

    # Function_2_26D end

    def Function_3_283(): pass

    label("Function_3_283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 7)), scpexpr(EXPR_END)), "loc_51E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_343")
    TalkBegin(0xFE)

    ChrTalk(    #0
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I formally refuse for the sake\x01",
            "of Major Cid...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "The major is a good man.\x01",
            "Intelligent, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "His only problem is that he's\x01",
            "probably too nice a guy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Jump("loc_51B")

    label("loc_343")

    TalkBegin(0xFE)
    OP_A2(0x0)

    ChrTalk(    #4
        0xFE,
        (
            "But still...the major's got things\x01",
            "pretty tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "Getting pushed around and\x01",
            "used by those guys in \x01",
            "Intelligence all the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "Being forthright is admirable,\x01",
            "but I think he should be more...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 400)
    Sleep(400)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #7
        0xFE,
        (
            "Hey, you! How long have you\x01",
            "been standing there?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Th-This area is strictly off-limits\x01",
            "to civilians!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Get out of here before I have\x01",
            "to arrest you!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xFE, 180, 0)
    OP_4B(0xFE, 255)
    ClearMapFlags(0x80)

    label("loc_51B")

    Jump("loc_82F")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 2)), scpexpr(EXPR_END)), "loc_747")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_598")

    ChrTalk(    #10
        0xFE,
        "...Hmm? S-Still here, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Get out of here! If you don't,\x01",
            "I swear I'll put you in the brig!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741")

    label("loc_598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6B0")
    OP_A2(0x1)

    ChrTalk(    #12
        0xFE,
        (
            "What's your problem? Do you\x01",
            "WANT to get arrested?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "You can't threaten me! This\x01",
            "area is crawling with our \x01",
            "secret Intelligence forces...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(800)

    ChrTalk(    #14
        0xFE,
        "Uh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        "(Crap.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        "...Ahem!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I'm afraid I must ask you to\x01",
            "vacate the premises.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_741")

    label("loc_6B0")

    OP_A2(0x0)

    ChrTalk(    #18
        0xFE,
        (
            "This is the Royal Army base\x01",
            "of Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Civilian access is prohibited.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "I insist that you leave this\x01",
            "area immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_741")

    TalkEnd(0xFE)
    Jump("loc_82F")

    label("loc_747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_82F")
    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_79B")

    ChrTalk(    #21
        0xFE,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Your persistence will get\x01",
            "you nowhere. Now, shoo!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82C")

    label("loc_79B")

    OP_A2(0x0)

    ChrTalk(    #23
        0xFE,
        (
            "This is the Royal Army base\x01",
            "of Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Civilian access is prohibited.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "I insist that you leave this\x01",
            "area immediately.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82C")

    TalkEnd(0xFE)

    label("loc_82F")

    Return()

    # Function_3_283 end

    def Function_4_830(): pass

    label("Function_4_830")

    EventBegin(0x0)
    SetChrPos(0x101, -50, 0, -57100, 0)
    SetChrPos(0x102, -1380, 0, -57730, 0)
    OP_6D(-240, -50, -54460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    StopSound(0x9470, 0x493E0, 0x1F40)

    def lambda_8A4():
        OP_6D(1220, 250, -12050, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8A4)

    def lambda_8BC():
        OP_67(0, 5140, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8BC)

    def lambda_8D4():
        OP_6B(8860, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8D4)

    def lambda_8E4():
        OP_6C(77000, 9000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8E4)
    Sleep(9000)
    Fade(1000)
    StopSound(0x9470, 0x1FBD0, 0x0)
    OP_6D(-240, -50, -54460, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(    #26
        0x101,
        (
            "#004FWow... Check out the\x01",
            "size of this base.\x02\x03",

            "It's gotta be several times\x01",
            "as big as the Haken Gate,\x01",
            "don't you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x102,
        (
            "#012FYeah...\x01",
            "You may be right.\x02\x03",

            "It was apparently the primary\x01",
            "base of the counteroffensive\x01",
            "in the war, ten years ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#006FOh, okay...\x01",
            "That's pretty impressive.\x02\x03",

            "Well, let's go inside and see\x01",
            "if we can talk to whoever's in\x01",
            "charge.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #29
        0x102,
        "#014F...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #30
        0x101,
        "#004F#2PWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        (
            "#010FNothing... It's just that you're\x01",
            "not acting like your usual, timid\x01",
            "self.\x02\x03",

            "You're starting to remind\x01",
            "me of Dad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#007F#2POh, come on. It's not\x01",
            "like I'm not nervous.\x02\x03",

            "But after General Morgan,\x01",
            "how bad can it be?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x102,
        (
            "#019FHa ha...\x01",
            "I guess you're right.\x02\x03",

            "#013FI wonder if he's still at the\x01",
            "Haken Gate...?\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x0)
    Return()

    # Function_4_830 end

    def Function_5_C22(): pass

    label("Function_5_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_293E")
    OP_A2(0x55C)
    OP_28(0x43, 0x1, 0x2)
    OP_28(0x43, 0x1, 0x4)
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -730, 250, -10440, 0)
    SetChrPos(0x102, 580, 250, -10420, 0)
    OP_6D(420, 1480, -5420, 0)
    OP_67(0, 6320, -20350, 0)
    OP_6B(1000, 0)
    OP_6E(611, 0)
    Sleep(1000)

    ChrTalk(    #34
        0x101,
        (
            "#004FHuh...\x01",
            "There's no one here...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#012FThat's strange...\x02\x03",

            "There's usually a gatekeeper\x01",
            "outside, at least.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("Man's Voice")

    AnonymousTalk(    #36
        "\x07\x05...Identify yourselves.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #37
        0x101,
        (
            "#004FUm...\x01",
            "Where'd that come from?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x102,
        "#012FProbably a speaker.\x02",
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #39
        (
            "This is Leiston Fortress, HQ of\x01",
            "Liberl's Royal Armed Forces.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #40
        "This place is off-limits to civilians.\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #41
        (
            "I'm afraid you're going to\x01",
            "have to leave.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #42
        0x101,
        (
            "#505F(Hmm...\x01",
            "They SOUND polite, but...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        (
            "#015F(Yeah... I think they're\x01",
            "just being extra-cautious.)\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #44
        (
            "*sigh*\x01",
            "Can you two hear me?\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #45
        0x101,
        (
            "#006FSorry, but we're not civilians.\x02\x03",

            "We're from the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x102,
        (
            "#010FWe're here to discuss the\x01",
            "matter of the central lab\x01",
            "being attacked.\x02\x03",

            "Could we please speak with\x01",
            "the individual in charge?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #47
        "Are you actual bracers, then?\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #48
        0x101,
        (
            "#006FIf you don't believe us, you\x01",
            "can inspect our emblems.\x02\x03",

            "You can see them, right?\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #49
        "...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #50
        (
            "Indeed. You appear to be\x01",
            "the genuine article.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #51
        (
            "However, I regret to inform\x01",
            "you that the C.O. of this\x01",
            "base is currently away.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #52
        (
            "Perhaps you can come\x01",
            "back another day.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #53
        0x101,
        (
            "#505FNo commanding officer?\x01",
            "Well, that sounds sloppy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x102,
        (
            "#010FIn that case, anyone from the\x01",
            "Intelligence Division will be fine.\x02\x03",

            "We have information that must\x01",
            "go to either Colonel Richard\x01",
            "or Captain Amalthea.\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("Man's Voice")

    AnonymousTalk(    #55
        "...\x02",
    )

    CloseMessageWindow()

    AnonymousTalk(    #56
        "Very well. Wait there.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Sleep(500)

    ChrTalk(    #57
        0x101,
        (
            "#007FWhew... It's like pulling\x01",
            "teeth with these guys.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x102,
        (
            "#012FYeah...I wasn't expecting security\x01",
            "to be quite THIS tight here.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(72, 320, 56, 3)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 40, 0, 3860, 180)
    SetChrPos(0x9, -760, 160, 4180, 180)
    SetChrPos(0xA, 900, 160, 4180, 180)
    OP_4A(0x9, 0)
    OP_4A(0xA, 0)
    OP_72(0x0, 0x10)
    OP_70(0x0, 0x1C2)
    Sleep(1000)

    ChrTalk(    #59
        0x101,
        "#004FWhoa!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x102,
        "#012FWell, someone's here at least...\x02",
    )

    CloseMessageWindow()

    def lambda_1357():
        OP_67(0, 12570, -20350, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1357)
    OP_6C(0, 8000)
    OP_73(0x0)

    def lambda_137B():
        OP_8E(0xFE, 0xFFFFFF92, 0xD2, 0xFFFFE37C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_137B)
    Sleep(500)

    def lambda_139B():
        OP_8E(0xFE, 0xFFFFFC54, 0xAA, 0xFFFFE728, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_139B)

    def lambda_13B6():
        OP_8E(0xFE, 0x316, 0xAA, 0xFFFFE714, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_13B6)

    def lambda_13D1():
        OP_6D(-150, 190, -6720, 5000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13D1)

    def lambda_13E9():
        OP_6B(850, 5000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13E9)
    WaitChrThread(0x8, 0x1)
    Sleep(500)

    ChrTalk(    #61
        0x8,
        (
            "#700F#6PPlease, forgive me\x01",
            "for making you wait.\x02\x03",

            "I am Major Cid, Garrison Commander\x01",
            "of Leiston Fortress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#006FI'm Estelle Bright,\x01",
            "of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        (
            "#010FAnd I'm Joshua Bright, also\x01",
            "of the Bracer Guild.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x8,
        "#702F#6PBright...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        "#004FIs something wrong?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x8,
        (
            "#703F#6PN-Nothing... Pardon me.\x02\x03",

            "#701FOn to business. You mentioned\x01",
            "the attack on the central labs?\x02\x03",

            "I'm very sorry...but no one\x01",
            "from the Intelligence Division\x01",
            "is currently here.\x02\x03",

            "If you'd have a message,\x01",
            "I can deliver it for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x101,
        (
            "#007FHmmm...\x01",
            "That could be a problem.\x02\x03",

            "#006F(Okay...\x01",
            "Time to shake things up...)\x02",
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
            "[We caught the people who attacked the lab.]\x01",             # 0
            "[We've confirmed the whereabouts of Prof. Russell.]\x01",      # 1
            "[We have a lead on an airship tied to the crime.]\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1739"),
        (1, "loc_18A5"),
        (2, "loc_1A0D"),
        (SWITCH_DEFAULT, "loc_1AD0"),
    )


    label("loc_1739")


    ChrTalk(    #68
        0x101,
        (
            "#007F*sigh* And here we caught the\x01",
            "people who attacked the lab.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #69
        0x8,
        "#702F#6PYou what?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #70
        0x102,
        (
            "#019FWay to not jump the gun, Estelle.\x02\x03",

            "The only clue we have is\x01",
            "that the professor was taken\x01",
            "away in an airship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #71
        0x101,
        (
            "#001FAh...ha ha...\x01",
            "Sorry... My mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x8,
        "#700F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #73
        0x101,
        "#006FWhy so quiet, Major?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD0")

    label("loc_18A5")


    ChrTalk(    #74
        0x101,
        (
            "#007F*sigh* And here we found out\x01",
            "where Professor Russell is...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #75
        0x8,
        "#702F#6PYou what?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #76
        0x102,
        (
            "#019FNice, Estelle. Really subtle.\x02\x03",

            "The only clue we have is\x01",
            "that the professor was taken\x01",
            "away in an airship.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #77
        0x101,
        (
            "#001FAh...ha ha...\x01",
            "Sorry... My mistake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x8,
        "#700F#6P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x8, 400)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #79
        0x101,
        "#006FWhy so quiet, Major?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AD0")

    label("loc_1A0D")


    ChrTalk(    #80
        0x101,
        (
            "#007F*sigh* And here we found a\x01",
            "lead on the airship that took\x01",
            "away the professor.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #81
        0x8,
        "#702F#6PYou what?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#006FWhat? Why do you look\x01",
            "so surprised, Major?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AD0")

    label("loc_1AD0")


    ChrTalk(    #83
        0x8,
        (
            "#701F#6POh... I-It's nothing. We've just\x01",
            "been searching for it, too.\x02\x03",

            "So...what is this lead, anyway?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x102,
        "#012FTake a look at this...\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0xD2, 0xFA, 0xFFFFDF94, 0xBB8, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #85
        "\x07\x00Handed over \x07\x02Dorothy's Photograph\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3F(0x358, 1)
    OP_8F(0x102, 0x1F4, 0xFA, 0xFFFFDD6E, 0x7D0, 0x0)

    ChrTalk(    #86
        0x8,
        (
            "#702F#6PThis... This is Leiston Fortress,\x01",
            "isn't it?\x02\x03",

            "How did you get this picture...?\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0xFFFFFDA8, 0xF0, 0xFFFFE174, 0xBB8, 0x0)
    TurnDirection(0x101, 0x8, 400)

    ChrTalk(    #87
        0x101,
        (
            "#006FNow, now...\x01",
            "No need to get worked up.\x02\x03",

            "Look at the top-right\x01",
            "corner of that picture.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0x8,
        "#700F#6PLet's see...\x02",
    )

    CloseMessageWindow()
    OP_62(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #89
        0x8,
        "#704F#6PWhat the...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x102,
        (
            "#010FThat's obviously not the\x01",
            "silhouette of a military\x01",
            "patrol ship, is it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x101,
        (
            "#507FAnd it's the spitting image of\x01",
            "the airship that took away the\x01",
            "professor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x8,
        (
            "#700F#6P...\x02\x03",

            "#703FIndeed...this is a grave matter.\x02\x03",

            "Thank you for your cooperation. I'll\x01",
            "send a report to the Intelligence\x01",
            "Division straight away.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x101,
        (
            "#004FHuh...?\x02\x03",

            "Hey, wait a minute!\x01",
            "Is that it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #94
        0x8,
        "#702F#4PIs what it?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_8F(0x101, 0xFFFFFD30, 0xFA, 0xFFFFDF12, 0x7D0, 0x0)

    ChrTalk(    #95
        0x101,
        (
            "#009FI mean...\x01",
            "Don't you think this is weird?\x02\x03",

            "Why would the suspects' ship\x01",
            "be hanging around HERE?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x8,
        (
            "#703F#4PIt's embarrassing to admit, but I'm afraid\x01",
            "that it's entirely my fault.\x02\x03",

            "We have been aggressively searching along\x01",
            "the border, so security wasn't as tight\x01",
            "at home as it should have been then.\x02\x03",

            "And if this airship fled to the north,\x01",
            "it's possible that this whole matter\x01",
            "may have been a plot by the Empire.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x101,
        "#505FR-Really...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x102,
        (
            "#013F...\x02\x03",

            "#010FI'd like to know just one thing.\x02\x03",

            "Where, exactly, ARE all of the\x01",
            "intelligence personnel right now?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x102, 400)

    ChrTalk(    #99
        0x8,
        (
            "#700F#6P...\x02\x03",

            "#703FThat's classified.\x02\x03",

            "I'm sorry I can't say more.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2145():

        label("loc_2145")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2145")

    QueueWorkItem2(0x9, 1, lambda_2145)

    def lambda_2156():

        label("loc_2156")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_2156")

    QueueWorkItem2(0xA, 1, lambda_2156)
    OP_8C(0x8, 0, 400)

    def lambda_216E():
        OP_8E(0xFE, 0x28, 0x0, 0xF14, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_216E)
    Sleep(1000)

    def lambda_218E():
        OP_8E(0xFE, 0xFFFFFD08, 0xA0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_218E)

    def lambda_21A9():
        OP_8E(0xFE, 0x384, 0xA0, 0x1054, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_21A9)
    Sleep(2000)

    def lambda_21C9():
        OP_67(0, 18220, -20350, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21C9)

    def lambda_21E1():
        OP_6E(489, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_21E1)
    Sleep(4000)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #100
        0x101,
        (
            "#009FOkay now... Maybe it's just me...\x02\x03",

            "...but don't you think this all\x01",
            "kinda smells a little funny?\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #101
        0x102,
        (
            "#013FI know...\x02\x03",

            "But without any concrete\x01",
            "evidence, pursuing this\x01",
            "lead won't do us any good.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        "#003FYeah...\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(1000)
    OP_6D(-770, 1700, -3300, 0)
    OP_67(0, 5430, -10000, 0)
    OP_6B(4880, 0)
    OP_6C(339000, 0)
    OP_6E(262, 0)
    OP_72(0x0, 0x800)
    OP_22(0x6C, 0x0, 0x64)
    OP_6F(0x0, 450)
    OP_70(0x0, 0x136)
    OP_73(0x0)
    OP_22(0x9A, 0x0, 0x64)
    OP_23(0x6C)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    TurnDirection(0x101, 0x8, 400)
    TurnDirection(0x102, 0x8, 400)
    Sleep(500)
    OP_71(0x0, 0x800)

    ChrTalk(    #103
        0x101,
        "#004FHuh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x102,
        "#014FWhat the...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #105
        0x8,
        "Major Cid",
        (
            "Wh-What...?\x01",
            "Why did it stop short?\x02\x03",

            "...\x02\x03",

            "What...?\x02\x03",

            "Did that phenomenon start\x01",
            "up again?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #106
        0x101,
        "#005F(Joshua, that's...!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0x102,
        (
            "#012F(Yeah, I think that's exactly\x01",
            "what we needed.)\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0x8, 1280, 0, 3540, 0)
    SetChrPos(0x9, 1280, 0, 3540, 0)
    SetChrPos(0xA, 1280, 0, 3540, 0)

    def lambda_24EB():

        label("loc_24EB")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_24EB")

    QueueWorkItem2(0x101, 3, lambda_24EB)

    def lambda_24FC():

        label("loc_24FC")

        TurnDirection(0xFE, 0x8, 0)
        OP_48()
        Jump("loc_24FC")

    QueueWorkItem2(0x102, 3, lambda_24FC)

    def lambda_250D():
        OP_6D(-120, 180, -6630, 3000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_250D)

    def lambda_2525():
        OP_6B(4090, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2525)

    def lambda_2535():
        OP_8E(0xFE, 0xFFFFFF38, 0xAA, 0xFFFFE6BA, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2535)
    Sleep(500)

    def lambda_2555():
        OP_8E(0xFE, 0xFFFFFC0E, 0x0, 0xFFFFEBD8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2555)
    Sleep(500)

    def lambda_2575():
        OP_8E(0xFE, 0x3DE, 0x0, 0xFFFFECD2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2575)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #108
        0x8,
        (
            "#701F#4PI-It seems I've let you\x01",
            "see us at our worst.\x02\x03",

            "It looks like the gate mechanism\x01",
            "isn't in the best of conditions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#019FIndeed...\x01",
            "That's a real problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#006FMaybe you could get some\x01",
            "folks from the central\x01",
            "labs out to repair it?\x02\x03",

            "I'll bet that someone like\x01",
            "Professor Russell could have it\x01",
            "good as new in no time flat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#701F#4PY-Yes.\x01",
            "I'll keep that in mind.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    ChrTalk(    #112
        0x8,
        (
            "#704FYou two maintain post here until\x01",
            "it's back in working order.\x02\x03",

            "Be sure to keep any careless\x01",
            "civilians away.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 400)

    ChrTalk(    #113
        0x9,
        "Sir! Yes, sir!\x02",
    )

    CloseMessageWindow()

    def lambda_27AA():
        OP_8E(0xFE, 0xFFFFF254, 0x0, 0xFFFFED18, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_27AA)

    def lambda_27C5():

        label("loc_27C5")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_27C5")

    QueueWorkItem2(0x9, 1, lambda_27C5)

    ChrTalk(    #114
        0xA,
        "Understood, sir!\x02",
    )

    CloseMessageWindow()

    def lambda_27EC():
        OP_8E(0xFE, 0xEA6, 0x0, 0xFFFFEBE2, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_27EC)

    def lambda_2807():

        label("loc_2807")

        OP_8C(0xFE, 180, 400)
        OP_48()
        Jump("loc_2807")

    QueueWorkItem2(0xA, 1, lambda_2807)
    Sleep(1000)
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #115
        0x8,
        (
            "#701F#4PThat said, you two can\x01",
            "be on your way.\x02\x03",

            "I'll be certain to take that\x01",
            "photograph to Intelligence.\x02\x03",

            "Now, if you'll pardon me.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 0, 400)

    def lambda_28B4():
        OP_6D(-220, 250, -8550, 5000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_28B4)

    def lambda_28CC():
        OP_67(0, 9500, -10000, 5000)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_28CC)

    def lambda_28E4():
        OP_6C(45000, 5000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_28E4)

    def lambda_28F4():
        OP_6B(2800, 5000)
        ExitThread()

    QueueWorkItem(0x1, 3, lambda_28F4)

    def lambda_2904():
        OP_8E(0xFE, 0x4EC, 0xFA, 0xD48, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2904)
    WaitChrThread(0x0, 0x2)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    EventEnd(0x0)
    OP_85(0x9)
    OP_85(0xA)
    OP_4B(0x9, 0)
    OP_4B(0xA, 0)

    label("loc_293E")

    Return()

    # Function_5_C22 end

    def Function_6_293F(): pass

    label("Function_6_293F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B7E")
    OP_A2(0x55D)
    OP_28(0x43, 0x1, 0x8)
    OP_28(0x43, 0x1, 0x10)
    EventBegin(0x0)
    TurnDirection(0x102, 0x101, 400)
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #116
        0x101,
        (
            "#002FSomehow I find it hard to believe\x01",
            "a word that guy said...\x02\x03",

            "Especially if that little malfunction\x01",
            "we just saw is what I think it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x102,
        (
            "#015FYes...it was probably that\x01",
            "same phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#505FWhich would mean...\x02\x03",

            "#005FThe professor is being held\x01",
            "prisoner inside!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0x102,
        (
            "#012F(Shh, Estelle!)\x02\x03",

            "(This isn't the place \x01",
            "to be discussing that.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x101,
        "#004F(O-Okay...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x102,
        (
            "#013F(For now, let's get back \x01",
            "to Zeiss and see what \x01",
            "Kilika has to say.)\x02\x03",

            "(If we have the chance, we\x01",
            "can call for the lab chief.)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x3FA)
    NewScene("ED6_DT01/T3120   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_2B7E")

    Return()

    # Function_6_293F end

    def Function_7_2B7F(): pass

    label("Function_7_2B7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C19")
    EventBegin(0x1)
    OP_4A(0x9, 0)
    OP_4A(0xA, 0)
    TurnDirection(0x9, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    ChrTalk(    #122
        0x9,
        (
            "You heard the man.\x01",
            "This area's off limits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xA,
        "Be on your way.\x02",
    )

    CloseMessageWindow()
    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    OP_8C(0x9, 180, 0)
    OP_8C(0xA, 180, 0)
    OP_4B(0x9, 0)
    OP_4B(0xA, 0)

    label("loc_2C19")

    Return()

    # Function_7_2B7F end

    def Function_8_2C1A(): pass

    label("Function_8_2C1A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #124
        (
            "\x07\x05      -WARNING-\x01",
            "No photography allowed\x01",
            " on military property.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_2C1A end

    SaveToFile()

Try(main)
