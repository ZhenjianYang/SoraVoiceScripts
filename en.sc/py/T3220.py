from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 蔡斯

    CreateScenaFile(
        FileName            = 'T3220   ._SN',
        MapName             = 'Zeiss',
        Location            = 'T3220.x',
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
        'Sima',                                 # 9
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
        'ED6_DT07/CH01020 ._CH',             # 00
    )

    AddCharChipPat(
        'ED6_DT07/CH01020P._CP',             # 00
    )

    DeclNpc(
        X                   = 2550,
        Z                   = 250,
        Y                   = 4470,
        Direction           = 192,
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
        TriggerX            = 2440,
        TriggerZ            = 250,
        TriggerY            = 2960,
        TriggerRange        = 400,
        ActorX              = 2550,
        ActorZ              = 1750,
        ActorY              = 4470,
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
    OP_A9(0xA0)
    TalkEnd(0x8)
    Return()

    label("loc_11A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12B")
    TalkEnd(0x8)
    Return()

    label("loc_12B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x402, 2)), scpexpr(EXPR_END)), "loc_28A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FF")

    ChrTalk(    #0
        0x8,
        (
            "The hot springs' pump is back in\x01",
            "working order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x8,
        (
            "I suppose one of the technicians from\x01",
            "the central factory must have fixed it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x8,
        "I wish they'd fix the lights while they're at it!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_287")

    label("loc_1FF")


    ChrTalk(    #3
        0x8,
        (
            "The hot springs' pump is back in\x01",
            "working order.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x8,
        (
            "I suppose one of the technicians from\x01",
            "the central factory must have fixed it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_287")

    Jump("loc_A50")

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_489")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C2")

    ChrTalk(    #5
        0x8,
        "Oh. Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x8,
        (
            "Apparently, the airships have stopped,\x01",
            "so I don't have many guests now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x8,
        (
            "You might already know, but I have a\x01",
            "young son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x8,
        "It's been a struggle raising him on my own...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x8,
        (
            "Anyway, we're in a bit of a fix here with no\x01",
            "tourists coming, so please buy something.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    Jump("loc_486")

    label("loc_3C2")


    ChrTalk(    #10
        0x8,
        (
            "You might already know, but I have a\x01",
            "young son.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x8,
        "It's been a struggle raising him on my own...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x8,
        (
            "Anyway, we're in a bit of a fix here with no\x01",
            "tourists coming, so please buy something.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_486")

    Jump("loc_A50")

    label("loc_489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C0, 0)), scpexpr(EXPR_END)), "loc_62E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_532")

    ChrTalk(    #13
        0x8,
        (
            "As long as a few fine guests like you come,\x01",
            "I can keep a roof over my head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x8,
        (
            "Until Quantay's bigger, I just gotta hold on,\x01",
            "little by little...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62B")

    label("loc_532")


    ChrTalk(    #15
        0x8,
        (
            "Phew! Thank Aidios! The baths are\x01",
            "back to normal.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x8,
        "That's a relief, let me tell you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x8,
        (
            "As long as a few fine guests like you come,\x01",
            "I can keep a roof over my head.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x8,
        (
            "Until Quantay's bigger, I just gotta hold on,\x01",
            "little by little...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_62B")

    Jump("loc_A50")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x284, 0)), scpexpr(EXPR_END)), "loc_74F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6AF")

    ChrTalk(    #19
        0x8,
        (
            "My store lives and dies on the patronage\x01",
            "of bathing guests.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x8,
        "If the hot springs are done for, so am I.\x02",
    )

    CloseMessageWindow()
    Jump("loc_74C")

    label("loc_6AF")


    ChrTalk(    #21
        0x8,
        "If the hot springs are done for, so am I.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x8,
        "Please, hurry up and fix it somehow!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x8,
        (
            "My store lives and dies on the patronage\x01",
            "of bathing guests.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_74C")

    Jump("loc_A50")

    label("loc_74F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x282, 6)), scpexpr(EXPR_END)), "loc_934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_806")

    ChrTalk(    #24
        0x8,
        (
            "I read that the non-aggression pact\x01",
            "signing will be at the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x8,
        (
            "It's got nothing to do with commoners\x01",
            "like us, but it's interesting enough to know.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_931")

    label("loc_806")


    ChrTalk(    #26
        0x8,
        (
            "Because of the problem with the springs,\x01",
            "the store's been mostly empty. I've just\x01",
            "been reading the Liberl News to pass time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x8,
        (
            "I read that the non-aggression pact\x01",
            "signing will be at the royal villa.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x8,
        (
            "It's got nothing to do with commoners\x01",
            "like us, but it's interesting enough to know.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_931")

    Jump("loc_A50")

    label("loc_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x281, 2)), scpexpr(EXPR_END)), "loc_A50")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_999")

    ChrTalk(    #29
        0x8,
        "I've got new stuff in, so take a look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x8,
        "We've got lots of great souvenirs.\x02",
    )

    CloseMessageWindow()
    Jump("loc_A50")

    label("loc_999")


    ChrTalk(    #31
        0x8,
        "Ah... Hey, welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x8,
        "I've got new stuff in, so take a look!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x8,
        "Not many customers are coming...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x8,
        (
            "I hope Quantay is doing his job out\x01",
            "there and calling in customers.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_A50")

    TalkEnd(0x8)
    Return()

    # Function_3_FD end

    SaveToFile()

Try(main)
