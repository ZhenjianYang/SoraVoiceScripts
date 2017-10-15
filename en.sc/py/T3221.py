from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3221   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3221.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T3221_1 ._SN',
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
        'Mao',                                  # 9
        'Addy',                                 # 10
        'Horrace',                              # 11
        'Horrace',                              # 12
        'Ed',                                   # 13
        'Recia',                                # 14
        'Faults',                               # 15
        'Shelby',                               # 16
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
        'ED6_DT07/CH02430 ._CH',             # 00
        'ED6_DT07/CH01130 ._CH',             # 01
        'ED6_DT07/CH01003 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT07/CH01150 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01140 ._CH',             # 06
        'ED6_DT07/CH01143 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT07/CH02430P._CP',             # 00
        'ED6_DT07/CH01130P._CP',             # 01
        'ED6_DT07/CH01003P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT07/CH01150P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01140P._CP',             # 06
        'ED6_DT07/CH01143P._CP',             # 07
    )

    DeclNpc(
        X                   = 2590,
        Z                   = 250,
        Y                   = 5360,
        Direction           = 180,
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
        X                   = 8490,
        Z                   = 0,
        Y                   = 340,
        Direction           = 102,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 14140,
        Z                   = 200,
        Y                   = 2029,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x135,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -2490,
        Z                   = 0,
        Y                   = 40320,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = -31490,
        Z                   = -250,
        Y                   = 8530,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 7590,
        Z                   = 0,
        Y                   = 73170,
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
        X                   = 11190,
        Z                   = 0,
        Y                   = 2440,
        Direction           = 225,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 8780,
        Z                   = 200,
        Y                   = 6560,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x195,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )


    DeclActor(
        TriggerX            = 2670,
        TriggerZ            = 250,
        TriggerY            = 3820,
        TriggerRange        = 400,
        ActorX              = 2590,
        ActorZ              = 1750,
        ActorY              = 5360,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 9940,
        TriggerZ            = 0,
        TriggerY            = 90,
        TriggerRange        = 400,
        ActorX              = 8490,
        ActorZ              = 1500,
        ActorY              = 340,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 8960,
        TriggerZ            = 250,
        TriggerY            = 13840,
        TriggerRange        = 1000,
        ActorX              = 9100,
        ActorZ              = 1750,
        ActorY              = 13840,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_256",          # 00, 0
        "Function_1_2F8",          # 01, 1
        "Function_2_2F9",          # 02, 2
        "Function_3_2FE",          # 03, 3
        "Function_4_1F28",         # 04, 4
        "Function_5_1F2D",         # 05, 5
        "Function_6_2776",         # 06, 6
        "Function_7_2A85",         # 07, 7
        "Function_8_31C0",         # 08, 8
        "Function_9_39F3",         # 09, 9
        "Function_10_3B88",        # 0A, 10
        "Function_11_3ECF",        # 0B, 11
        "Function_12_4B31",        # 0C, 12
        "Function_13_557B",        # 0D, 13
        "Function_14_5604",        # 0E, 14
        "Function_15_565D",        # 0F, 15
    )


    def Function_0_256(): pass

    label("Function_0_256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_28B")
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_283")
    SetChrPos(0xD, -1150, 0, 40780, 0)
    Jump("loc_288")

    label("loc_283")

    SetChrFlags(0xD, 0x80)

    label("loc_288")

    Jump("loc_2D3")

    label("loc_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_29A")
    SetChrFlags(0xD, 0x80)
    Jump("loc_2D3")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2B8")
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_2D3")

    label("loc_2B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_2CC")
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_2D3")

    label("loc_2CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2D3")

    label("loc_2D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2E9")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 3)
    Jump("loc_2F7")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_2F7")
    OP_A3(0x10F1)
    Event(0, 12)

    label("loc_2F7")

    Return()

    # Function_0_256 end

    def Function_1_2F8(): pass

    label("Function_1_2F8")

    Return()

    # Function_1_2F8 end

    def Function_2_2F9(): pass

    label("Function_2_2F9")

    Call(0, 3)
    Return()

    # Function_2_2F9 end

    def Function_3_2FE(): pass

    label("Function_3_2FE")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_335")
    Call(1, 1)
    Jump("loc_339")

    label("loc_335")

    Call(1, 0)

    label("loc_339")

    Jump("loc_1F24")

    label("loc_33C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_388")
    Call(6, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_377")
    OP_A9(0xA1)
    TalkEnd(0x8)
    Return()

    label("loc_377")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_388")
    TalkEnd(0x8)
    Return()

    label("loc_388")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A02")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x410, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_633")
    EventBegin(0x0)
    Fade(1000)
    OP_6D(2590, 250, 4210, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 3260, 250, 3540, 0)
    SetChrPos(0x102, 2200, 250, 3530, 0)
    SetChrPos(0xF8, 3750, 250, 2330, 0)
    SetChrPos(0xF9, 2210, 250, 2420, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        "#1000FHi, Mrs. Mao.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BB")

    ChrTalk(    #1
        0x107,
        "#061FHello!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "#680FAh, Estelle and Tita. Thanks for coming.\x02\x03",

            "#683FOh, over there, is that...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_506")

    label("loc_4BB")


    ChrTalk(    #3
        0x8,
        (
            "#680FAh, Estelle. Thanks for coming.\x02\x03",

            "#683FOh, over there, is that...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_506")


    ChrTalk(    #4
        0x102,
        "#1040F#6PIt's been a while, ma'am.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x8,
        (
            "#681FI thought I knew that face!\x01",
            "So it IS Joshua.\x02\x03",

            "Seems like ages since I saw you\x01",
            "all together like this.\x02\x03",

            "#680FSorry to say the baths are out of commission\x01",
            "right now, but please take a load off.\x02\x03",

            "Our delicious food is still available, after all!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2083)
    EventEnd(0x0)
    Jump("loc_9FB")

    label("loc_633")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A")

    ChrTalk(    #6
        0x8,
        (
            "#680FThanks to this little orbment blackout,\x01",
            "you can't use the baths.\x02\x03",

            "Still, there's not a thing wrong with our kitchen!\x01",
            "Feel free to order something!\x02\x03",

            "I'm sure you're busy, but do relax for a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9FB")

    label("loc_70A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_882")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E7")

    ChrTalk(    #7
        0x8,
        (
            "#680FHey, you all. Good work.\x02\x03",

            "Thanks to you guys, our inn is ready\x01",
            "for business again.\x02\x03",

            "I'm sure it'll be a bit before the customers\x01",
            "return, but as long as they come back,\x01",
            "I don't mind waiting!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_87F")

    label("loc_7E7")


    ChrTalk(    #8
        0x8,
        (
            "#680FThanks to you guys, our inn is ready\x01",
            "for business again.\x02\x03",

            "Now we just have to wait for all the chaos\x01",
            "to settle down and our guests to return.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87F")

    Jump("loc_9FB")

    label("loc_882")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 7)), scpexpr(EXPR_END)), "loc_9F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95C")

    ChrTalk(    #9
        0x8,
        (
            "#680FThe pump shed is up on the\x01",
            "area north of the village square.\x02\x03",

            "If we can't get that thing working again,\x01",
            "I'm afraid I'll go out of business.\x02\x03",

            "If you lot have any good ideas,\x01",
            "I'm all ears!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_9F3")

    label("loc_95C")


    ChrTalk(    #10
        0x8,
        (
            "#680FThe Pump Shed is up on the\x01",
            "area north of the village square.\x02\x03",

            "If we can't get that thing working again,\x01",
            "I'm afraid we'll go out of business.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F3")

    Jump("loc_9FB")

    label("loc_9F6")

    Call(0, 11)
    Return()

    label("loc_9FB")

    TalkEnd(0x8)
    Return()

    label("loc_A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x290, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1117")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_AF6")

    ChrTalk(    #11
        0x8,
        (
            "#680FWell, one way or another, if nature's\x01",
            "behind it, there's not much we can do.\x02\x03",

            "Should something like that happen again,\x01",
            "we'll give up and call the guild.\x02\x03",

            "Well, if anything else comes up,\x01",
            "we'll be counting on you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1114")

    label("loc_AF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_CB4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_BC6")

    ChrTalk(    #12
        0x8,
        (
            "#680FSeems like the earth has finally settled\x01",
            "down, so that's one case closed.\x02\x03",

            "If you find some time, you should\x01",
            "all come and stay a spell with us.\x02\x03",

            "You guys're always welcome.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CB1")

    label("loc_BC6")


    ChrTalk(    #13
        0x8,
        (
            "#680FHello, dears. Thanks for the help before.\x02\x03",

            "With our hot springs up and running again,\x01",
            "we can finally get back to business.\x02\x03",

            "If you find some time, you should\x01",
            "all come and stay a spell with us.\x02\x03",

            "You guys're always welcome.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_CB1")

    Jump("loc_109D")

    label("loc_CB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_D63")

    ChrTalk(    #14
        0x8,
        (
            "#680FYou can reach the cave with the Hot Springs\x01",
            "Fountainhead by going through the wood\x01",
            "gate in the back.\x02\x03",

            "If you use that key I just gave you,\x01",
            "it should open.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_109D")

    label("loc_D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_EBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_E13")

    ChrTalk(    #15
        0x8,
        (
            "#680FMy, my. I've heard rumors about earthquakes\x01",
            "cropping up all over the place.\x02\x03",

            "Can't imagine something like that being\x01",
            "all that common in this region.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EBB")

    label("loc_E13")


    ChrTalk(    #16
        0x8,
        (
            "#680FApparently there was an earthquake\x01",
            "in Zeiss a bit ago, if you can believe it\x02\x03",

            "I've been here for AGES and I can hardly\x01",
            "remember a rumble in all that time.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_EBB")

    Jump("loc_109D")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_1022")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F49")

    ChrTalk(    #17
        0x8,
        (
            "#680FA non-aggression pact's just a\x01",
            "promise to be peaceful, right?\x02\x03",

            "Why didn't they sign something like\x01",
            "that sooner?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_101F")

    label("loc_F49")


    ChrTalk(    #18
        0x8,
        (
            "#680FSeems like there'll be a signing ceremony\x01",
            "for a non-aggression pact or whatever soon.\x02\x03",

            "Should be some Republican guests, too, apparently.\x01",
            "I'm hoping we see a few of those as customers\x01",
            "after it's done.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_101F")

    Jump("loc_109D")

    label("loc_1022")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_109D")

    ChrTalk(    #19
        0x8,
        (
            "#680FIf you're in need of a rejuvenating soak,\x01",
            "feel free to hit the baths whenever you like!\x02\x03",

            "Well, take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_109D")

    Jump("loc_1114")

    label("loc_10A0")


    ChrTalk(    #20
        0x8,
        (
            "#680FIf you're in need of a rejuvenating soak,\x01",
            "feel free to hit the baths whenever you like!\x02\x03",

            "Well, take care.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1114")

    Jump("loc_1F24")

    label("loc_1117")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 7)), scpexpr(EXPR_END)), "loc_1896")
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #21
        0x8,
        "#680FOhh, welcome.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x107, 400)

    ChrTalk(    #22
        0x8,
        "#680FI see little Tita's with you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x107,
        "#560FHi, Mrs. Mao!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1006FLong time no see, Mrs. Mao.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #25
        0x8,
        (
            "#680FAhh, Estelle! It HAS been a while.\x02\x03",

            "You seem a lot more grown up since\x01",
            "the last time we met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        "#1008FAhaha... Really?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1611")

    ChrTalk(    #27
        0x104,
        "#030FMadam, thank you for your care the other day.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #28
        0x8,
        (
            "#683FOh, I thought I knew you...\x02\x03",

            "If it isn't Olivier!\x01",
            "What brings you back so soon?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x107,
        "#064FHuh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x104,
        (
            "#035FHeh, I have my reasons.\x02\x03",

            "Currently, I am accompanying Estelle\x01",
            "as a supporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        "#1004FD-Do you two know each other?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #32
        0x8,
        (
            "#680FYes, we do. He stayed here not\x01",
            "that long ago.\x02\x03",

            "#685FHe's the first customer we've ever\x01",
            "had that played a lute in the baths.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1445")

    ChrTalk(    #33
        0x106,
        "#551FNew place, same shtick. Typical.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1481")

    label("loc_1445")


    ChrTalk(    #34
        0x103,
        (
            "#025F*sigh* I guess you do the same \x01",
            "thing everywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1481")


    ChrTalk(    #35
        0x104,
        (
            "#031FHeh, 'tis the sacred duty of all those\x01",
            "dedicated to the arts.\x02\x03",

            "Time and location mean nothing to one\x01",
            "who serves the Goddess of beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        (
            "#1007FYeah, but playing your lute in the buff?\x02\x03",

            "#1013F...\x01",
            "...\x01",
            "And now that image is in my head. Ewww.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x107, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #37
        0x107,
        "#562FE-Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x8,
        (
            "#680FWell, one way or another, glad you\x01",
            "liked our baths.\x02\x03",

            "How about staying for a while?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1672")

    label("loc_1611")


    ChrTalk(    #39
        0x8,
        (
            "#680FWell, putting that aside, since you're here...\x02\x03",

            "How about a relaxing night at the inn?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_16EB")

    ChrTalk(    #40
        0x106,
        (
            "#051FWe'd love to take you up on that, but\x01",
            "we're in the middle of work right now.\x02\x03",

            "Another time for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_177C")

    label("loc_16EB")


    ChrTalk(    #41
        0x103,
        (
            "#020FI think we'd all love to, but unfortunately\x01",
            "we're in the middle of work.\x02\x03",

            "We'll have to have our soak a little later\x01",
            "on down the line.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_177C")

    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #42
        0x8,
        (
            "#680FWhat, on the job again? Don't you bracers\x01",
            "ever take a day off? Hmph.\x02\x03",

            "Well, at least take a quick dip before you go.\x02\x03",

            "You're all welcome to go in any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1001FAh, that sounds really niiiiice...\x02\x03",

            "If we get some time, we'll definitely\x01",
            "take you up on that.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1E")

    label("loc_1896")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_1F1E")
    TurnDirection(0x8, 0x101, 0)
    OP_62(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x8)

    ChrTalk(    #44
        0x8,
        "#680FOhh, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        "#1006FLong time no see, Mrs. Mao.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x8,
        (
            "#680FAhh, Estelle! It HAS been a while.\x02\x03",

            "You seem a lot more grown up since\x01",
            "the last time we met.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        "#1008FAhaha... Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x104,
        "#030FMadam, thank you for your care the other day.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x104, 400)

    ChrTalk(    #49
        0x8,
        (
            "#683FOh, I thought I knew you...\x02\x03",

            "If it isn't Olivier.\x01",
            "What brings you back, dear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x104,
        (
            "#035FHeh, I have my reasons.\x02\x03",

            "Currently, I am accompanying Estelle\x01",
            "as a supporter.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        "#1004FD-Do you two know each other?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #52
        0x8,
        (
            "#680FYes, dear. He stayed here not\x01",
            "that long ago.\x02\x03",

            "#685FHe's the first customer we've ever\x01",
            "had that played a lute in the baths.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1B59")

    ChrTalk(    #53
        0x106,
        "#551FNew place, same shtick. Typical.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B95")

    label("loc_1B59")


    ChrTalk(    #54
        0x103,
        (
            "#025F*sigh* I guess you do the same \x01",
            "thing everywhere.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B95")


    ChrTalk(    #55
        0x104,
        (
            "#031FHeh, 'tis the sacred duty of all those\x01",
            "dedicated to the arts.\x02\x03",

            "Time and location mean nothing to one\x01",
            "who serves the Goddess of beauty.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        (
            "#1007FYeah, but playing your lute in the buff?\x02\x03",

            "#1013F...\x01",
            "...\x01",
            "And now that image is in my head. Ewww.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x105,
        "#540F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x8,
        (
            "#680FWell, one way or another, glad you\x01",
            "liked our baths.\x02\x03",

            "How about staying for a while?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1D76")

    ChrTalk(    #59
        0x106,
        (
            "#051FWe'd love to take you up on that, but\x01",
            "we're in the middle of work right now.\x02\x03",

            "Another time for sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E07")

    label("loc_1D76")


    ChrTalk(    #60
        0x103,
        (
            "#020FI think we'd all love to, but unfortunately\x01",
            "we're in the middle of work.\x02\x03",

            "We'll have to have our soak a little later\x01",
            "on down the line.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E07")

    TurnDirection(0x8, 0xF7, 400)

    ChrTalk(    #61
        0x8,
        (
            "#680FWhat, on the job again? Don't you bracers\x01",
            "ever take a day off? Hmph.\x02\x03",

            "Well, at least take a quick dip before you go.\x02\x03",

            "You're all welcome to go in any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1001FAh, that sounds really niiiiice...\x02\x03",

            "If we get some time, we'll definitely\x01",
            "take you up on that.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1E")

    OP_A2(0x1482)
    OP_A2(0x0)

    label("loc_1F24")

    TalkEnd(0x8)
    Return()

    # Function_3_2FE end

    def Function_4_1F28(): pass

    label("Function_4_1F28")

    Call(0, 5)
    Return()

    # Function_4_1F28 end

    def Function_5_1F2D(): pass

    label("Function_5_1F2D")

    TalkBegin(0x9)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                                 # 0
            "Shop\x01",                                 # 1
            "[Mountain Man Stew] - 1000 mira\x01",      # 2
            "Leave\x01",                                # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAD")
    OP_0D()
    OP_A9(0xA2)
    OP_56(0x0)
    TalkEnd(0x9)
    Return()

    label("loc_1FAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C5")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_208B")
    SubMira(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #63
        "\x06Ate #2CMountain Man Stew#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0xBB8)
    OP_31(0x1, 0xFD, 0xBB8)
    OP_31(0x2, 0xFD, 0xBB8)
    OP_31(0x3, 0xFD, 0xBB8)
    OP_31(0x4, 0xFD, 0xBB8)
    OP_31(0x5, 0xFD, 0xBB8)
    OP_31(0x6, 0xFD, 0xBB8)
    OP_31(0x7, 0xFD, 0xBB8)
    OP_31(0x8, 0xFD, 0xBB8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x4)"), scpexpr(EXPR_END)), "loc_204A")
    Jump("loc_207D")

    label("loc_204A")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #64
        "\x06Learned [#2CMountain Man Stew#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_207D")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_20B3")

    label("loc_208B")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #65
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_20B3")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x9)
    Return()

    label("loc_20C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D6")
    TalkEnd(0x9)
    Return()

    label("loc_20D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_21B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2154")

    ChrTalk(    #66
        0x9,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x9,
        "The baths are finally available for use.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x9,
        "Please, relax and enjoy yourselves.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_21AF")

    label("loc_2154")


    ChrTalk(    #69
        0x9,
        "The baths are finally available for use.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x9,
        "Our inn is open for business as always.\x02",
    )

    CloseMessageWindow()

    label("loc_21AF")

    Jump("loc_2772")

    label("loc_21B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_22F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2278")

    ChrTalk(    #71
        0x9,
        "Welcome. Welcome to the Maple Leaf Inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x9,
        (
            "I'm very sorry, but the bath\x01",
            "isn't usable at the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x9,
        (
            "For all orbments to be out...\x01",
            "What could be the cause, I wonder.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)
    Jump("loc_22F2")

    label("loc_2278")


    ChrTalk(    #74
        0x9,
        "I'm sorry, but the baths aren't usable right now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x9,
        (
            "I really am sorry. I'm sure you\x01",
            "were looking forward to them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F2")

    Jump("loc_2772")

    label("loc_22F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_23D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_235F")

    ChrTalk(    #76
        0x9,
        "The baths are finally available for use.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x9,
        "Our baths are finally back to normal.\x02",
    )

    CloseMessageWindow()
    Jump("loc_23CD")

    label("loc_235F")


    ChrTalk(    #78
        0x9,
        "Ah, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x9,
        "The baths are finally available for use.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x9,
        "Our baths are finally back to normal.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_23CD")

    Jump("loc_2772")

    label("loc_23D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_24A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_243B")

    ChrTalk(    #81
        0x9,
        (
            "This is the first time we've ever had\x01",
            "such a problem.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x9,
        "I wonder what happened...\x02",
    )

    CloseMessageWindow()
    Jump("loc_249E")

    label("loc_243B")


    ChrTalk(    #83
        0x9,
        "For the springs to get so hot that they'd boil...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x9,
        "I wonder what happened underground.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_249E")

    Jump("loc_2772")

    label("loc_24A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_265A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2569")

    ChrTalk(    #85
        0x9,
        (
            "Apparently some monsters wandered\x01",
            "into the outdoor bath.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x9,
        (
            "I wonder if the rumors about the peeping\x01",
            "tom were actually just the monsters...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x9,
        "Really, what troublemakers.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2657")

    label("loc_2569")


    ChrTalk(    #88
        0x9,
        (
            "Lately, I've heard rumors that there's\x01",
            "a peeping tom at our baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x9,
        (
            "No one's caught a clear look at the culprit,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x9,
        (
            "I hate having just rumors running\x01",
            "around with no proof.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x9,
        "I hope some bracers will solve it soon...\x02",
    )

    CloseMessageWindow()

    label("loc_2657")

    Jump("loc_2772")

    label("loc_265A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_26E2")

    ChrTalk(    #92
        0x9,
        (
            "We're famous for our Eastern-style cooking\x01",
            "here. We've got new recipes in, so I really\x01",
            "recommend giving it a try.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2772")

    label("loc_26E2")


    ChrTalk(    #93
        0x9,
        "Ah, welcome. Welcome to the Maple Leaf Inn.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x9,
        (
            "We're famous for our Eastern-style cooking\x01",
            "here. Please try some and enjoy yourselves.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_2772")

    TalkEnd(0x9)
    Return()

    # Function_5_1F2D end

    def Function_6_2776(): pass

    label("Function_6_2776")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_28AE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2836")

    ChrTalk(    #95
        0xFE,
        (
            "The beauty of Eastern cooking is that it\x01",
            "makes the most of its ingredients.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "People with a poor sense of taste would be\x01",
            "hard pressed to appreciate its complexity.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28AB")

    label("loc_2836")


    ChrTalk(    #97
        0xFE,
        (
            "The Eastern cooking here is on par\x01",
            "with the best out there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0xFE,
        "I've been to the Anterose, so I would know.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_28AB")

    Jump("loc_2A81")

    label("loc_28AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2963")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_28F8")

    ChrTalk(    #99
        0xFE,
        (
            "Sure is noisy out there.\x01",
            "What's going on out front?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2960")

    label("loc_28F8")


    ChrTalk(    #100
        0xFE,
        (
            "Sure is noisy out there.\x01",
            "What's going on out front?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        "I wonder if some monsters wandered in.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2960")

    Jump("loc_2A81")

    label("loc_2963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_296D")
    Jump("loc_2A81")

    label("loc_296D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_2A81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_29FC")

    ChrTalk(    #102
        0xFE,
        "Ho ho, what a good bath.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #103
        0xFE,
        (
            "What a wonderful refreshing feeling even after\x01",
            "getting out. It really is a quality spring.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A81")

    label("loc_29FC")


    ChrTalk(    #104
        0xFE,
        (
            "I've come all the way from\x01",
            "Bose to visit the baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "These springs are worth it, though.\x01",
            "Best in the country, I tell ya!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_2A81")

    TalkEnd(0xFE)
    Return()

    # Function_6_2776 end

    def Function_7_2A85(): pass

    label("Function_7_2A85")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_2BE2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B52")

    ChrTalk(    #106
        0xFE,
        (
            "Hey, you guys.\x01",
            "Seems like you fixed the pump, huh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "Haha, I guess this is the second time,\x01",
            "but looking forward to seeing you in\x01",
            "the future. As guests next time, hopefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2BDF")

    label("loc_2B52")


    ChrTalk(    #108
        0xFE,
        (
            "We expect great things from you guys\x01",
            "if anything else comes up, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0xFE,
        (
            "With orbments not working, I'm sure\x01",
            "it's hard on everyone.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BDF")

    Jump("loc_31BC")

    label("loc_2BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_2D2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CB9")

    ChrTalk(    #110
        0xFE,
        (
            "My kitchen's non-orbal, so my\x01",
            "work hasn't been affected at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        (
            "An orbal stove's nice and all, but if\x01",
            "something like this were to happen again,\x01",
            "old tools are definitely the way to go.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)
    Jump("loc_2D27")

    label("loc_2CB9")


    ChrTalk(    #112
        0xFE,
        (
            "My kitchen's non-orbal, so my\x01",
            "work hasn't been affected at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Yeah, simple tools really are best.\x02",
    )

    CloseMessageWindow()

    label("loc_2D27")

    Jump("loc_31BC")

    label("loc_2D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_2E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2DB5")

    ChrTalk(    #114
        0xC,
        (
            "It's great to have the hot springs\x01",
            "back to normal. Thanks!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xC,
        (
            "Next time come by on your down time\x01",
            "and relax a bit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E47")

    label("loc_2DB5")


    ChrTalk(    #116
        0xC,
        "Hey, you guys!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xC,
        (
            "Ahhh, it's so good to have the hot springs\x01",
            "back to normal. You guys are lifesavers!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xC,
        "Bracers really are reliable.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2E47")

    Jump("loc_31BC")

    label("loc_2E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_2F5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_2EC4")

    ChrTalk(    #119
        0xC,
        "For the hot springs to boil over like that...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xC,
        "Man, you never know what'll happen in the world.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F57")

    label("loc_2EC4")


    ChrTalk(    #121
        0xC,
        (
            "We're counting on you guys to investigate\x01",
            "the water source and sort this out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xC,
        (
            "If things continue on like this,\x01",
            "we're out of business.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_2F57")

    Jump("loc_31BC")

    label("loc_2F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_30C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3019")

    ChrTalk(    #123
        0xC,
        (
            "Recia's got the palate of a chef. Heh.\x01",
            "Just what'd I'd expect from a daughter of mine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xC,
        (
            "Of course, she's also inherited my, ah,\x01",
            "slightly irresponsible nature too...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C5")

    label("loc_3019")


    ChrTalk(    #125
        0xC,
        (
            "Lately, my daughter Recia's been\x01",
            "helping out around the inn.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xC,
        (
            "She's cleaning the rooms right now,\x01",
            "but in the future I'd like her to help me\x01",
            "out in the kitchen.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_30C5")

    Jump("loc_31BC")

    label("loc_30C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_31BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_316F")

    ChrTalk(    #127
        0xC,
        (
            "It's said there are three important principles in\x01",
            "Eastern cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xC,
        (
            "First is flavor, second's appearance,\x01",
            "and the last is that it's healthy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BC")

    label("loc_316F")


    ChrTalk(    #129
        0xC,
        "Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xC,
        (
            "Give our pride, our Eastern-style cooking,\x01",
            "a try!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_31BC")

    TalkEnd(0xC)
    Return()

    # Function_7_2A85 end

    def Function_8_31C0(): pass

    label("Function_8_31C0")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3355")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32A8")

    ChrTalk(    #131
        0xFE,
        (
            "Seems like no one here's really bothered\x01",
            "at all that orbments aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0xFE,
        (
            "That kinda freaks me out just as much as\x01",
            "the orbments not working, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "I bet Zeiss has totally lost it.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)
    Jump("loc_3352")

    label("loc_32A8")


    ChrTalk(    #134
        0xFE,
        (
            "Seems like no one here's really bothered\x01",
            "at all that orbments aren't working.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        (
            "That kinda freaks me out just as much as\x01",
            "the orbments not working, if you ask me.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3352")

    Jump("loc_39EF")

    label("loc_3355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x286, 0)), scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_362F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3524")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3425")

    ChrTalk(    #136
        0xD,
        (
            "I didn't have anything better to do,\x01",
            "so I got a part-time job here cleaning,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xD,
        (
            "All our customers are so old that it's\x01",
            "hard to get excited about work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3521")

    label("loc_3425")


    ChrTalk(    #138
        0xD,
        (
            "I didn't have anything better to do,\x01",
            "so I got a part-time job here cleaning,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0xD,
        (
            "All our customers are so old that it's\x01",
            "hard to get excited about work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xD,
        (
            "It'd be nice if we had some real\x01",
            "customers again like Lord Olivier.\x01",
            "*siiiiigh*\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_3521")

    Jump("loc_35AA")

    label("loc_3524")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_35AA")

    ChrTalk(    #141
        0xD,
        (
            "Ahhhhh, oh, Lord Olivier...\x01",
            "You're so coooool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0xD,
        (
            "Mmmm, I wish he would kidnap me\x01",
            "away to the Imperial capital. Heehee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35AA")

    Jump("loc_362C")

    label("loc_35AD")


    ChrTalk(    #143
        0xD,
        (
            "Ahhhhh, oh, Lord Olivier...\x01",
            "You're so coooool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xD,
        (
            "Mmmm, I wish he would kidnap me\x01",
            "away to the Imperial capital. Heehee.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_362C")

    Jump("loc_39EF")

    label("loc_362F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C3")

    ChrTalk(    #145
        0xD,
        (
            "I didn't have anything better to do,\x01",
            "so I got a part-time job here cleaning,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0xD,
        (
            "All our customers are so old that it's\x01",
            "hard to get excited about work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xD,
        "...Ah. Wh-What?\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #148
        0xD,
        "Aaaaaaahhhh?! It's Lord Olivier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xD,
        "I'm soooo happy! You came again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1004F(L-Lord Olivier...?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x104,
        (
            "#031FHeh, it's been a while.\x01",
            "Have you been a good girl?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3979")

    label("loc_37C3")


    ChrTalk(    #152
        0xD,
        (
            "I didn't have anything better to do,\x01",
            "so I got a part-time job here cleaning,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xD,
        (
            "All our customers are so old that it's\x01",
            "hard to get excited about work.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x104, 500)

    ChrTalk(    #154
        0xD,
        "...Ah. Wh-What?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xD,
        "O-Over there... Could it be...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0x104,
        (
            "#031FHeh, it's been a while.\x01",
            "Have you been a good girl?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #157
        0xD,
        "Aaaaaaahhhh! I knew it! It's Lord Olivier!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #158
        0xD,
        "I'm soooo happy! You came again?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #159
        0x101,
        "#1004F(L-Lord Olivier...?)\x02",
    )

    CloseMessageWindow()

    label("loc_3979")


    ChrTalk(    #160
        0xD,
        "Lord Olivier, come by and sing again!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #161
        0xD,
        (
            "You're at your most magnificent playing\x01",
            "your lute after all. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1430)
    OP_A2(0x5)

    label("loc_39EF")

    TalkEnd(0xD)
    Return()

    # Function_8_31C0 end

    def Function_9_39F3(): pass

    label("Function_9_39F3")

    TalkBegin(0xE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_3B84")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3A81")

    ChrTalk(    #162
        0xFE,
        (
            "Starting today I'm going to be writing\x01",
            "an article on Eastern cooking.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0xFE,
        "I hope I can come up with something good.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3B84")

    label("loc_3A81")


    ChrTalk(    #164
        0xFE,
        (
            "It's really hard to put delicious food into words.\x01",
            "The mouth can just appreciate it better than\x01",
            "the eyes, you know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0xFE,
        (
            "The more delicious a thing is,\x01",
            "the harder it is to put into words.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #166
        0xFE,
        (
            "What more even needs to be\x01",
            "said aside from, 'Delicious!'?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_3B84")

    TalkEnd(0xE)
    Return()

    # Function_9_39F3 end

    def Function_10_3B88(): pass

    label("Function_10_3B88")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_3C68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0D")

    ChrTalk(    #167
        0xFE,
        "Seems like the hot water's flowing again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0xFE,
        (
            "I guess Alvin's prayers to\x01",
            "the Goddess must have worked.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3C65")

    label("loc_3C0D")


    ChrTalk(    #169
        0xFE,
        "Seems like the hot water's flowing again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0xFE,
        "I might head to the baths in a bit.\x02",
    )

    CloseMessageWindow()

    label("loc_3C65")

    Jump("loc_3ECB")

    label("loc_3C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3ECB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E15")

    ChrTalk(    #171
        0xFE,
        (
            "I came with my partner to soak out the\x01",
            "soreness from our mountain climbing\x01",
            "trip, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #172
        0xFE,
        (
            "Apparently we can't go into the baths thanks\x01",
            "to some problem with the pump.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xFE,
        (
            "But, my partner is determined to have\x01",
            "a bath...somehow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xFE,
        (
            "Trying to insist on something in situations\x01",
            "like this only means you yourself lose out.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xFE,
        (
            "I'm relaxing by taking a nice, slow meal\x01",
            "of this great Eastern-style food.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_3ECB")

    label("loc_3E15")


    ChrTalk(    #176
        0xFE,
        (
            "Even though he knew he couldn't go in,\x01",
            "Alvin went off to the baths.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #177
        0xFE,
        (
            "He's the type who once he makes up his\x01",
            "mind to see something through he'll do it,\x01",
            "even if it kills him.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECB")

    TalkEnd(0xFE)
    Return()

    # Function_10_3B88 end

    def Function_11_3ECF(): pass

    label("Function_11_3ECF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3EEF")
    Call(0, 13)
    Call(0, 14)
    FadeToBright(0, 0)

    label("loc_3EEF")

    Fade(500)
    OP_6D(1600, 250, 5180, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    SetChrPos(0x101, 3260, 250, 3540, 0)
    SetChrPos(0x102, 2100, 250, 3530, 0)
    SetChrPos(0xF8, 3700, 250, 2250, 0)
    SetChrPos(0xF9, 2250, 250, 2250, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xC2, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_445C")

    ChrTalk(    #178
        0x8,
        (
            "#680F#4PYou don't need to worry about the hot springs.\x02\x03",

            "You've got your own jobs you need\x01",
            "to do, I'm sure.\x02\x03",

            "You can put that first.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Accept\x01",                      # 0
            "Offer to Assist Anyway\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4082")
    OP_28(0xC2, 0x1, 0x8000)
    EventEnd(0x0)
    Jump("loc_4459")

    label("loc_4082")


    ChrTalk(    #179
        0x101,
        (
            "#1006F#6PBut, since we're here, why don't we\x01",
            "have a look?\x02\x03",

            "I feel like we might be able to\x01",
            "offer a bracer-like solution.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #180
        0x102,
        "#1044F#6PEstelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x8,
        "#683F#4POh...? What would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #182
        0x101,
        (
            "#1015F#6PHmmm, well.\x02\x03",

            "#1006FFirst, I'd like to borrow the Pump Shed key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #183
        0x8,
        "#680F#4PSure, that's fine, but...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #184
        "\x07\x00Received #1034i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x40A, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42AA")
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    ChrTalk(    #185
        0x101,
        (
            "#1006F#4PTita, since we're here, why don't\x01",
            "we check out the pump?\x02\x03",

            "We might come up with something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #186
        0x107,
        "#560FOkay, sure!\x02",
    )

    CloseMessageWindow()
    Jump("loc_4323")

    label("loc_42AA")

    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #187
        0x101,
        (
            "#1006F#4PEveryone, since we're here, why\x01",
            "don't we check out the pump?\x02\x03",

            "We might come up with something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4323")


    ChrTalk(    #188
        0x102,
        "#1040F#6PAh, so that's your plan.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4389")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #189
        0x106,
        "#051F#6PGuess there's no helpin' it.\x02",
    )

    CloseMessageWindow()

    label("loc_4389")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43C1")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #190
        0x103,
        "#021F#6PNo objection from me.\x02",
    )

    CloseMessageWindow()

    label("loc_43C1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4405")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #191
        0x108,
        "#070F#6PWell, let's go have a look, then.\x02",
    )

    CloseMessageWindow()

    label("loc_4405")


    ChrTalk(    #192
        0x101,
        "#1001F#4PThat's settled, then. Let's go to the pump shed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2007)
    OP_28(0xC2, 0x4, 0x2)
    OP_28(0xC2, 0x4, 0x8)
    OP_28(0xC2, 0x1, 0x1)
    EventEnd(0x0)

    label("loc_4459")

    Jump("loc_4B29")

    label("loc_445C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44AE")

    ChrTalk(    #193
        0x107,
        (
            "#063FUm, Mrs. Mao...\x02\x03",

            "Is there anything we could help with?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_44F0")

    label("loc_44AE")


    ChrTalk(    #194
        0x101,
        (
            "#1015F#6PHey, Mrs. Mao.\x02\x03",

            "Is there anything we can help with?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44F0")


    ChrTalk(    #195
        0x8,
        (
            "#680F#4PWell.\x02\x03",

            "We've got soldiers patrolling regularly,\x01",
            "so it's not too dangerous here.\x02\x03",

            "If anything, I guess I'd ask if you could\x01",
            "make it so we could fill the baths, but...\x02\x03",

            "#685FWell, no point in asking that, really.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #196
        0x101,
        "#1015F#6PHmmm...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Sounds Hard\x01",               # 0
            "Offer to Help Anyway\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4754")

    ChrTalk(    #197
        0x101,
        (
            "#1007F#6P...Sorry, Mrs. Mao.\x02\x03",

            "#1003FI don't think we can be of any help there...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #198
        0x8,
        (
            "#680F#4PDon't worry about it.\x02\x03",

            "You've got your own jobs you need\x01",
            "to do, I'm sure.\x02\x03",

            "You can put that first.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #199
        0x102,
        "#1035F#6P... Yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0x101,
        "#1025F#6PYes, we'll do that.\x02",
    )

    CloseMessageWindow()
    OP_28(0xC2, 0x1, 0x8000)
    EventEnd(0x0)
    Jump("loc_4B29")

    label("loc_4754")


    ChrTalk(    #201
        0x101,
        (
            "#1006F#6PBut, since we're here, why don't we\x01",
            "have a look?\x02\x03",

            "I feel like we might be able to\x01",
            "offer a bracer-like solution.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #202
        0x102,
        "#1044F#6PEstelle...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x8,
        "#683F#4POh...? What would that be?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #204
        0x101,
        (
            "#1015F#6PHmmm, well.\x02\x03",

            "#1006FFirst, I'd like to borrow the Pump Shed key.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x8,
        "#680F#4PSure, that's fine, but...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #206
        "\x07\x00Received #1034i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_3E(0x40A, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_497B")
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    ChrTalk(    #207
        0x101,
        (
            "#1006F#4PTita, since we're here why\x01",
            "don't we check out the pump?\x02\x03",

            "We might come up with something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #208
        0x107,
        "#560FOkay, sure!\x02",
    )

    CloseMessageWindow()
    Jump("loc_49F3")

    label("loc_497B")

    OP_8C(0x101, 180, 400)
    Sleep(300)

    ChrTalk(    #209
        0x101,
        (
            "#1006F#4PEveryone, since we're here why\x01",
            "don't we check out the pump?\x02\x03",

            "We might come up with something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49F3")


    ChrTalk(    #210
        0x102,
        "#1040F#6PAh, so that's your plan.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A59")
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #211
        0x106,
        "#051F#6PGuess there's no helpin' it.\x02",
    )

    CloseMessageWindow()

    label("loc_4A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4A91")
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #212
        0x103,
        "#021F#6PNo objection from me.\x02",
    )

    CloseMessageWindow()

    label("loc_4A91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4AD5")
    TurnDirection(0x108, 0x101, 400)

    ChrTalk(    #213
        0x108,
        "#070F#6PWell, let's go have a look, then.\x02",
    )

    CloseMessageWindow()

    label("loc_4AD5")


    ChrTalk(    #214
        0x101,
        "#1001F#4PThat's settled, then. Let's go to the pump shed.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2007)
    OP_28(0xC2, 0x4, 0x2)
    OP_28(0xC2, 0x4, 0x8)
    OP_28(0xC2, 0x1, 0x1)
    EventEnd(0x0)

    label("loc_4B29")

    OP_43(0x8, 0x0, 0x6, 0x2)
    Return()

    # Function_11_3ECF end

    def Function_12_4B31(): pass

    label("Function_12_4B31")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B51")
    Call(0, 13)
    Call(0, 14)
    FadeToBright(0, 0)

    label("loc_4B51")

    OP_4A(0x8, 255)
    OP_6D(1600, 250, 5180, 0)
    OP_67(0, 5660, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(315000, 0)
    OP_6E(315, 0)
    SetChrPos(0x101, 3260, 250, 3540, 0)
    SetChrPos(0x102, 2100, 250, 3530, 0)
    SetChrPos(0xF8, 3700, 250, 2250, 0)
    SetChrPos(0xF9, 2250, 250, 2250, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #215
        0x8,
        (
            "#680F#4PGoodness... I didn't think you'd actually\x01",
            "get the pump working.\x02\x03",

            "#681FThanks. I can hardly believe it. Now we can let\x01",
            "people go in the baths as much as they please.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #216
        0x101,
        "#1008F#5PAhaha... I'm glad we could help.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 400)
    Sleep(300)

    ChrTalk(    #217
        0x101,
        "#1006F#2PWell, it was about 90% thanks to Tita, though.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 400)

    ChrTalk(    #218
        0x107,
        (
            "#067F#5PTh-That's not true at all.\x02\x03",

            "#560FI could only upgrade it because you went\x01",
            "out and found what we needed, Estelle.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4E76")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DB9")
    TurnDirection(0xF9, 0x101, 400)
    Jump("loc_4DC0")

    label("loc_4DB9")

    TurnDirection(0xF8, 0x102, 400)

    label("loc_4DC0")


    ChrTalk(    #219
        0x106,
        (
            "#551F#5PStill, this time we really did end\x01",
            "up going all over.\x02\x03",

            "#555FThis Orbal Shutdown Phenomenon is seriously\x01",
            "slowing us down.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E4C():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E4C)
    Sleep(50)

    def lambda_4E5F():
        TurnDirection(0xFE, 0x106, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4E5F)
    Sleep(50)
    TurnDirection(0x107, 0x106, 400)
    Jump("loc_5053")

    label("loc_4E76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E9B")
    TurnDirection(0xF9, 0x101, 400)
    Jump("loc_4EA2")

    label("loc_4E9B")

    TurnDirection(0xF8, 0x102, 400)

    label("loc_4EA2")


    ChrTalk(    #220
        0x103,
        (
            "#025F#5PStill, this time we really did end up\x01",
            "traveling all over the place.\x02\x03",

            "#022FThe Orbal Shutdown Phenomenon is certainly\x01",
            "taking a toll on our time and stamina.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F51():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4F51)
    Sleep(50)

    def lambda_4F64():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4F64)
    Sleep(50)
    TurnDirection(0x107, 0x103, 400)
    Jump("loc_5053")

    label("loc_4F7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5053")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FA0")
    TurnDirection(0xF9, 0x101, 400)
    Jump("loc_4FA7")

    label("loc_4FA0")

    TurnDirection(0xF8, 0x102, 400)

    label("loc_4FA7")


    ChrTalk(    #221
        0x108,
        (
            "#075F#5PStill, we end up going all over to solve\x01",
            "this one.\x02\x03",

            "#072FJust another byproduct of the Orbal\x01",
            "Shutdown Phenomenon.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_502C():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_502C)
    Sleep(50)

    def lambda_503F():
        TurnDirection(0xFE, 0x108, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_503F)
    Sleep(50)
    TurnDirection(0x107, 0x108, 400)

    label("loc_5053")

    WaitChrThread(0x102, 0x1)
    Sleep(200)

    ChrTalk(    #222
        0x102,
        (
            "#1043F#4PVery true.\x02\x03",

            "#1035FTechnology ceasing to function deals severe\x01",
            "damage to a society built on it...\x02\x03",

            "#1042FAt this rate the situation is only going\x01",
            "to get worse.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x102, 400)

    ChrTalk(    #223
        0x107,
        "#063F#5PJoshua...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #224
        0x101,
        (
            "#1006F#2PWell, no need to be so pessimistic.\x02\x03",

            "Even with orbments stopped we managed\x01",
            "to get the pump working.\x02\x03",

            "#1001FPeople can do anything if they put their\x01",
            "minds to it, don't you think?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #225
        0x102,
        "#1044F#3PEstelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x8,
        (
            "#681F#4PHahaha, nicely said.\x02\x03",

            "#680FAnyway, it's a job well done.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5265():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5265)
    Sleep(100)

    def lambda_5278():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5278)
    Sleep(100)

    def lambda_528B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_528B)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52AF")
    OP_8C(0xF9, 0, 400)
    Jump("loc_52B6")

    label("loc_52AF")

    OP_8C(0xF8, 0, 400)

    label("loc_52B6")

    Sleep(300)

    ChrTalk(    #227
        0x8,
        (
            "#680F#4PYou should and go take the first bath for\x01",
            "yourself and relax from your journey.\x02\x03",

            "#681FOh, I know! Here's some special medicinal\x01",
            "tea handed down in my family.\x02\x03",

            "You should drink it when you get out\x01",
            "of the bath. It'll fix you right up.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #228
        "\x07\x00Received #457i x4.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x1C9, 4)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #229
        (
            "\x07\x05And so, Estelle's group took a bath, dined on a feast of\x01",
            "Eastern dishes, and left the Maple Leaf Inn behind them.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_549E")
    OP_31(0x0, 0xFB, 0x0)

    label("loc_549E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54B1")
    OP_31(0x1, 0xFB, 0x0)

    label("loc_54B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54C4")
    OP_31(0x2, 0xFB, 0x0)

    label("loc_54C4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54D7")
    OP_31(0x5, 0xFB, 0x0)

    label("loc_54D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54EA")
    OP_31(0x6, 0xFB, 0x0)

    label("loc_54EA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54FD")
    OP_31(0x7, 0xFB, 0x0)

    label("loc_54FD")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #230
        "#0CQuest #2C[Hot Spring Restoration] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3F(0x40A, 1)
    OP_3F(0x40B, 1)
    OP_28(0xC2, 0x4, 0x10)
    OP_28(0xC2, 0x1, 0x2000)
    OP_28(0xC2, 0x1, 0x4000)
    OP_A2(0x2012)
    ClearMapFlags(0x10000000)
    NewScene("ED6_DT21/T3200   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4B31 end

    def Function_13_557B(): pass

    label("Function_13_557B")

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
        (0, "loc_55F7"),
        (1, "loc_55FD"),
        (SWITCH_DEFAULT, "loc_5603"),
    )


    label("loc_55F7")

    OP_A2(0x1200)
    Jump("loc_5603")

    label("loc_55FD")

    OP_A2(0x1201)
    Jump("loc_5603")

    label("loc_5603")

    Return()

    # Function_13_557B end

    def Function_14_5604(): pass

    label("Function_14_5604")

    ClearMapFlags(0x1)
    OP_6D(106730, -1920, 53920, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_14_5604 end

    def Function_15_565D(): pass

    label("Function_15_565D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #231
        "\x07\x05Outdoor baths this way ⇒\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_565D end

    SaveToFile()

Try(main)
