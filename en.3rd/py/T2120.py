from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2120   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2120.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T2120   ._SN',
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
        "O'Neil",                               # 9
        'Clem',                                 # 10
        'Target Camera',                        # 11
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
        'ED6_DT07/CH01100 ._CH',             # 00
        'ED6_DT07/CH02590 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01100P._CP',             # 00
        'ED6_DT07/CH02590P._CP',             # 01
    )

    DeclNpc(
        X                   = 30000,
        Z                   = 0,
        Y                   = 4500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_133",          # 01, 1
        "Function_2_134",          # 02, 2
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5E2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132")
    Event(0, 2)

    label("loc_132")

    Return()

    # Function_0_11A end

    def Function_1_133(): pass

    label("Function_1_133")

    Return()

    # Function_1_133 end

    def Function_2_134(): pass

    label("Function_2_134")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 30400, 0, 2300, 0)
    SetChrPos(0x14E, 32540, 0, 4580, 0)
    OP_6D(30260, 500, 3220, 0)
    OP_67(0, 5340, -10000, 0)
    OP_6B(2560, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #0
        0x11,
        "#774F#3SA happiness stone?!\x02",
    )

    OP_7C(0x0, 0xF0, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #1
        0x10,
        (
            "Indeed. It's a magical stone with a golden glow,\x01",
            "said to bring happiness to those who possess it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "I'm sure you're aware of how the Goddess created\x01",
            "this continent in ancient times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10,
        (
            "When that happened, Her power showered down\x01",
            "upon the land as an infinite number of particles,\x01",
            "their light radiant and divine.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "Most of those lights were fleeting, but not all of\x01",
            "them! Some of those particles of light remained,\x01",
            "hidden by mist in tall mountains.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10,
        "Over time, they grew in size, bit by bit...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        "And that is the origin of the happiness stones.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x11,
        "#772F#3STh-That's so cool!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        "Heheh! Isn't it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "Still, as you can imagine, it's exceptionally\x01",
            "rare that anyone finds one.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "After all, they only develop in the deepest regions\x01",
            "of the tallest mountains. That's not somewhere\x01",
            "people go every day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x11,
        (
            "#772FB-But you say you did?\x02\x03",

            "When you went on that expedition to the far\x01",
            "north, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "You got it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10,
        (
            "It was on the sacred mountain of Tegis, a perilous\x01",
            "place full of snow and ice.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "Even the slightest loss of footing would have sent\x01",
            "me cascading into the ravines below, and the never-\x01",
            "ceasing blizzards assaulted me from morn to night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "Before I knew it, even my food supply had run out,\x01",
            "and I was left wandering that white desert alone,\x01",
            "not knowing how much longer I had left...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "At times, I had to fend off the assault of vicious\x01",
            "monsters, while at other times, I found myself\x01",
            "almost plunged upside down the cliffsides.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "But while the experience may have been enough\x01",
            "to take out most ordinary men, it wasn't enough\x01",
            "to take ME down!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x10,
        (
            "I clung desperately to the razor-sharp ice walls,\x01",
            "making my way gradually farther into the mountain,\x01",
            "never once letting my resolve waver.\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x11, 0x0, 0x12C, 0x0, 0x12C, 0x1388)
    OP_95(0x11, 0x0, 0x12C, 0x0, 0x12C, 0x1388)

    ChrTalk(    #19
        0x11,
        "#771FMan, you're so COOL!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "No matter what happens, don't give up!\x01",
            "That's my policy, and it should be yours,\x01",
            "too!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #21
        0x10,
        "#3SBe like the mighty Captain O'Neil: invincible!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "Regardless, after overcoming countless trials and\x01",
            "obstacles before me, I finally found that faintly\x01",
            "glowing stone!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "My hands shook, but I reached out and picked it\x01",
            "up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "And the second I did, the raging winds stopped\x01",
            "as if they had never been blowing at all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "Then the morning sun began to shine down through\x01",
            "the clouds above.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "That light hit the stone, and it began to glow with\x01",
            "a glistening, radiant beauty...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x10,
        "It was like something out of this world.\x02",
    )

    CloseMessageWindow()

    def lambda_B76():
        OP_6B(2860, 4000)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_B76)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0x7D0)
    OP_21()
    Sleep(1000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/T2402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_2_134 end

    SaveToFile()

Try(main)
