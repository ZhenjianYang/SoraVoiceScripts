from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3116   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3116.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60013",
        Flags               = 1,
        EntryFunctionIndex  = 12,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3116_1 ._SN',
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
        'Karl',                                 # 9
        'Professor Russell',                    # 10
        'Tita',                                 # 11
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
        'ED6_DT07/CH01190 ._CH',             # 00
        'ED6_DT07/CH02020 ._CH',             # 01
        'ED6_DT07/CH00060 ._CH',             # 02
        'ED6_DT07/CH00137 ._CH',             # 03
        'ED6_DT07/CH00130 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01190P._CP',             # 00
        'ED6_DT07/CH02020P._CP',             # 01
        'ED6_DT07/CH00060P._CP',             # 02
        'ED6_DT07/CH00137P._CP',             # 03
        'ED6_DT07/CH00130P._CP',             # 04
    )

    DeclNpc(
        X                   = -2000,
        Z                   = 0,
        Y                   = 3410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 2,
    )

    DeclNpc(
        X                   = -120,
        Z                   = 0,
        Y                   = 13020,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = -1920,
        Z                   = 0,
        Y                   = 14190,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    DeclActor(
        TriggerX            = -340,
        TriggerZ            = 0,
        TriggerY            = 15310,
        TriggerRange        = 1000,
        ActorX              = -340,
        ActorZ              = 500,
        ActorY              = 15310,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4350,
        TriggerZ            = 0,
        TriggerY            = 2150,
        TriggerRange        = 1000,
        ActorX              = 4350,
        ActorZ              = 500,
        ActorY              = 2150,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4600,
        TriggerZ            = 0,
        TriggerY            = 15420,
        TriggerRange        = 1000,
        ActorX              = 4600,
        ActorZ              = 500,
        ActorY              = 15420,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_1CF",          # 01, 1
        "Function_2_1FB",          # 02, 2
        "Function_3_121E",         # 03, 3
        "Function_4_1323",         # 04, 4
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1A8")
    Jump("loc_1CE")

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BE")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)

    label("loc_1BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE")
    SetChrFlags(0x8, 0x10)

    label("loc_1CE")

    Return()

    # Function_0_19E end

    def Function_1_1CF(): pass

    label("Function_1_1CF")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EE")
    OP_79(0xFF, 0x2)
    OP_7A(0x8, 0x2)
    OP_7B()
    OP_72(0x3, 0x4)
    OP_72(0x4, 0x4)

    label("loc_1EE")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    Return()

    # Function_1_1CF end

    def Function_2_1FB(): pass

    label("Function_2_1FB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_91D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x419, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A0")

    ChrTalk(    #0
        0xFE,
        "Hmm? Ah, bracers.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Hey, long time no see.\x01",
            "Glad to see you're well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        (
            "#1000FYou too, Karl.\x02\x03",

            "Sure seems like things are pretty\x01",
            "rough around here.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #3
        0xFE,
        (
            "Yeah, everything from the lights to the\x01",
            "experiment equipment is dead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "By the way...\x01",
            "What happened to that gunner?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1004FYou mean Olivier?\x02\x03",

            "#1015FHe went back to his home country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        "...Home country?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        "So Olivier, was he...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        "#1040FYes, he was from another nation.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #9
        0xFE,
        "Huh, that so...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        "Hmm, what a shame.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "I would've loved to have him take a\x01",
            "look at the new model gun.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Of course, I know now's not\x01",
            "the time for that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "If this phenomenon continues as it is,\x01",
            "my research is going to need to be\x01",
            "completely redone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Haha, hahahahaha... Ah...\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1020FK-Karl...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x102,
        (
            "#1048F(Seems like this situation's really\x01",
            "pushing him to the edge...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    OP_A2(0x20CF)
    Jump("loc_91A")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_726")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B")

    ChrTalk(    #17
        0xFE,
        (
            "If this phenomenon continues as it is,\x01",
            "my research is going to need to be\x01",
            "completely redone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "Haha, hahahahaha... Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        "Ahahahaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_723")

    label("loc_64B")


    ChrTalk(    #20
        0xFE,
        (
            "Not being able to use guns anymore\x01",
            "was a heck of a shock...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "No point in being depressed forever,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "If I let myself get depressed over one or two\x01",
            "setbacks, I'll never make any grand discoveries.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_723")

    Jump("loc_91A")

    label("loc_726")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CA")

    ChrTalk(    #23
        0xFE,
        (
            "If this phenomenon continues as it is,\x01",
            "my research is going to need to be\x01",
            "completely redone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        "Haha, hahahahaha... Ah...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        "Ahahahaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_91A")

    label("loc_7CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87E")

    ChrTalk(    #26
        0xFE,
        (
            "I finally managed to get my new model gun\x01",
            "ready for production, but now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        "For it to all be for nothing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Haha, I can't stop laughing from\x01",
            "the shock.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_91A")

    label("loc_87E")


    ChrTalk(    #29
        0xFE,
        (
            "I managed to get my new model gun\x01",
            "ready for production, but now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xFE,
        (
            "For it to all be for nothing... I can barely\x01",
            "touch my research from the shock.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_91A")

    Jump("loc_121A")

    label("loc_91D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_92B")
    Call(1, 9)
    Jump("loc_121A")

    label("loc_92B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_939")
    Call(1, 11)
    Jump("loc_121A")

    label("loc_939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_947")
    Call(1, 10)
    Jump("loc_121A")

    label("loc_947")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_9B5")

    ChrTalk(    #31
        0xFE,
        (
            "Combat doesn't count if you haven't equipped\x01",
            "the 0-Type Orbal Gun α.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xFE,
        "Be careful of that.\x02",
    )

    CloseMessageWindow()
    Jump("loc_121A")

    label("loc_9B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_9C3")
    Call(1, 8)
    Jump("loc_121A")

    label("loc_9C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_9D1")
    Call(1, 1)
    Jump("loc_121A")

    label("loc_9D1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EA")
    Call(1, 4)
    Jump("loc_121A")

    label("loc_9EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A15")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_A0E")
    Call(1, 2)
    Jump("loc_A12")

    label("loc_A0E")

    Call(1, 0)

    label("loc_A12")

    Jump("loc_121A")

    label("loc_A15")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6E, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_EB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_B7A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AC8")

    ChrTalk(    #33
        0xFE,
        (
            "They've declared the earthquake danger over,\x01",
            "so I should be able to focus on my research\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "Look forward to my new model orbal gun!\x02",
    )

    CloseMessageWindow()
    Jump("loc_B77")

    label("loc_AC8")


    ChrTalk(    #35
        0xFE,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "They've declared the earthquake danger over,\x01",
            "so I should be able to focus on my research\x01",
            "for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        "Look forward to my new model orbal gun!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_B77")

    Jump("loc_EAE")

    label("loc_B7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_CBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C04")

    ChrTalk(    #38
        0xFE,
        (
            "Seems like Professor Russell's doing \x01",
            "some kind of experiment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        "If I get some time, maybe I'll go check it out.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBA")

    label("loc_C04")


    ChrTalk(    #40
        0xFE,
        "Ah, you all.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Seems like Professor Russell's doing some kind\x01",
            "of experiment. Do you know anything about it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Maybe once I finish the paperwork\x01",
            "I'll go check it out...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_CBA")

    Jump("loc_EAE")

    label("loc_CBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_D9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D28")

    ChrTalk(    #43
        0xFE,
        (
            "Looks like you're busy.\x01",
            "On the job again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "Man, it must be tough being a bracer.\x02",
    )

    CloseMessageWindow()
    Jump("loc_D99")

    label("loc_D28")


    ChrTalk(    #45
        0xFE,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xFE,
        (
            "Looks like you're busy.\x01",
            "On the job again?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "Man, it must be tough being a bracer.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_D99")

    Jump("loc_EAE")

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_EAE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E22")

    ChrTalk(    #48
        0xFE,
        (
            "Thanks for your help today.\x01",
            "You were a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "If anything else should come up,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAE")

    label("loc_E22")


    ChrTalk(    #50
        0xFE,
        "Hey, everyone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Thanks for your help today.\x01",
            "You were a big help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "If anything else should come up,\x01",
            "I'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_EAE")

    Jump("loc_121A")

    label("loc_EB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_FB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F1B")

    ChrTalk(    #53
        0xFE,
        "To have no one respond to my request...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "Maybe the requirements were too tough?\x02",
    )

    CloseMessageWindow()
    Jump("loc_FB2")

    label("loc_F1B")


    ChrTalk(    #55
        0xFE,
        "*sigh* I'm really in a fix here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "I've waited a long time, but no one's\x01",
            "taken up my request...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "Maybe the requirements were too tough?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_FB2")

    Jump("loc_121A")

    label("loc_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_10FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_104D")

    ChrTalk(    #58
        0xFE,
        (
            "Phew! It's finally ready. Now I just\x01",
            "have to wait for some testers to arrive.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "Let's see...\x01",
            "I didn't forget anything, I hope.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10F8")

    label("loc_104D")


    ChrTalk(    #60
        0xFE,
        (
            "Let's see, the orbal gun is tuned.\x01",
            "I've already finished all the paperwork... yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "All right, I'm ready. Now I just have to\x01",
            "wait for some testers to arrive.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_10F8")

    Jump("loc_121A")

    label("loc_10FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_121A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11B4")

    ChrTalk(    #62
        0xFE,
        (
            "Let's see, the orbal gun is tuned.\x01",
            "I've already finished all the paperwork... yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "All right, I'm ready. Now I just have to\x01",
            "wait for some testers to arrive.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_121A")

    label("loc_11B4")


    ChrTalk(    #64
        0xFE,
        (
            "Phew! To have an earthquake\x01",
            "at a time like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        "I've got an important test soon, too...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_121A")

    TalkEnd(0x8)
    Return()

    # Function_2_1FB end

    def Function_3_121E(): pass

    label("Function_3_121E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_131F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1299")

    ChrTalk(    #66
        0x9,
        (
            "#103FWhat, that interested in my invention,\x01",
            "are you?\x02\x03",

            "#101FHeh heh heh, look forward to it, then.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_131F")

    label("loc_1299")


    ChrTalk(    #67
        0x9,
        (
            "#100FHow goes the investigation?\x02\x03",

            "It'll still take me a bit of time to get ready.\x02\x03",

            "Once I'm prepared, I'll contact the guild.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_131F")

    TalkEnd(0x9)
    Return()

    # Function_3_121E end

    def Function_4_1323(): pass

    label("Function_4_1323")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1556")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1446")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_13B2")

    ChrTalk(    #68
        0xA,
        (
            "#560FI'm sure this device will be useful.\x02\x03",

            "We'll work on it as fast as we can,\x01",
            "so wait just a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1443")

    label("loc_13B2")


    ChrTalk(    #69
        0xA,
        (
            "#560FAh, Agate.\x02\x03",

            "I'm sure the device we're preparing\x01",
            "now will be useful.\x02\x03",

            "We'll work on it as fast as we can,\x01",
            "so wait just a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1443")

    Jump("loc_1556")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_14C1")

    ChrTalk(    #70
        0xA,
        (
            "#060FI'm sure this device will be useful.\x02\x03",

            "We'll work on it as fast as possible,\x01",
            "so wait just a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1556")

    label("loc_14C1")


    ChrTalk(    #71
        0xA,
        (
            "#060FOh, hey, guys!\x02\x03",

            "I'm sure the device we're preparing\x01",
            "now will be useful.\x02\x03",

            "We'll work on it as fast as we can,\x01",
            "so wait just a bit longer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_1556")

    TalkEnd(0xA)
    Return()

    # Function_4_1323 end

    SaveToFile()

Try(main)
