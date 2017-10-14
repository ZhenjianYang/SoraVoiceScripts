from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2100_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        "Function_1_DB7",          # 01, 1
        "Function_2_1101",         # 02, 2
        "Function_3_2603",         # 03, 3
        "Function_4_32D9",         # 04, 4
        "Function_5_381C",         # 05, 5
        "Function_6_3FDD",         # 06, 6
        "Function_7_403B",         # 07, 7
        "Function_8_4099",         # 08, 8
        "Function_9_40FC",         # 09, 9
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x245, 3)), scpexpr(EXPR_END)), "loc_837")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5")
    Call(1, 2)
    Jump("loc_834")

    label("loc_D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_152")

    ChrTalk(    #0
        0xFE,
        (
            "We're in the middle of an election,\x01",
            "so there ain't too many customers\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "Please, take your time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_834")

    label("loc_152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_281")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_200")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1C0")

    ChrTalk(    #2
        0xFE,
        "Ho ho ho! Solved the case, did you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Did my testimony help at all?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FD")

    label("loc_1C0")

    OP_A2(0x8)

    ChrTalk(    #4
        0xFE,
        "Ho ho ho! Solved the case, did you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "Good, good.\x02",
    )

    CloseMessageWindow()

    label("loc_1FD")

    Jump("loc_27E")

    label("loc_200")


    ChrTalk(    #6
        0xFE,
        (
            "However the election turns out,\x01",
            "I'll be on the job here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "That's how it's been until now,\x01",
            "and it ain't gonna change.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E")

    Jump("loc_834")

    label("loc_281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_4DE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_2F0")

    ChrTalk(    #8
        0xFE,
        (
            "If you need a boat, come talk to\x01",
            "me any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        "I'll give you a lift, free of charge.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB")

    label("loc_2F0")

    OP_A2(0x8)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_452")

    ChrTalk(    #10
        0xFE,
        (
            "Ah-ha! You're the one who just\x01",
            "used my boat, aren't you? Didn't\x01",
            "think I'd see you again so soon.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "How about it? Did the inspiration you\x01",
            "needed for your song strike you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x104,
        (
            "#030FThanks to you, a masterpiece\x01",
            "was born.\x02\x03",

            "Why, one could say these waters\x01",
            "gave rise to my finest work yet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        "Ho ho ho! That's what I like to hear.\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DB")

    label("loc_452")


    ChrTalk(    #14
        0xFE,
        (
            "There was some sort of fuss over\x01",
            "by the bridge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "And just as quickly as I'd heard it,\x01",
            "the fuss died down. Wonder what\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DB")

    Jump("loc_834")

    label("loc_4DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_53F")

    ChrTalk(    #16
        0xFE,
        "Oh, what's all that hollerin' for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "Something's happening over on\x01",
            "the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_834")

    label("loc_53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_5D0")

    ChrTalk(    #18
        0xFE,
        (
            "I met someone who wanted to set\x01",
            "sail on a boat to nail down a song...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "That is one refined young buck,\x01",
            "I tell you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B0")

    label("loc_5D0")

    OP_A2(0x8)

    ChrTalk(    #20
        0xFE,
        "I just lent out my boat.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "Think he was a traveler, but he was\x01",
            "one refined-looking young buck,\x01",
            "I tell you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Somethin' about needing the open\x01",
            "waters to inspire a song or somethin'...\x01",
            "That was the gist, anyway.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B0")

    Jump("loc_834")

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_788")

    ChrTalk(    #23
        0xFE,
        (
            "I do know the election's important, but\x01",
            "I wish they'd stop yellin' so much!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Everyone would know what they're saying\x01",
            "if they just glanced at a guldurned poster.\x01",
            "Plenty enough of 'em around!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_834")

    label("loc_788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 6)), scpexpr(EXPR_END)), "loc_834")

    ChrTalk(    #25
        0xFE,
        (
            "We're in the middle of an election,\x01",
            "so there ain't too many customers\x01",
            "right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        (
            "Sure is boring... Wish I could do some\x01",
            "fishin' while it's slow like this.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_834")

    Jump("loc_DB3")

    label("loc_837")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89D")

    ChrTalk(    #27
        0xFE,
        "Oh, what's all that hollerin' for?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "Something's happening over on\x01",
            "the bridge.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DB3")

    label("loc_89D")

    TurnDirection(0xFE, 0x101, 0)
    OP_A2(0x122B)
    OP_A2(0x9)

    ChrTalk(    #29
        0xFE,
        (
            "Now, who are you again...?\x01",
            "Oh, been quite a while, young lady!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACF")

    ChrTalk(    #30
        0x101,
        (
            "#1000FHow are you, sir?\x02\x03",

            "You remember us, right? You lent\x01",
            "us your boat when the bridge was up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x105,
        "#048FYou really saved us then.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x105, 400)

    ChrTalk(    #32
        0xFE,
        "Naw, it was no skin off my back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        "So, come back to ride again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1007FWish I could, but I've got some\x01",
            "work to do.\x02\x03",

            "We're investigating the case that\x01",
            "happened at the hotel.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #35
        0xFE,
        "Oh, sounds rough.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "If I can be of any help, feel free\x01",
            "to ask me what you like.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1006FWill do, sir!\x02",
    )

    CloseMessageWindow()
    Call(1, 2)
    Jump("loc_DB3")

    label("loc_ACF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BAF")

    ChrTalk(    #38
        0x101,
        (
            "#1000FOh, how've you been?\x02\x03",

            "You remember us, right? You lent\x01",
            "us your boat when the bridge was up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x105,
        (
            "#047FIf we didn't have transport then,\x01",
            "we would have been in serious\x01",
            "trouble.\x02\x03",

            "Thank you very much.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C46")

    label("loc_BAF")


    ChrTalk(    #40
        0x101,
        (
            "#1000FOh, how've you been?\x02\x03",

            "You remember us, right? You lent\x01",
            "us your boat when we were going\x01",
            "after Clem.\x02\x03",

            "You saved our butts, sir! Thanks again.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C46")


    ChrTalk(    #41
        0xFE,
        "Naw, it was no skin off my back.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        "So, come back to ride again?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1016FWish we could, but we're here on duty.\x02\x03",

            "Thankfully not as urgent as last time,\x01",
            "haha.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "Oh, is that right? Take it easy, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "We're in the middle of an election, so there\x01",
            "ain't too many customers right now. Think\x01",
            "you can take things easy this time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        "#1000FWill do, sir!\x02",
    )

    CloseMessageWindow()

    label("loc_DB3")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_DB7(): pass

    label("Function_1_DB7")

    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 16, -1, -1)

    AnonymousTalk(    #47
        "\x18What would you like to ask about?\x02",
    )

    OP_CC(0x0, 0x0, 0xA, 0xA, 0x1)
    OP_CC(0x1, 0x0, "Kuper")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_E68")
    OP_CC(0x1, 0x0, "Sounds")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF0), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_E9E")
    OP_CC(0x1, 0x0, "Anger")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFF0F), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_E9E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_ED4")
    OP_CC(0x1, 0x0, "Herio")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFF0FF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ED4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_F0A")
    OP_CC(0x1, 0x0, "Lunch")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFF0FFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_F48")
    OP_CC(0x1, 0x0, "The Bell Toll")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFF0FFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x800)"), scpexpr(EXPR_END)), "loc_F84")
    OP_CC(0x1, 0x0, "Cleaning Up")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xF0FFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_FBB")
    OP_CC(0x1, 0x0, "Belden")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFFFFFF), scpexpr(EXPR_AND), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IMUL), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_FBB")

    OP_CC(0x1, 0x0, "Stop")
    OP_CC(0x2, 0x0)
    MenuEnd(0x0)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_FFA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_101E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1042")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_1042")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1066")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_1066")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_108A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x10000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_10AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x100000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_10D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1000000), scpexpr(EXPR_IDIV), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_AND), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1100")

    label("loc_10F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1100")

    Return()

    # Function_1_DB7 end

    def Function_2_1101(): pass

    label("Function_2_1101")

    Call(1, 1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_112E"),
        (1, "loc_11C5"),
        (2, "loc_1505"),
        (3, "loc_1567"),
        (4, "loc_16FC"),
        (5, "loc_1FA7"),
        (6, "loc_2472"),
        (7, "loc_259D"),
        (SWITCH_DEFAULT, "loc_25FF"),
    )


    label("loc_112E")

    OP_28(0x6A, 0x1, 0x100)

    ChrTalk(    #48
        0xFE,
        (
            "Yeah, I know him. He's that young\x01",
            "fella workin' at the harbor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "Like everyone else these days, he's\x01",
            "been involved with the election.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2602")

    label("loc_11C5")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_12A2")

    ChrTalk(    #50
        0xFE,
        (
            "That big ol' sound happened at about\x01",
            "the same time as the bell rung.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        (
            "Hmm? I thought about it for a moment,\x01",
            "but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        (
            "I was hungry, so I didn't pay it much\x01",
            "mind and went on to the Lavantar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1502")

    label("loc_12A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_1353")

    ChrTalk(    #53
        0xFE,
        (
            "Hmm... Memory's kinda fuzzy, but\x01",
            "I did hear a loud noise from above.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "It was a impressive sound, like\x01",
            "something had run into something\x01",
            "else with a smack.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1502")

    label("loc_1353")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_28(0x69, 0x1, 0x1)

    ChrTalk(    #55
        0xFE,
        "Oh, a sound? Hmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "Thinking about it, I did hear a loud\x01",
            "noise from above.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1004FAbove from here?\x01",
            "You mean the balcony?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #58
        0xFE,
        "Probably around there, yeah.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "It was a impressive sound, like\x01",
            "something had run into something\x01",
            "else with a smack.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "Can't recall exactly when I'd\x01",
            "heard it, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x101,
        (
            "#1015FThat's too bad...\x02\x03",

            "#1006FStill, this is all good stuff to know.\x02\x03",

            "Thanks, sir.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x69, 0x1, 0x4)

    label("loc_1502")

    Jump("loc_2602")

    label("loc_1505")

    OP_28(0x6A, 0x1, 0x100)

    ChrTalk(    #62
        0xFE,
        "Oh, was Kuper that angry?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "Well, youngsters get worked up so\x01",
            "easily these days.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2602")

    label("loc_1567")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_15E7")

    ChrTalk(    #64
        0xFE,
        (
            "Herio's that young merchant fella,\x01",
            "yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xFE,
        (
            "From the looks of him, he's the\x01",
            "city type. Quiet, too.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F9")

    label("loc_15E7")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #66
        0xFE,
        (
            "Herio's that young merchant fella,\x01",
            "yeah?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "If he wants to be a merchant, I think\x01",
            "he needs to have a bit more 'oomph!'\x01",
            "to him, ya hear me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0xFE,
        (
            "He's got 'gullible' written all over him.\x01",
            "He'll get people rippin' him off at every\x01",
            "turn if he doesn't shape up.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F9")

    Jump("loc_2602")

    label("loc_16FC")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_17D2")

    ChrTalk(    #69
        0xFE,
        (
            "I always listen for bell toll to head\x01",
            "to the Lavantar for lunch.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "No one was in the hotel basement\x01",
            "when I'd passed through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "When I got back, though, I saw\x01",
            "Norman's son down there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA4")

    label("loc_17D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6A, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1B1B")
    OP_28(0x6A, 0x1, 0x20)

    ChrTalk(    #72
        0xFE,
        "I went to the Lavantar for lunch today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        (
            "Always been in the habit of going\x01",
            "out to lunch as soon as I hear the\x01",
            "bell toll.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x101,
        (
            "#1011FSounds like a nice enough routine.\x02\x03",

            "#1015FYou have to go through the hotel\x01",
            "to get there, though, right?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #75
        0xFE,
        "Yep, that I do.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "I can't fly across the sea, now, can I?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x101,
        (
            "#1016FAhaha, good point.\x02\x03",

            "#1000F...So did you see anyone in\x01",
            "the hotel at the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        (
            "Well, Ernest was on the first floor,\x01",
            "of course, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "The rest was real quiet.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0x101,
        "#1011FHuh...? There was no one there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Yeah, I'd say so. The basement and\x01",
            "first floor were both pretty quiet when\x01",
            "I'd passed through.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        (
            "Norman's son was there when\x01",
            "I came back, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1015FNorman's son...? Norman's... Oh!\x01",
            "You mean Belden.\x02\x03",

            "#1006FYeah, that's more than enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        "No, no, it was nothing.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FA4")

    label("loc_1B1B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1BA8")

    ChrTalk(    #85
        0xFE,
        "I went to eat at the Lavantar today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Always been in the habit of going\x01",
            "out to lunch as soon as I hear the\x01",
            "bell toll.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FA4")

    label("loc_1BA8")

    OP_28(0x69, 0x1, 0x40)

    ChrTalk(    #87
        0xFE,
        "About lunch?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        "I went to eat at the Lavantar today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "Always been in the habit of going\x01",
            "out to lunch as soon as I hear the\x01",
            "#4Cbell toll.#0C\x02",
        )
    )

    OP_22(0x11, 0x0, 0x64)
    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1011FThe 'bell toll'?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #91
        0x105,
        (
            "#040FThe bell on the Langland Bridge.\x02\x03",

            "Remember? It rang when the bridge\x01",
            "went up.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #92
        0x101,
        (
            "#1018FOh, yeah!\x02\x03",

            "Yeah, yeah, it did ring.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xFE,
        (
            "It always rings at certain times,\x01",
            "see. I use it in place of a clock.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #94
        0x101,
        (
            "#1000FThat's sure convenient.\x02\x03",

            "Kinda big to use in place of a clock,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x105,
        (
            "#040FHey, Estelle?\x02\x03",

            "It might be good to ask some\x01",
            "people about the bell toll.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #96
        0x101,
        "#1004FHuh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x105,
        (
            "#040FThey should be able to clearly\x01",
            "remember the sound of a bell\x01",
            "ringing.\x02\x03",

            "It might act as a guidepost for their\x01",
            "memory, like with Mr. Murray.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1000FAhhhh, I get it.\x02\x03",

            "#1001FNice, Kloe. Very intellectual advice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x105,
        "#048FHeehee, you flatter me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "Not sure what you two are gigglin'\x01",
            "about, but glad I was able to help.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xFE, 400)

    ChrTalk(    #101
        0x101,
        (
            "#1006FYou sure were!\x02\x03",

            "Okay, let's go ask around!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x105,
        "#041FRight!\x02",
    )

    CloseMessageWindow()

    label("loc_1FA4")

    Jump("loc_2602")

    label("loc_1FA7")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x80)"), scpexpr(EXPR_END)), "loc_2099")

    ChrTalk(    #103
        0xFE,
        (
            "That big sound I heard was right\x01",
            "when the bell went off, like it was\x01",
            "timed or somethin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0xFE,
        (
            "I remember takin' pause when it\x01",
            "happened.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0xFE,
        (
            "I was hungry, though, so I just ignored\x01",
            "it and headed over to the Lavantar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_2099")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x69, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2404")
    OP_28(0x69, 0x1, 0x80)

    ChrTalk(    #106
        0xFE,
        "It was the Langland Bridge bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "We citizens of Ruan hear it on daily\x01",
            "basis, I'll have you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xFE,
        "Speaking of the sound of a bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1002FDid you remember something?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #110
        0xFE,
        (
            "No, you... You asked about it\x01",
            "a second ago, didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "That big sound.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#1004FAh, the sound? Like something\x01",
            "smacking into something, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "Yeah, that thing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "Well, I remember something now!\x01",
            "That sound happened as if it were\x01",
            "timed to the bell, at least to my ears.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x101,
        (
            "#1015FTimed to the bell...?\x02\x03",

            "So basically, you heard the sound\x01",
            "of the bell at roughly the same time\x01",
            "as that big sound?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "Well, if you wanna make it sound all\x01",
            "boring, yeah.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0x105,
        (
            "#042FIf... If that sound was something\x01",
            "caused by the criminal...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x101,
        (
            "#1002FThen someone without an alibi\x01",
            "when the bell rang is the criminal.\x02\x03",

            "Yeah, we should check out people\x01",
            "we suspect.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_246F")

    label("loc_2404")


    ChrTalk(    #119
        0xFE,
        "It was the Langland Bridge bell.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "We citizens of Ruan hear it on daily\x01",
            "basis, I'll have you know.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_246F")

    Jump("loc_2602")

    label("loc_2472")

    OP_28(0x6A, 0x1, 0x100)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_250D")

    ChrTalk(    #121
        0xFE,
        "I wonder who cleared up the plates.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "I sure as heck don't know!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "I was enjoying a nice, warm meal\x01",
            "over at the Lavantar.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_259A")

    label("loc_250D")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #124
        0xFE,
        (
            "Someone cleaned up the plates\x01",
            "for Ernest?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        (
            "Ho ho ho! It's a rare thing to find\x01",
            "someone so considerate of others\x01",
            "nowadays.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_259A")

    Jump("loc_2602")

    label("loc_259D")

    OP_28(0x6A, 0x1, 0x100)

    ChrTalk(    #126
        0xFE,
        "By 'Belden,' do you mean that kid?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0xFE,
        (
            "He wasn't in the basement,\x01",
            "I'm pretty sure.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2602")

    label("loc_25FF")

    Jump("loc_2602")

    label("loc_2602")

    Return()

    # Function_2_1101 end

    def Function_3_2603(): pass

    label("Function_3_2603")

    EventBegin(0x0)
    SetChrPos(0x101, 65180, 240, 94310, 90)
    SetChrPos(0xF7, 64550, 0, 95280, 90)
    SetChrPos(0x104, 64319, 0, 93660, 90)
    SetChrPos(0x127, 63690, 170, 94700, 90)
    OP_6D(65440, 260, 94110, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0x10, 0x14)
    OP_73(0x10)
    Sleep(750)
    SetChrPos(0x31, 69180, 500, 93590, 0)
    ClearChrFlags(0x31, 0x80)
    OP_8E(0x31, 0x1026D, 0x1F4, 0x16F22, 0x7D0, 0x0)
    Sleep(1000)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C3B")

    ChrTalk(    #128
        0x31,
        (
            "Thank you for your time.\x01",
            "I know you're quite busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0x31,
        "The children were overjoyed.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x67, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_2765")

    ChrTalk(    #130
        0x31,
        "That was a wonderful lecture!\x02",
    )

    CloseMessageWindow()

    label("loc_2765")


    ChrTalk(    #131
        0x101,
        (
            "#1001FHaha, thanks.\x02\x03",

            "I was pretty nervous before I did it,\x01",
            "but if they had fun, then it was worth it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x31,
        (
            "I do apologize for cutting things\x01",
            "short, but I have more classes.\x01",
            "If you'll pardon me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x31,
        (
            "Should the chance come again,\x01",
            "I would love to have you back for\x01",
            "another talk.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #134
        0x101,
        "#1006FSure thing.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x31, 0x10E3C, 0x1F4, 0x16D96, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x80)
    Sleep(500)
    OP_72(0x10, 0x800)
    OP_6F(0x10, 20)
    OP_70(0x10, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x10)
    OP_71(0x10, 0x800)

    def lambda_28DA():
        OP_6D(64560, 0, 94340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_28DA)
    Sleep(2000)
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2930")

    ChrTalk(    #135
        0x106,
        "#051FSeems you managed things just fine.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2957")

    label("loc_2930")


    ChrTalk(    #136
        0x103,
        "#021FSeems you managed just fine.\x02",
    )

    CloseMessageWindow()

    label("loc_2957")

    OP_8C(0x101, 270, 400)

    ChrTalk(    #137
        0x101,
        "#1015FPhew! Somehow...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #138
        0x104,
        (
            "#031FNo need to be so humble.\x02\x03",

            "I witnessed your performance.\x01",
            "You were a fantastic teacher.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x101,
        (
            "#1008FAww, c'mon! R-Really...?\x02\x03",

            "#1003F...Still, it made me think about just\x01",
            "how much I don't know.\x02\x03",

            "Every time they asked for details,\x01",
            "I started panicking.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2B12")

    ChrTalk(    #140
        0x106,
        (
            "#053FYou just gotta keep working at it,\x01",
            "that's all.\x02\x03",

            "No one's gonna want anything\x01",
            "from a bracer that doesn't even\x01",
            "know the code.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B92")

    label("loc_2B12")


    ChrTalk(    #141
        0x103,
        (
            "#026FWell, just make sure to work hard\x01",
            "from now on.\x02\x03",

            "#027FNo one's going to trust a bracer\x01",
            "who doesn't even know the code.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B92")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #142
        0x101,
        (
            "#1015FYeah...\x02\x03",

            "#1002FI'll keep working at it. I promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #143
        "Quest #2C[Sunday School Lecturer] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jump("loc_32D4")

    label("loc_2C3B")


    ChrTalk(    #144
        0x31,
        "Phew! Th-Thanks for your help today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x31,
        "The children were certainly happy, but...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x31,
        (
            "If you don't mind me saying, you might\x01",
            "want to consider hitting the books a little\x01",
            "harder yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #147
        0x101,
        "#1007F...I-I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x31,
        (
            "A class like that could hardly gain\x01",
            "the children's trust.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x31,
        (
            "Bracers are the object of much adoration,\x01",
            "so please take into consideration who\x01",
            "you're representing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x101,
        "#1007FO-Of course... I'll keep that in mind.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x31,
        (
            "All right, I still have class, so if\x01",
            "you'll pardon me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0x31,
        (
            "Should the chance come up,\x01",
            "I hope we can see you again.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_8E(0x31, 0x10E3C, 0x1F4, 0x16D96, 0x7D0, 0x0)
    SetChrFlags(0x31, 0x80)
    Sleep(500)
    OP_72(0x10, 0x800)
    OP_6F(0x10, 20)
    OP_70(0x10, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0x10)
    OP_71(0x10, 0x800)

    def lambda_2ED1():
        OP_6D(64560, 0, 94340, 2000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2ED1)
    Sleep(2000)
    TurnDirection(0xF7, 0x101, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2F90")

    ChrTalk(    #153
        0x106,
        "#057F...Just what kind of class did you do?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #154
        0x104,
        (
            "#031FI took a peek once things were underway...\x02\x03",

            "It was truly a spectacle to behold.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3020")

    label("loc_2F90")


    ChrTalk(    #155
        0x103,
        (
            "#025F*sigh* That was certainly...incredible.\x01",
            "In a way.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #156
        0x104,
        (
            "#031FI enjoyed it far more than I imagined\x01",
            "I would. Truly entertaining.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3020")


    ChrTalk(    #157
        0x127,
        "#151FYeah, that was reeeally interesting!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)
    OP_8C(0x101, 270, 400)

    ChrTalk(    #158
        0x101,
        (
            "#1022FAhhh, stop saying that! I get it! I get it!\x01",
            "I'm trying to move on!\x02\x03",

            "#1009FUuuuugh, I know! I'll study, okay?\x02\x03",

            "I'm gonna make it so I can rattle off\x01",
            "the whole damn code in a single breath!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_31BD")

    ChrTalk(    #159
        0x106,
        (
            "#053FWell, uh, just keep working at it.\x02\x03",

            "No one's gonna want anything from\x01",
            "a bracer that doesn't even know the\x01",
            "code.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_322B")

    label("loc_31BD")


    ChrTalk(    #160
        0x103,
        (
            "#026FWell, be sure to keep at it.\x02\x03",

            "#027FNo one's going to trust a bracer\x01",
            "who doesn't even know the code.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_322B")


    ChrTalk(    #161
        0x101,
        (
            "#1007F*sigh* Yeah, yeah.\x02\x03",

            "#1002FI'll keep working at it. I promise.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x106, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #162
        "Quest #2C[Sunday School Lecturer] #0Cfailed...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    label("loc_32D4")

    OP_30(0x0)
    EventEnd(0x0)
    Return()

    # Function_3_2603 end

    def Function_4_32D9(): pass

    label("Function_4_32D9")

    EventBegin(0x0)
    SetChrPos(0x2F, 28180, 0, 90850, 325)
    OP_4A(0x2F, 255)
    OP_6D(22810, 0, 94820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_334C")
    AddParty(0x5, 0xF7, 0xFF)
    SetChrPos(0x106, 17370, 0, 97650, 24)
    Jump("loc_3368")

    label("loc_334C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3368")
    AddParty(0x2, 0xF7, 0xFF)
    SetChrPos(0x103, 17370, 0, 97650, 24)

    label("loc_3368")

    AddParty(0x3, 0xFF, 0xFF)
    SetChrPos(0x104, 17370, 0, 97650, 24)
    SetChrPos(0x101, 17370, 0, 97650, 24)
    SetChrPos(0x105, 17370, 0, 97650, 24)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0xA, 0x1D)
    OP_73(0xA)
    Sleep(400)
    OP_43(0x101, 0x1, 0x1, 0x8)
    Sleep(500)
    OP_43(0x105, 0x1, 0x1, 0x9)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_33EB")
    OP_43(0x106, 0x1, 0x1, 0x6)
    Jump("loc_33F9")

    label("loc_33EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_33F9")
    OP_43(0x103, 0x1, 0x1, 0x6)

    label("loc_33F9")

    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x7)
    Sleep(400)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 29)
    OP_70(0xA, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_71(0xA, 0x800)
    WaitChrThread(0x104, 0x1)
    Sleep(600)

    ChrTalk(    #163
        0x101,
        (
            "#1000F#2PPhew! Well, that's done and over\x01",
            "with. Finally.\x02\x03",

            "I wouldn't have dreamed it would\x01",
            "end like that, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x104,
        (
            "#030FTruth is always stranger than fiction.\x02\x03",

            "#031FHowever, as your valued assistant,\x01",
            "I take great pride in our completion\x01",
            "of this most puzzling assignment.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #165
        0x101,
        "#1019F#2PYou didn't do a damn thing.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #166
        0x101,
        (
            "#1006F#2POh, but I really appreciate your help,\x01",
            "Kloe!\x02\x03",

            "You gave a ton of good advice. It was\x01",
            "a big help during the investigation.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #167
        0x105,
        (
            "#048FI'm always happy to help.\x02\x03",

            "There's no need to thank me,\x01",
            "though, Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #168
        0x101,
        (
            "#1008F#2PRight. I guess you two are our\x01",
            "support staff already, aren't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3716")

    ChrTalk(    #169
        0x106,
        (
            "#050FYep. We'll have you do what needs\x01",
            "to be done.\x02\x03",

            "Okay, let's get going.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3774")

    label("loc_3716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3774")

    ChrTalk(    #170
        0x103,
        (
            "#020FIndeed. We'll have you do what\x01",
            "needs to be done.\x02\x03",

            "All right, let's head out.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3774")

    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #171
        0x101,
        "#1006F#2PNext up is the Zeiss region!\x02",
    )

    CloseMessageWindow()
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #172
        "Quest #CR#[Election Office Assault] #CW#completed!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x69, 0x1, 0x8000)
    OP_28(0x69, 0x4, 0x10)
    EventEnd(0x0)
    OP_4B(0x2F, 255)
    Return()

    # Function_4_32D9 end

    def Function_5_381C(): pass

    label("Function_5_381C")

    EventBegin(0x0)
    SetChrPos(0x2F, 28180, 0, 90850, 325)
    OP_4A(0x2F, 255)
    OP_6D(22810, 0, 94820, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_387E")
    AddParty(0x5, 0xF7, 0xFF)
    Jump("loc_3889")

    label("loc_387E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3889")
    AddParty(0x2, 0xF7, 0xFF)

    label("loc_3889")

    SetChrPos(0xF7, 17370, 0, 97650, 24)
    AddParty(0x3, 0xFF, 0xFF)
    SetChrPos(0x104, 17370, 0, 97650, 24)
    SetChrPos(0x101, 24000, 0, 94500, 180)
    SetChrPos(0x105, 24000, 0, 93300, 0)
    Sleep(1000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_70(0xA, 0x1D)
    OP_73(0xA)
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    def lambda_390C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_390C)
    Sleep(50)

    def lambda_391F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_391F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3938")
    OP_43(0x106, 0x1, 0x1, 0x6)
    Jump("loc_3946")

    label("loc_3938")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3946")
    OP_43(0x103, 0x1, 0x1, 0x6)

    label("loc_3946")

    Sleep(500)
    OP_43(0x104, 0x1, 0x1, 0x7)
    WaitChrThread(0x104, 0x1)
    OP_72(0xA, 0x800)
    OP_6F(0xA, 29)
    OP_70(0xA, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    OP_71(0x0, 0x800)
    Sleep(600)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_39B7")

    ChrTalk(    #173
        0x106,
        (
            "#050FSorry for the wait.\x02\x03",

            "...Now, let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39F6")

    label("loc_39B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_39F6")

    ChrTalk(    #174
        0x103,
        (
            "#020FSorry to keep you waiting.\x02\x03",

            "...Now, let's go.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39F6")


    ChrTalk(    #175
        0x101,
        "#1002F#2PSo who was the criminal, anyway?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0x104,
        "#031FHeh heh, well, you see...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3A6B")

    ChrTalk(    #177
        0x106,
        "#057FHey, shut it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A8D")

    label("loc_3A6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3A8D")

    ChrTalk(    #178
        0x103,
        "#026FNo, no, Olivier.\x02",
    )

    CloseMessageWindow()

    label("loc_3A8D")


    ChrTalk(    #179
        0x101,
        "#1009F#2PAww, why? Why can't you tell me?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3B70")

    ChrTalk(    #180
        0x106,
        (
            "#050FWe have a duty of confidentiality.\x01",
            "You should know that.\x02\x03",

            "Without an official reason, details of\x01",
            "our work are forbidden to be revealed.\x02\x03",

            "Even to other bracers.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C16")

    label("loc_3B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3C16")

    ChrTalk(    #181
        0x103,
        (
            "#022FWe have a duty of confidentiality,\x01",
            "I'm afraid.\x02\x03",

            "Without an official reason, details of\x01",
            "our job are forbidden to be revealed.\x02\x03",

            "Even to other bracers.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C16")


    ChrTalk(    #182
        0x101,
        "#1007F#2PAll right. I get...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xF7, 400)

    ChrTalk(    #183
        0x105,
        "#042FVery strict rules, indeed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x105, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3D0A")

    ChrTalk(    #184
        0x106,
        (
            "#050FIt's so people can trust us to handle\x01",
            "delicate business.\x02\x03",

            "#552FThat's why those with loose lips\x01",
            "aren't well suited to this line of work...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D97")

    label("loc_3D0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3D97")

    ChrTalk(    #185
        0x103,
        (
            "#027FIt's so people can trust us to handle\x01",
            "business discretely.\x02\x03",

            "This line of work's not well suited to\x01",
            "those with loose lips...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D97")


    ChrTalk(    #186
        0x104,
        (
            "#033FHm? I feel the unwavering heat of\x01",
            "many eyes upon my person...\x02\x03",

            "#035FHow truly reprehensible! My lips are\x01",
            "far from 'loose.'\x02\x03",

            "They are, however, smooth and\x01",
            "shapely like the bubbles of a high-\x01",
            "class champagne. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #187
        0x101,
        (
            "#1019F#2PMore like your brain is made of bubbles.\x02\x03",

            "#1015FAnyway, if I knew it was going to turn\x01",
            "out this way I would have kept at it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3F6B")

    ChrTalk(    #188
        0x106,
        (
            "#053FWell, there's a lesson for you:\x01",
            "don't abandon your work.\x02\x03",

            "#050FAll right, let's go.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD6")

    label("loc_3F6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3FD6")

    ChrTalk(    #189
        0x103,
        (
            "#020FWell, always remember to see your\x01",
            "job through to the end, Estelle.\x02\x03",

            "Now, let's get going.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD6")

    EventEnd(0x0)
    OP_4B(0x2F, 255)
    Return()

    # Function_5_381C end

    def Function_6_3FDD(): pass

    label("Function_6_3FDD")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 94200, 86)

    def lambda_3FFF():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FFF)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x57F8, 0x0, 0x17124, 0x5DC, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_6_3FDD end

    def Function_7_403B(): pass

    label("Function_7_403B")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 93800, 86)

    def lambda_405D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_405D)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x56B8, 0x0, 0x16D1E, 0x5DC, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_7_403B end

    def Function_8_4099(): pass

    label("Function_8_4099")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 94200, 86)

    def lambda_40BB():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40BB)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x5DC0, 0x0, 0x17124, 0x5DC, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_8_4099 end

    def Function_9_40FC(): pass

    label("Function_9_40FC")

    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xFE, 19260, 1200, 93800, 86)

    def lambda_411E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_411E)
    OP_90(0xFE, 0x5DC, 0x0, 0x0, 0x5DC, 0x0)
    OP_8E(0xFE, 0x5C94, 0x0, 0x16D1E, 0x5DC, 0x0)
    Sleep(200)
    OP_8C(0xFE, 270, 400)
    Return()

    # Function_9_40FC end

    SaveToFile()

Try(main)
