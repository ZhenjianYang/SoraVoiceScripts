from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0200_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0200_1 ._SN',
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
    SetChrPos(0x101, 7870, 0, -15950, 0)
    SetChrPos(0xF7, 6710, 0, -16560, 0)
    SetChrPos(0xF8, 7910, 0, -17100, 0)
    SetChrPos(0xF9, 8940, 0, -16500, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_124")
    SetChrPos(0xF9, 7910, 0, -17100, 0)
    SetChrPos(0xF8, 8940, 0, -16500, 0)

    label("loc_124")

    OP_6D(8740, 0, -14620, 0)
    OP_67(0, 8360, -10000, 0)
    OP_6B(3250, 0)
    OP_6C(45000, 0)
    OP_6E(230, 0)
    OP_0D()

    ChrTalk(    #0
        0x101,
        (
            "#1002F#5PHey, don't these remind you of the\x01",
            "shape and symbols on the card?\x02\x03",

            "The boxes, I mean. The way they're\x01",
            "lined up's almost a perfect match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#020F#5PYou're right. Exactly five boxes,\x01",
            "too.\x02\x03",

            "Looks like we should investigate.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x101,
        "#1006F#5PYep, way ahead of you.\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x1EBE, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)

    ChrTalk(    #3
        0x101,
        "#1028F#6P...Where is it, where is it...\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_8F(0x101, 0x1ACC, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)
    Sleep(1500)
    OP_8F(0x101, 0x2152, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)
    Sleep(500)
    OP_8F(0x101, 0x1EBE, 0x0, 0xFFFFC6F8, 0x7D0, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0x101)

    ChrTalk(    #4
        0x101,
        "#1018F#6PBingo!\x02",
    )

    CloseMessageWindow()

    def lambda_356():
        TurnDirection(0xF7, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_356)

    def lambda_364():
        TurnDirection(0xF8, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_364)

    def lambda_372():
        TurnDirection(0xF9, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_372)
    OP_8C(0x101, 180, 400)
    Fade(1000)
    SetChrChipByIndex(0x101, 6)
    OP_0D()
    Sleep(1000)
    FadeToDark(300, 0, 100)
    OP_AD(0x240093, 0xBE, 0x64, 0x1F4)
    Sleep(1000)
    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05'The third key is in the city.\x01",
            "Search the belly of the Eight-Eyed Iron Beast.'\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        "#1015F#6PThat's what's on this new card.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x103,
        (
            "#022F#5PAn 'eight-eyed iron beast,' huh?\x02\x03",

            "It should be in the city, but what\x01",
            "could it possibly be?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_56A")

    ChrTalk(    #8
        0x104,
        (
            "#034FI'm up for another scavenger\x01",
            "hunt if everyone else is.\x02\x03",

            "Though, personally, I'd like to\x01",
            "find this beast quickly so we\x01",
            "can take a well-deserved break.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C")

    label("loc_56A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_605")

    ChrTalk(    #9
        0x108,
        (
            "#070FDon't think we've got much of a\x01",
            "choice but to walk around until\x01",
            "we bump into it, as always.\x02\x03",

            "Annoying, yeah, but hang in there.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C")

    label("loc_605")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_672")

    ChrTalk(    #10
        0x106,
        (
            "#050FI think our only option's to walk\x01",
            "around and check things out.\x02\x03",

            "Let's get movin'.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70C")

    label("loc_672")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_70C")

    ChrTalk(    #11
        0x105,
        (
            "#040FWe'll just have to keep up with\x01",
            "our investigation and walk around\x01",
            "a bit more.\x02\x03",

            "The next clue's right around the\x01",
            "corner, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70C")

    Sleep(500)
    Fade(1000)
    SetChrChipByIndex(0x101, 65535)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77C")

    ChrTalk(    #12
        0x101,
        (
            "#1016F#6PAhaha, no argument from me.\x02\x03",

            "#1006FWell, let's get it over with.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_77C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B8")

    ChrTalk(    #13
        0x101,
        "#1006F#6PNo problem. Let's get going.\x02",
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_7B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E3")

    ChrTalk(    #14
        0x101,
        "#1006F#6PYep, let's.\x02",
    )

    CloseMessageWindow()
    Jump("loc_815")

    label("loc_7E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_815")

    ChrTalk(    #15
        0x101,
        "#1006F#6PYep, let's get going.\x02",
    )

    CloseMessageWindow()

    label("loc_815")

    OP_28(0x77, 0x1, 0x20)
    OP_64(0x0, 0x1)
    EventEnd(0x0)
    Return()

    # Function_0_AA end

    SaveToFile()

Try(main)
