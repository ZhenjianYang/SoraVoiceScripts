from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'C0403_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/C0403_1 ._SN',
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
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -6090, 250, 1060, 90)
    SetChrPos(0x103, -6070, 250, 2780, 180)
    SetChrPos(0xF8, -8390, 250, 160, 90)
    SetChrPos(0xF9, -7890, 250, 2110, 135)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, -8390, 250, 160, 90)
    SetChrPos(0xF8, -7890, 250, 2110, 135)

    label("loc_124")

    OP_6D(-6780, 250, 1000, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0xFA), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_22E")
    Sleep(1000)
    OP_44(0x8, 0x1)
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B0")

    def lambda_194():

        label("loc_194")

        OP_97(0x8, 0xFFFFF060, 0x3E8, 0x57E40, 0x1B58, 0x1)
        OP_48()
        Jump("loc_194")

    QueueWorkItem2(0x8, 1, lambda_194)
    Jump("loc_1CF")

    label("loc_1B0")


    def lambda_1B6():

        label("loc_1B6")

        OP_97(0x8, 0xFFFFF060, 0x3E8, 0xFFFA81C0, 0x1B58, 0x1)
        OP_48()
        Jump("loc_1B6")

    QueueWorkItem2(0x8, 1, lambda_1B6)

    label("loc_1CF")

    SetChrChipByIndex(0x8, 11)
    ClearChrFlags(0x8, 0x400)
    SetChrFlags(0x8, 0x4)
    OP_22(0x15B, 0x0, 0x64)
    OP_22(0x8C, 0x0, 0x64)

    label("loc_1E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_220")
    OP_51(0x8, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC8), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2328), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_218")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Jump("loc_220")

    label("loc_218")

    Sleep(15)
    Jump("loc_1E8")

    label("loc_220")

    OP_44(0x8, 0x1)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x4)

    label("loc_22E")

    WaitChrThread(0x8, 0x1)
    OP_82(0x0, 0x0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x07\x00Found #564i. \x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x234, 1)

    ChrTalk(    #1
        0x101,
        (
            "#1004FA ring?\x02\x03",

            "Why would something\x01",
            "like this be here?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x72, 0x0, 0x8)"), scpexpr(EXPR_END)), "loc_403")

    ChrTalk(    #2
        0x103,
        (
            "#022F...\x02\x03",

            "About that bird just now...\x02\x03",

            "That was a crow, I believe.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #3
        0x101,
        (
            "#4P#1002FMaybe.\x02\x03",

            "It sure looked like one,\x01",
            "but what does--\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #4
        0x101,
        (
            "#4P#1020F...Oh!\x02\x03",

            "Isn't this Armand's ring?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)

    ChrTalk(    #5
        0x103,
        (
            "#022FIt's very, very likely.\x02\x03",

            "Let's head back and report. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        "#4P#1002FRight!\x02",
    )

    CloseMessageWindow()
    OP_28(0x72, 0x1, 0x4)
    Jump("loc_665")

    label("loc_403")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_43D")

    ChrTalk(    #7
        0x105,
        "#043FHm? Did someone misplace this?\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F5")

    label("loc_43D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_476")

    ChrTalk(    #8
        0x107,
        (
            "#064FDid someone drop this,\x01",
            "maybe?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F5")

    label("loc_476")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CA")

    ChrTalk(    #9
        0x104,
        (
            "#030FHmm. Someone's lost treasure,\x01",
            "it seems. Most intriguing.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F5")

    label("loc_4CA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4F5")

    ChrTalk(    #10
        0x108,
        "#073FSomeone lose this?\x02",
    )

    CloseMessageWindow()

    label("loc_4F5")


    ChrTalk(    #11
        0x103,
        (
            "#026FThis is an odd place to\x01",
            "drop something, though.\x02\x03",

            "I can't see anyone coming\x01",
            "here for a picnic, that's for\x01",
            "sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        (
            "#1007FYeah, same here. \x02\x03",

            "#1003FHuh. It doesn't have an\x01",
            "inscription or anything. \x02\x03",

            "I wonder whose it is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        (
            "#020FWell, let's take it with us.\x02\x03",

            "If we really want to know,\x01",
            "we can ask around in town.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        "#1000FTrue enough! I'll hang on to it.\x02",
    )

    CloseMessageWindow()

    label("loc_665")

    OP_28(0x72, 0x1, 0x4000)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
