from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3118   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3118.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 1,
        EntryFunctionIndex  = 0,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3118_1 ._SN',
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
        'Dr. Miriam',                           # 9
        'Antoine',                              # 10
        'Antoine',                              # 11
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
        'ED6_DT07/CH01430 ._CH',             # 00
        'ED6_DT07/CH01700 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01430P._CP',             # 00
        'ED6_DT07/CH01700P._CP',             # 01
    )

    DeclNpc(
        X                   = -1410,
        Z                   = 0,
        Y                   = 6690,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -5510,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -5510,
        Z                   = 0,
        Y                   = -3140,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -5510,
        TriggerZ            = 0,
        TriggerY            = -3140,
        TriggerRange        = 1000,
        ActorX              = -5510,
        ActorZ              = 500,
        ActorY              = -3140,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_13E",          # 00, 0
        "Function_1_16F",          # 01, 1
        "Function_2_19F",          # 02, 2
        "Function_3_200",          # 03, 3
        "Function_4_17D0",         # 04, 4
    )


    def Function_0_13E(): pass

    label("Function_0_13E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_15B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_158")
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_158")

    Jump("loc_16E")

    label("loc_15B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_16E")
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x0, 0x2)

    label("loc_16E")

    Return()

    # Function_0_13E end

    def Function_1_16F(): pass

    label("Function_1_16F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A")
    OP_6F(0x0, 29)
    OP_72(0x0, 0x10)
    OP_79(0xFF, 0x2)
    OP_7A(0x7, 0x2)
    OP_7B()
    OP_72(0x6, 0x4)
    OP_72(0x7, 0x4)

    label("loc_19A")

    OP_64(0x0, 0x1)
    Return()

    # Function_1_16F end

    def Function_2_19F(): pass

    label("Function_2_19F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FF")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x1, 0x400)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x8)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x6F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5")
    OP_8D(0xFE, -3860, -2270, -5240, -3760, 1000)
    Jump("loc_1FC")

    label("loc_1E5")

    OP_8D(0xFE, -6290, -6030, -3150, 520, 1000)

    label("loc_1FC")

    Jump("Function_2_19F")

    label("loc_1FF")

    Return()

    # Function_2_19F end

    def Function_3_200(): pass

    label("Function_3_200")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_76B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_601")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_292")
    TurnDirection(0xFE, 0x107, 0)

    ChrTalk(    #0
        0xFE,
        "Oh, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "And, Tita, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x107,
        "#560FHi, Dr. Miriam.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        "#1000FAhaha, it's been a while.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CA")

    label("loc_292")


    ChrTalk(    #4
        0xFE,
        "Oh, bracers...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        "#1000FYeah, it's been a while.\x02",
    )

    CloseMessageWindow()

    label("loc_2CA")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #6
        0xFE,
        "I'm glad to see you all look well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1000FYou too, Dr. Miriam.\x02\x03",

            "#1007FWell, I mean, aside from all the craziness\x01",
            "going on right now, anyway. I imagine\x01",
            "work's pretty tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "Yes, for now I'm checking over our\x01",
            "stocks of medical supplies.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "We'll be in deep trouble if we don't\x01",
            "have medicine when it's needed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x102,
        (
            "#1043FYeah...\x02\x03",

            "At the moment, it's not exactly easy to\x01",
            "restock with transportation so limited.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "Indeed. We'll just have to be very conservative\x01",
            "in our use of the supplies we do have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        "So, you all be careful too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "If you get hurt really badly and dragged in\x01",
            "here, I will give you an absolute earful.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C2")

    ChrTalk(    #14
        0x101,
        (
            "#1016FAhaha... We'll be careful.\x02\x03",

            "...Right, Agate?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x106,
        "#552FWhat're you looking at me for?\x02",
    )

    CloseMessageWindow()
    Jump("loc_5F8")

    label("loc_5C2")


    ChrTalk(    #16
        0x101,
        "#1016FAhaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x102,
        "#1035FWe'll be very careful.\x02",
    )

    CloseMessageWindow()

    label("loc_5F8")

    OP_A2(0x0)
    OP_A2(0x20D3)
    Jump("loc_768")

    label("loc_601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_6F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_684")

    ChrTalk(    #18
        0xFE,
        (
            "We'll just have to be very conservative\x01",
            "in our use of the supplies we do have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "You all be very careful.\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F3")

    label("loc_684")


    ChrTalk(    #20
        0xFE,
        (
            "Seems like it's the first time\x01",
            "I've seen Antoine in a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "Really, where was this kitty, I wonder.\x02",
    )

    CloseMessageWindow()

    label("loc_6F3")

    Jump("loc_768")

    label("loc_6F6")


    ChrTalk(    #22
        0xFE,
        (
            "We'll just have to be very conservative\x01",
            "in our use of the supplies we do have.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0xFE,
        "You all be very careful.\x02",
    )

    CloseMessageWindow()

    label("loc_768")

    Jump("loc_17CC")

    label("loc_76B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x285, 6)), scpexpr(EXPR_END)), "loc_F85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_9E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_882")

    ChrTalk(    #24
        0xFE,
        (
            "The priests of the Septian Church are\x01",
            "developing new medicines even now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "It's still a mystery how they can\x01",
            "innovate so much, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Reading this treatise I can accept it. Basically,\x01",
            "it seems like they've got some incredible people.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E3")

    label("loc_882")


    ChrTalk(    #27
        0xFE,
        (
            "A while back, I was reading a treatise in\x01",
            "a medicinal journal written by a priest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "And it was just...really impressive.\x01",
            "I admit to being a little shocked.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "For the church to not just have knowledge about\x01",
            "traditional medicine, but also modern medicine...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "I'd love to have the chance to talk in\x01",
            "depth with the writer, Father Divine.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_9E3")

    Jump("loc_F21")

    label("loc_9E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_BCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_A9C")

    ChrTalk(    #31
        0xFE,
        (
            "One of my recent research themes has\x01",
            "been analysis of medicines prescribed\x01",
            "by the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        (
            "If I can arrange what we know,\x01",
            "I'm sure I'll find something out.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCC")

    label("loc_A9C")


    ChrTalk(    #33
        0xFE,
        (
            "One of my recent research themes has\x01",
            "been analysis of medicines prescribed\x01",
            "by the church.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "I've had some results, such as I found their\x01",
            "shoulder pain medicine is constructed in\x01",
            "a pharmacological manner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "It's a very small first step, but building up\x01",
            "those is how we make new discoveries.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_BCC")

    Jump("loc_F21")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_DFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_CF5")

    ChrTalk(    #36
        0xFE,
        (
            "Modern medicine which medical scientists rely\x01",
            "upon as a foundation has a very short history.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "Surgical fields have had some success,\x01",
            "but our understanding of medicine is still\x01",
            "far from the church's.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "After all, they have over a thousand\x01",
            "years of experience on us.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DF9")

    label("loc_CF5")


    ChrTalk(    #39
        0xFE,
        (
            "There was that Septian Church medicine\x01",
            "that saved Agate, remember?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        (
            "It was very interesting, so I tried to analyze\x01",
            "it, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "I couldn't figure out how it\x01",
            "worked in the slightest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "*sigh* Modern medical science still has a\x01",
            "long way to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_DF9")

    Jump("loc_F21")

    label("loc_DFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_F21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EA3")

    ChrTalk(    #43
        0xFE,
        (
            "There are dangerous medical substances\x01",
            "in the central factory labs as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "If any bottles were to break or crack,\x01",
            "it wouldn't be pretty...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F21")

    label("loc_EA3")


    ChrTalk(    #45
        0xFE,
        (
            "Doesn't seem like there was much\x01",
            "damage from the earthquake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Phew! Thank goodness the shaking\x01",
            "wasn't too strong.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_F21")

    Jump("loc_F82")

    label("loc_F24")


    ChrTalk(    #47
        0xFE,
        "If anything comes up, stop by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        "I'll probably be right here if you need me.\x02",
    )

    CloseMessageWindow()

    label("loc_F82")

    Jump("loc_17CC")

    label("loc_F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1341")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #49
        0xFE,
        "Oh, you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1011FAh, Dr. Miriam.\x02\x03",

            "#1007FThank you very much again for your\x01",
            "help back then.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x106,
        "#053FYeah, I owe you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x106, 400)

    ChrTalk(    #52
        0xFE,
        "Agate. I'm glad to see you're well.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        "How have you been since then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x106,
        (
            "#050FNo problem at all. I'm totally back to normal.\x01",
            "Thanks for askin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "Well, that's good. It doesn't seem like\x01",
            "there were any aftereffects, in that case.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "That's some vitality.\x01",
            "I guess that's a bracer for you. Your body\x01",
            "is your capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1016FWell, that's Agate, anyway. If nothing else,\x01",
            "he's a walking damage sponge.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11EC")

    ChrTalk(    #58
        0x107,
        "#067FAhaha...\x02",
    )

    CloseMessageWindow()

    label("loc_11EC")


    ChrTalk(    #59
        0xFE,
        "If anything comes up, stop by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Of course, I never want to see\x01",
            "an injury like that again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x106,
        (
            "#051FYeah, no worries.\x02\x03",

            "I never wanna be injured like that again,\x01",
            "anyway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0xFE,
        "Yes, don't forget those words.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        "Do be very careful as you attend to your work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1006FYeah, you got it.\x02\x03",

            "Well, see you later, Dr. Miriam.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17C6")

    label("loc_1341")

    TurnDirection(0xFE, 0x101, 0)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #65
        0xFE,
        "Oh, you all...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1011FOh, Dr. Miriam.\x02\x03",

            "#1007FThank you very much again for your\x01",
            "help back then.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13EA")

    ChrTalk(    #67
        0x107,
        "#562FY-Yeah...\x02",
    )

    CloseMessageWindow()

    label("loc_13EA")


    ChrTalk(    #68
        0xFE,
        "No, I didn't do anything.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "If you want to thank anyone, you should thank\x01",
            "the priest who supplied the medicine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        "So...is Agate well?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x101,
        (
            "#1006FYeah, no problem. Seems like\x01",
            "he's totally back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0xFE,
        "I see, good to hear that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "That's some vitality.\x01",
            "I guess that's a bracer for you. Your body\x01",
            "is your capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1016FWell, that's Agate, anyway. If nothing else,\x01",
            "he's a walking damage sponge.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15AD")

    ChrTalk(    #75
        0x107,
        "#067FAhaha...\x02",
    )

    CloseMessageWindow()

    label("loc_15AD")


    ChrTalk(    #76
        0xFE,
        "If anything comes up, stop by any time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "Of course, I never want to see\x01",
            "an injury like that again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1015FYeah... We'll stay on our toes.\x02\x03",

            "Any job could have danger in it, after all...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x103,
        (
            "#026FYes, absolutely, Estelle.\x02\x03",

            "To perpetually sharpen your awareness\x01",
            "to prepare for unseen threats...\x02\x03",

            "#027FCassius often spoke of that as\x01",
            "the mindset of a bracer.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #80
        0xFE,
        "Yes, don't forget those words.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #81
        0xFE,
        (
            "Continue to be careful as you attend\x01",
            "to your work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x101,
        (
            "#1006FYeah, you got it.\x02\x03",

            "Well, see you later, Dr. Miriam.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C6")

    OP_A2(0x142E)
    OP_A2(0x0)

    label("loc_17CC")

    TalkEnd(0x8)
    Return()

    # Function_3_200 end

    def Function_4_17D0(): pass

    label("Function_4_17D0")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_17F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_17F6")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #83
        0xFE,
        "Nya～～go.\x02",
    )

    CloseMessageWindow()

    label("loc_17F6")

    Jump("loc_180A")

    label("loc_17F9")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #84
        0xFE,
        "Nya-o.\x02",
    )

    CloseMessageWindow()

    label("loc_180A")

    TalkEnd(0x9)
    Return()

    # Function_4_17D0 end

    SaveToFile()

Try(main)
