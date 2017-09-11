from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T1210_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'T1210.x',
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
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    ScpFunction(
        "Function_0_66",           # 00, 0
        "Function_1_918",          # 01, 1
    )


    def Function_0_66(): pass

    label("Function_0_66")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_77C")
    EventBegin(0x0)
    OP_69(0xFE, 0x3E8)
    OP_28(0xE, 0x4, 0x8)
    OP_28(0xE, 0x4, 0x4)
    OP_28(0xE, 0x1, 0x1)
    OP_28(0xE, 0x1, 0x2)
    OP_28(0xE, 0x1, 0x4)
    OP_A2(0x2)
    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #0
        0xFE,
        "Huh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "Might you be the ones from the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "Did you see the request on the\x01",
            "bulletin board?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_22E")

    ChrTalk(    #3
        0x101,
        "#000FYep, we sure did.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #4
        0xFE,
        "This is wonderful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "My name is Reisen, and I guess\x01",
            "you could say that I'm the elder\x01",
            "of this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xFE,
        (
            "As I'm sure you're already aware, there's\x01",
            "been a vicious monster roaming the trail\x01",
            "behind the village.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5")

    label("loc_22E")

    OP_28(0xE, 0x4, 0x2)

    ChrTalk(    #7
        0x101,
        "#000FBulletin board?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #8
        0xFE,
        (
            "I'm called Reisen, and I serve as\x01",
            "the elder of this village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Recently, there's been a vicious\x01",
            "monster appearing on the trail\x01",
            "behind the village.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "So I've requested that the Bracer Guild\x01",
            "send someone to take care of it.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x1, 0x4000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5")

    ChrTalk(    #11
        0x101,
        "#004FEh...?! Really?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x103,
        (
            "#022FIt looks like we should ask him for\x01",
            "some more details about the matter.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5")


    ChrTalk(    #13
        0x102,
        (
            "#012FSo do you know what kind of monster\x01",
            "has taken up residence in the area?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 0)

    ChrTalk(    #14
        0xFE,
        (
            "No, I don't think anyone has gotten\x01",
            "a good look at the thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "However, I think it may be one\x01",
            "which lies in wait for its prey.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "When the mine was active years ago,\x01",
            "this type of monster often appeared\x01",
            "and harassed the workers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x103,
        (
            "#022FI see... So it lies in wait, huh?\x01",
            "It's going to be a bit of a pain\x01",
            "to find then.\x02\x03",

            "It looks like we'll just have to\x01",
            "hit the trail and see if we can\x01",
            "find out where it's hiding.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "After the mine was abandoned and people\x01",
            "stopped going up that way, we had believed\x01",
            "that the monsters had gone into slumber...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xFE,
        (
            "So why in the world is one appearing\x01",
            "now...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #20
        0xFE,
        (
            "It's almost time for us to begin\x01",
            "planting saplings this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        (
            "As a way to keep the villagers from worrying,\x01",
            "I've had Figaro standing guard at the gate\x01",
            "and not told anyone else about the monster.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "Please exterminate the monster\x01",
            "as soon as you can.\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_917")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_809")

    ChrTalk(    #23
        0xFE,
        (
            "It's almost time for us to begin\x01",
            "planting saplings this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xFE,
        (
            "Please try and exterminate the\x01",
            "monster as soon as you can.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_917")

    label("loc_809")

    OP_A2(0x2)

    ChrTalk(    #25
        0xFE,
        "Oh, it's you bracers again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0xFE,
        "Did you have any luck?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x101,
        (
            "#003FI'm sorry, but it may take a bit\x01",
            "longer than we expected.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #28
        0xFE,
        (
            "It's almost time for us to begin\x01",
            "planting saplings this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "Please try and exterminate the\x01",
            "monster as soon as you can.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_917")

    Return()

    # Function_0_66 end

    def Function_1_918(): pass

    label("Function_1_918")

    OP_28(0xE, 0x1, 0x800)
    OP_A2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0xE, 0x0, 0x4)"), scpexpr(EXPR_END)), "loc_9D1")

    ChrTalk(    #30
        0xFE,
        "Oh, it's you bracers again.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Did you have any luck?\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #32
        0x101,
        (
            "#001FHeehee! ♪\x02\x03",

            "You bet we did! We took care of\x01",
            "that old monster!☆\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8F")

    label("loc_9D1")


    ChrTalk(    #33
        0xFE,
        (
            "Might you be the ones from the\x01",
            "Bracer Guild?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        (
            "Did you see the request on the\x01",
            "bulletin board?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #35
        0x101,
        (
            "#001FHeehee! ♪\x02\x03",

            "We already took care of that monster!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8F")

    TurnDirection(0xFE, 0x101, 0)

    ChrTalk(    #36
        0xFE,
        "Oh, this is wonderful news!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "It looks like we'll be able to plant\x01",
            "the saplings without any worries\x01",
            "this year.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "I appreciate everything you've\x01",
            "done for us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "Our village may be a little off the\x01",
            "beaten path, but feel free to visit\x01",
            "any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        (
            "#000FSure, we'll take you up on that\x01",
            "some time.\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_1_918 end

    SaveToFile()

Try(main)
