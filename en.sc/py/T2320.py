from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2320   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2320.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60015",
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
        'Creda',                                # 9
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
        'ED6_DT07/CH01010 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01010P._CP',             # 00
    )

    DeclNpc(
        X                   = -4000,
        Z                   = 500,
        Y                   = 8800,
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


    DeclActor(
        TriggerX            = -4040,
        TriggerZ            = 500,
        TriggerY            = 7530,
        TriggerRange        = 400,
        ActorX              = -4000,
        ActorZ              = 2000,
        ActorY              = 8800,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_F6",           # 00, 0
        "Function_1_F7",           # 01, 1
        "Function_2_F8",           # 02, 2
        "Function_3_FD",           # 03, 3
    )


    def Function_0_F6(): pass

    label("Function_0_F6")

    Return()

    # Function_0_F6 end

    def Function_1_F7(): pass

    label("Function_1_F7")

    Return()

    # Function_1_F7 end

    def Function_2_F8(): pass

    label("Function_2_F8")

    Call(0, 3)
    Return()

    # Function_2_F8 end

    def Function_3_FD(): pass

    label("Function_3_FD")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A")
    OP_A9(0x6E)
    TalkEnd(0x8)
    Return()

    label("loc_11A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B")
    TalkEnd(0x8)
    Return()

    label("loc_12B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_2A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214")

    ChrTalk(    #0
        0x8,
        (
            "Lately, young folk have been coming\x01",
            "to learn cooking from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "After all, old cooking methods don't\x01",
            "need much more than a pot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        (
            "You can make a meal with nothing more\x01",
            "than the fire in your fireplace.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_2A2")

    label("loc_214")


    ChrTalk(    #3
        0x8,
        (
            "Lately, young folk have been coming\x01",
            "to learn cooking from me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "Seems like none of them know how\x01",
            "to handle a fire. Pffft. Kids today!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A2")

    Jump("loc_7F8")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_3ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37D")

    ChrTalk(    #5
        0x8,
        (
            "Lacking orbments doesn't bother me one\x01",
            "whit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "I can put on some firewood if I get cold,\x01",
            "and lamps are fine to keep things lit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "I really don't get why everyone's\x01",
            "making such a fuss.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_3EA")

    label("loc_37D")


    ChrTalk(    #8
        0x8,
        (
            "Lacking orbments doesn't bother me one\x01",
            "whit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "I really don't get why everyone's\x01",
            "making such a fuss.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EA")

    Jump("loc_7F8")

    label("loc_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_521")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_49B")

    ChrTalk(    #10
        0x8,
        (
            "What matters most in an election\x01",
            "is the candidate's character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        (
            "We failed at that last time, so this time\x01",
            "we've got to be very clear on that point.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51E")

    label("loc_49B")

    OP_A2(0x0)

    ChrTalk(    #12
        0x8,
        (
            "What matters most in an election\x01",
            "is the candidate's character.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x8,
        (
            "As long as you don't mistake that,\x01",
            "everything is fine.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51E")

    Jump("loc_7F8")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_703")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_5D8")

    ChrTalk(    #14
        0x8,
        (
            "Zack has plenty of ideas, I'm sure,\x01",
            "but actions are more important than\x01",
            "anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x8,
        (
            "Rather than talking, get to moving,\x01",
            "as they say. That's how I was taught.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_700")

    label("loc_5D8")

    OP_A2(0x0)

    ChrTalk(    #16
        0x8,
        (
            "The village elder seems pretty busy,\x01",
            "with the election coming up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "But I wonder more of what Zack is doing.\x01",
            "Frittering away his time proposing new\x01",
            "'ideas,' no doubt.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "To have the youth not doing any job\x01",
            "would be unthinkable in the old days.\x01",
            "They've gotten soft, I tell you! Soft!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_700")

    Jump("loc_7F8")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_END)), "loc_769")

    ChrTalk(    #19
        0x8,
        (
            "My granddaughter Sadie has a flower\x01",
            "shop in front.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "If you'd like, take a look in.\x02",
    )

    CloseMessageWindow()
    Jump("loc_7F8")

    label("loc_769")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_7F8")

    ChrTalk(    #21
        0x8,
        "I met a traveling priest out front a bit ago.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        (
            "Apparently he's just been assigned here,\x01",
            "but he was so young and... My, oh, my!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F8")

    TalkEnd(0x8)
    Return()

    # Function_3_FD end

    SaveToFile()

Try(main)
